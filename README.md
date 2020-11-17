# pothole-srgan-yolo
Autumn 2020 CS 230 project on pothole detection using SRGAN and YOLO Net.

Authors: Sharan Ramjee and Moo Jin Kim

Project Summary Video: https://youtu.be/rwbdRwAr6Mk

## Utils
(1) To downscale images, specify path to original images and path to rescaled/downscaled images in downscale.py and run:
```
$ python3 downscale.py
```

## SRGAN
(1) To run the SRGAN, specify path to test set, path to downscaled images, and path to upscaled images in srgan_isr.py and run:
```
$ python3 srgan_isr.py
```

More detailed steps for the SRGAN, including requirements and setup, can be found here: https://github.com/idealo/image-super-resolution

## YOLOv4
(1) To train YOLOv4:
```
$ ./darknet detector train <DATA_CONFIG_FILE> <NETWORK_CONFIG_FILE> <WEIGHTS_FILE>
```
Example:
```
$ ./darknet detector train cfg/obj-720p-train.data cfg/yolo-pothole-720p-train.cfg pothole_weights/yolo-pothole-720p-train_last.weights
```

(2) To evaluate (get mAP score of) YOLOv4 model on val or test set:
```
$ ./darknet detector map <DATA_CONFIG_FILE> <NETWORK_CONFIG_FILE> <WEIGHTS_FILE>
```
Example:
```
$ ./darknet detector map cfg/obj-720p-test.data cfg/yolo-pothole-720p-test.cfg pothole_weights/yolo-pothole-720p-train_last.weights
```

(3) To run inference on input image with YOLOv4 model, outputting image (predictions.jpg) containing bounding boxes:
```
$ ./darknet detector test <DATA_CONFIG_FILE> <NETWORK_CONFIG_FILE> <WEIGHTS_FILE> <IMAGE_FILE>
```
Example:
```
$ ./darknet detector test cfg/obj-720p-test.data cfg/yolo-pothole-720p-test.cfg pothole_weights/yolo-pothole-720p-train_last.weights some_image.jpg
```

More detailed steps for YOLOv4, including requirements and setup, can be found here: https://github.com/AlexeyAB/darknet
