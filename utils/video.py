import os
import cv2


def generate_video(image_dir, video_path):
	images = [img for img in os.listdir(image_dir) if img.endswith('.jpg')]
	images.sort()
	frame = cv2.imread(os.path.join(image_dir, images[0]))
	height, width, layers = frame.shape
	video = cv2.VideoWriter(video_path, 0, 10, (width, height))
	for image in images:
	    video.write(cv2.imread(os.path.join(image_dir, image)))
	cv2.destroyAllWindows()
	video.release()


if __name__ == '__main__':
	image_dir = '../yolo/yolo-predictions'
	video_path = '../yolo/video.avi'
	generate_video(image_dir, video_path)
