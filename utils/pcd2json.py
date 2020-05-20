import numpy as np
import open3d as o3d
import os
import json
from tqdm import tqdm

if __name__ == "__main__":
	pcd_file = '/home/a1/Desktop/Town2_02_0.pcd'
	pcd = o3d.io.read_point_cloud(pcd_file)

	points = np.round( np.asarray(pcd.points), 0)
	colors = np.round(np.asarray(pcd.colors) * 255, 0)

	unique_points, unique_indices = np.unique(points, return_index=True, axis=0)
	unique_colors = colors[unique_indices]

	# JSON
	cloud_data = []
	for i in tqdm(range(len(unique_points))):
		point = {
			"position": [unique_points[i][0],unique_points[i][1],unique_points[i][2] ],
			"normal": [0,0,0],
			"color": [int(unique_colors[i][0]), int(unique_colors[i][1]), int(unique_colors[i][2]) ]
		}
		cloud_data.append(point)

	print('write a json file...')
	cloud_json = json.dumps(cloud_data, indent=2)
	with open('/home/a1/git/abcde/help.json', 'w') as json_file:
		json.dump(cloud_data, json_file)
	print('complete...')

