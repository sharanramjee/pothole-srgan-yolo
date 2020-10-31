import os
import numpy as np
from PIL import Image
from ISR.models import RDN


def load_test_set(test_spec_path):
	with open(test_spec_path, 'r') as test_spec_file:
		test_set_paths = test_spec_file.readlines()
	test_set_files = [os.path.basename(test_set_path[:-1]) for test_set_path in test_set_paths]
	return test_set_files


def upscale_image(downscaled_img_path):
	img = Image.open(downscaled_img_path)
	lr_img = np.array(img)
	rdn = RDN(weights='psnr-small')
	sr_img = rdn.predict(lr_img, by_patch_of_size=50)
	sr_img_arr = Image.fromarray(sr_img)
	return sr_img_arr


def upscale_test_set(test_spec_path, downscaled_dir, upscaled_dir):
	test_set_files = load_test_set(test_spec_path)
	for downscaled_img_file in test_set_files:
		print('Upscaling:', downscaled_img_file)
		downscaled_img_path = downscaled_dir + '/' + downscaled_img_file
		upscaled_img = upscale_image(downscaled_img_path)
		upscaled_img_path = upscaled_dir + '/' + downscaled_img_file
		upscaled_img.save(upscaled_img_path)


if __name__ == '__main__':
	# Set path to file specifying test split
	test_spec_path = 'splits/train.txt'
	# Set the path to the dir with downscaled images
	downscaled_dir = '../data/downscaled_360p'
	# Set the path to dir to save the upscaled images
	upscaled_dir = 'output/upscaled_720p/train'
	# Upscale the images in the test set
	upscale_test_set(test_spec_path, downscaled_dir, upscaled_dir)