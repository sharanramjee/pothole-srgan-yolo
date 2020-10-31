import os
from os.path import isfile, join
from PIL import Image


def make_dir(path):
	if not os.path.exists(path):
	    os.makedirs(path)


def downscale_img(img_file_path, downscale_resolution):
	img = Image.open(img_file_path)
	downscaled_image = img.resize(downscale_resolution)
	return downscaled_image
	

def copy_img_file(img_file_path, save_dir, downscale_resolution):
	# Generate the path to save the image file
	img_file_name = os.path.basename(img_file_path)
	print('Downscaling image:', img_file_name)
	save_path = save_dir + '/' + img_file_name
	# Downscale and save the image
	img = downscale_img(img_file_path, downscale_resolution)
	img.save(save_path)


def copy_txt_file(txt_file_path, save_dir):
	os.system('cp ' + txt_file_path + ' ' + save_dir)


def label_to_box(txt_file_path, save_dir, downscale_resolution):
	txt_file_name = os.path.basename(txt_file_path)
	split_name = os.path.splitext(txt_file_name)
	img_file_path = save_dir + '/' + split_name[0] + '.jpg'
	box_labels = list()
	with open(txt_file_path, 'r') as file:
			labels = file.readlines()
	for label in labels:
		split_label = label.split(' ')
		object_class = int(split_label[0])
		x_center = float(split_label[1]) * downscale_resolution[0]
		y_center = float(split_label[2]) * downscale_resolution[1]
		width = float(split_label[3]) * downscale_resolution[0]
		height = float(split_label[4]) * downscale_resolution[1]
		# Convert to boundng box
		x1 = int(x_center - height / 2)
		x2 = int(x_center + height / 2)
		y1 = int(y_center - width / 2)
		y2 = int(y_center + width / 2)
		box_label = ','.join([str(x1), str(y1), str(x2), str(y2), str(object_class)])
		box_labels.append(box_label)
	box_labels = [img_file_path] + box_labels
	return ' '.join(box_labels)


def create_annotations(label_dir, save_dir, downscale_resolution):
	txt_files = [join(label_path, f) for f in os.listdir(label_path) if isfile(join(label_path, f))]
	txt_files.sort()
	annotations_file_path = save_dir + '/annotations_' + str(downscale_resolution[0]) + '_' + str(downscale_resolution[1]) + '.txt' 
	with open(annotations_file_path, 'w') as annotations_file:
		for txt_file in txt_files:
			txt_labels = label_to_box(txt_file, save_dir, downscale_resolution)
			annotations_file.write(txt_labels)
			annotations_file.write('\n')


def create_downscaled_dataset(dataset_path, label_path, downscaled_path, downscale_resolution):
	image_files = [join(dataset_path, f) for f in os.listdir(dataset_path) if isfile(join(dataset_path, f)) and os.path.splitext(f)[1]=='.jpg']
	image_files.sort()
	# Copy image file (after downscaling) to new downscaled dataset dir
	for image_file in image_files:
		copy_img_file(image_file, downscaled_path, downscale_resolution)
	create_annotations(label_path, downscaled_path, downscale_resolution)

	
if __name__ == '__main__':
	# Set downscale resolution
	# original: (3680, 2760)
	# original_downscaled: (920, 690)
	# 1080p: (1920, 1080)
	# 4k: (3840, 2160)
	downscale_resolution = (640, 360)
	# Set downscale dataset path
	downscaled_path = '../data/downscaled_360p'
	make_dir(downscaled_path)
	# Set labels directory path
	label_path = '../data/labels'
	# Get original dataset path
	original_path = '../data/original'
	# Create downscaled dataset
	create_downscaled_dataset(original_path, label_path, downscaled_path, downscale_resolution)
