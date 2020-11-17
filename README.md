# pothole-srgan-yolo
Autumn 2020 CS 230 project on pothole detection using SRGAN and YOLO Net.

Authors: Sharan Ramjee and Moo Jin Kim

## Utils
Specify path to original images and path to rescaled/downscaled images: $ python3 downscale.py

## SRGAN
Specify path to test set, path to downscaled images, and path to upscaled images: $ python3 srgan_isr.py

## YOLOv4
(1) To train YOLOv4:
```
$ ./darknet detector train <DATA_CONFIG_FILE> <NETWORK_CONFIG_FILE> <WEIGHTS_FILE>
```
Example:
```
$ ./darknet detector train cfg/obj-720p.data cfg/yolo-pothole-normal-train.cfg pothole_weights/yolo-pothole-720p-train_last.weights
```

(2) To evaluate (get mAP score of) YOLOv4 model on val or test set:
```
$ ./darknet detector map <DATA_CONFIG_FILE> <NETWORK_CONFIG_FILE> <WEIGHTS_FILE>
```
Example:
```
$ ./darknet detector map cfg/obj-720p-test.data cfg/yolo-pothole-normal-test.cfg pothole_weights/yolo-pothole-720p-train_last.weights
```

(3) To make predictions on image with YOLOv4 model:
```
$ ./darknet detector test <DATA_CONFIG_FILE> <NETWORK_CONFIG_FILE> <WEIGHTS_FILE> <IMAGE_FILE>
```
Example:
```
$ ./darknet detector test cfg/obj-720p-test.data cfg/yolo-pothole-normal-test.cfg pothole_weights/yolo-pothole-720p-train_last.weights some_image.jpg
```

More detailed steps for YOLOv4, including requirements and setup, can be found here: https://github.com/AlexeyAB/darknet
