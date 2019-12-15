import h5py, numpy as np, cv2, os

#PATH = 'examples/basic/output'
PATH_ = 'examples/bop/output/'
#PATH_ = 'experiments/occlusion_linemod/output'

dirs = ['lm',]
#dirs = ['tless/000001',]
# '003_cracker_box',
# '004_sugar_box',
# '005_tomato_soup_can',
# '006_mustard_bottle',
# '007_tuna_fish_can',
# '008_pudding_box',
# '009_gelatin_box',
# '010_potted_meat_can',
# '011_banana',
# '019_pitcher_base',
# '021_bleach_cleanser',
# '024_bowl',
# '025_mug',
# '035_power_drill',
# '036_wood_block',
# '037_scissors',
# '040_large_marker',
# '051_large_clamp',
# '052_extra_large_clamp',
# '061_foam_brick',
# ]

# dirs = [
# 'Ape',
# 'Can',
# 'Cat',
# 'Driller',
# 'Duck',
# 'Eggbox',
# 'Glue',
# 'Holepuncher'
# ]

for d in dirs:
	PATH = os.path.join(PATH_, d)
	
	filelist = os.listdir(PATH)
	filelist = [item for item in filelist if item.split('.')[-1] == 'hdf5']

	cv2.namedWindow('rgb', cv2.WINDOW_AUTOSIZE)
	cv2.moveWindow('rgb', 10, 10)
	# cv2.namedWindow('normal', cv2.WINDOW_AUTOSIZE)
	# cv2.moveWindow('normal', 1000, 10)

	for item in filelist:
	    f = h5py.File(os.path.join(PATH, item))
	    rgb = np.asarray(f.get('colors'), dtype=np.uint8)
	    #normal = np.asarray(f.get('normals'))
	    print('rgb shape: ', rgb.shape, 'rgb range: ' + str(rgb.min()) + ' to ' + str(rgb.max()))
	    cv2.imshow('rgb', rgb[:,:,::-1])
	    #cv2.imshow('normal', normal[:,:,::-1])
	    k = cv2.waitKey()
	    if k == 27:
	        break
