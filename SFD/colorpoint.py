import numpy as np
from PIL import Image
from kitti_object import *
from vis import *


def color(data_idx, split='training'):
    dataset = kitti_object('./', split)

    calib = dataset.get_calibration(data_idx)
    img_rgb = dataset.get_image(data_idx)
    # print(np.shape(img_rgb))
    if 's' in sys.argv:
        points = dataset.get_lidar(data_idx)
    if 'd' in sys.argv:
        points = dataset.get_lidar_dpc(data_idx)
    if 'm' in sys.argv:
        points = mask(points)
    # print(np.shape(points))

    pc_2d = calib.project_velo_to_image(points[:,:3]).astype(int)
    # print(np.shape(pc_2d))

    pc_color = np.ones((np.shape(pc_2d)[0],3))
    # print(np.shape(pc_color))

    for i,point in enumerate(pc_2d):
        try:
            pc_color[i]=img_rgb[point[1]][point[0]]
        except:
            continue

    return points,pc_color,pc_2d


def main():
    with open('kitti_infos_val.pkl', 'rb') as f:
        gt_infos = pickle.load(f)

    with open('second_dpc_cat_epoch_82.pkl', 'rb') as f:
        pred_infos = pickle.load(f)

    with open('second_epoch75.pkl', 'rb') as f:
        ori_infos = pickle.load(f)

    i=1039
    while(True):
        idx = getIndex(i, gt_infos)

        vis = open3d.visualization.Visualizer()
        if 's' in sys.argv:
            vis.create_window(window_name='Visualization, idx: '
                            + idx, width=1080,
                            height=540)
        else:
            vis.create_window(window_name='Visualization, idx: '
                            + idx, width=1080,
                            height=540)


        vis.get_render_option().point_size=2.0
        vis.get_render_option().background_color=np.ones(3)


        points,pc_color,pc_2d=color(int(idx))
        draw_points(vis, points,color=pc_color/256)


        if 'g' in sys.argv:
            boxes=getGTBox(i,gt_infos)
            draw_boxes(vis, boxes=boxes,color=[1,0,0])
        if 'p' in sys.argv:
            boxes=getPredBox(i,pred_infos)
            draw_boxes(vis, boxes=boxes)
        if 'o' in sys.argv:
            boxes=getPredBox(i,ori_infos)
            draw_boxes(vis, boxes=boxes,color=[0,0,1])


        # draw origin
        # origin = open3d.geometry.TriangleMesh.create_coordinate_frame(size=1.0)
        # vis.add_geometry(origin)

        # set view point
        ctr=vis.get_view_control()
        param = open3d.io.read_pinhole_camera_parameters('viewpoint.json')
        ctr.convert_from_pinhole_camera_parameters(param)

        # display
        vis.run()

        # save view point
        # param = ctr.convert_to_pinhole_camera_parameters()
        # open3d.io.write_pinhole_camera_parameters('viewpoint.json', param)


        del ctr
        i+=1

def find():
    with open('kitti_infos_val.pkl', 'rb') as f:
        gt_infos = pickle.load(f)
    i=1000
    while(True):
        idx = getIndex(i, gt_infos)
        print (str(i) + ' ' + idx)
        i+=1
        if int(idx) == 2086:
            break

if __name__ == "__main__":
    main()
    # find()

# python .\colorpoint.py d p g m