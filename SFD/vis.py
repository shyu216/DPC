import open3d
import numpy as np
import matplotlib.pyplot as plt
import pickle
import sys

def getIndex(i,infos):
    return infos[i]['point_cloud']['lidar_idx']
    
def getSparsePointCloud(idx):
    points = np.fromfile('training/velodyne/'+idx+'.bin', dtype=np.float32).reshape(-1, 4)
    return points

def getDensePointCloud(idx):
    points = np.fromfile('training/velodyne_dpc/'+idx+'.bin', dtype=np.float32).reshape(-1, 4)
    return points

def getGTBox(i, infos):
    return infos[i]['annos']['gt_boxes_lidar']

def getPredBox(i, infos):
    return infos[i]['boxes_lidar']

def translate_boxes_to_open3d_instance(gt_boxes):
    """
             4-------- 6
           /|         /|
          5 -------- 3 .
          | |        | |
          . 7 -------- 1
          |/         |/
          2 -------- 0
    """
    center = gt_boxes[0:3] # center
    lwh = gt_boxes[3:6] #length width height
    axis_angles = np.array([0, 0, gt_boxes[6] + 1e-10]) # rotation angle
    rot = open3d.geometry.get_rotation_matrix_from_axis_angle(axis_angles)
    box3d = open3d.geometry.OrientedBoundingBox(center, rot, lwh)

    line_set = open3d.geometry.LineSet.create_from_oriented_bounding_box(box3d)

    lines = np.asarray(line_set.lines)
    lines = np.concatenate([lines, np.array([[1, 4], [7, 6]])], axis=0)
    line_set.lines = open3d.utility.Vector2iVector(lines)

    return line_set, box3d

def draw_boxes(vis, boxes, color=[0, 1, 0]):
    for i in range(boxes.shape[0]):
        line_set, box3d = translate_boxes_to_open3d_instance(boxes[i])
        line_set.paint_uniform_color(color)
        vis.add_geometry(line_set)

def draw_points(vis, points, color=None):

    pts = open3d.geometry.PointCloud()
    pts.points = open3d.utility.Vector3dVector(points[:, :3])
    if color is None:
        pts.colors = open3d.utility.Vector3dVector(
            np.ones((points.shape[0], 3)))
    else:
        pts.colors = open3d.utility.Vector3dVector(color)
    vis.add_geometry(pts)


def mask(depth_pc_velo):
    cbox = np.array([[0, 70.4], [-40, 40], [-3, 1]])
    # x:[0, 70.4], y:[-40, 40], z:[-3, 2]
    
    depth_box_fov_inds = (
                (depth_pc_velo[:, 0] < cbox[0][1])
                & (depth_pc_velo[:, 0] >= cbox[0][0])
                & (depth_pc_velo[:, 1] < cbox[1][1])
                & (depth_pc_velo[:, 1] >= cbox[1][0])
                & (depth_pc_velo[:, 2] < cbox[2][1])
                & (depth_pc_velo[:, 2] >= cbox[2][0])
            )
    depth_pc_velo = depth_pc_velo[depth_box_fov_inds]
    return depth_pc_velo
def main():
    with open('kitti_infos_val.pkl', 'rb') as f:
        gt_infos = pickle.load(f)

    with open('second_dpc_cat_epoch_82.pkl', 'rb') as f:
        pred_infos = pickle.load(f)


    i=10
    while(True):
        idx = getIndex(i, gt_infos)

        vis = open3d.visualization.Visualizer()
        if 's' in sys.argv:
            vis.create_window(window_name='Visualization, idx: '
                            + idx, width=900,
                            height=600)
        else:
            vis.create_window(window_name='Visualization, idx: '
                            + idx, width=900,
                            height=600,left=1000)


        vis.get_render_option().point_size=2.0
        vis.get_render_option().background_color=np.zeros(3)

        if 's' in sys.argv:
            points = getSparsePointCloud(idx)
        if 'd' in sys.argv:
            points = getDensePointCloud(idx)
        if 'm' in sys.argv:
            points = mask(points)
        if 'g' in sys.argv:
            boxes=getGTBox(i,gt_infos)
            draw_boxes(vis, boxes=boxes,color=[1,0,0])
        if 'p' in sys.argv:
            boxes=getPredBox(i,pred_infos)
            draw_boxes(vis, boxes=boxes)

        draw_points(vis, points)

        # draw origin
        origin = open3d.geometry.TriangleMesh.create_coordinate_frame(size=1.0)
        vis.add_geometry(origin)

        # set view point
        ctr=vis.get_view_control()
        param = open3d.io.read_pinhole_camera_parameters('viewpoint.json')
        ctr.convert_from_pinhole_camera_parameters(param)

        # display
        vis.run()

        # save view point
        param = ctr.convert_to_pinhole_camera_parameters()
        open3d.io.write_pinhole_camera_parameters('viewpoint.json', param)


        del ctr
        i+=1

