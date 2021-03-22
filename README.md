# OpenCv_Basics

OpenCV (Open Source Computer Vision Library) is a library of programming functions mainly aimed at real-time computer vision.

## Basic Functions
<img src="https://github.com/HarshitDolu/OpenCv_Basics/blob/main/demo/2.png" width="800">

## Resize and Crop
<img src="https://github.com/HarshitDolu/OpenCv_Basics/blob/main/demo/3.png" width="800">

## Shapes and Text
<img src="https://github.com/HarshitDolu/OpenCv_Basics/blob/main/demo/4.png" width="800">

## Wrap perspective

In Perspective Transformation, , we can change the perspective of a given image or video for getting better insights about the required information. In Perspective Transformation, we need provide the points on the image from which want to gather information by changing the perspective. We also need to provide the points inside which we want to display our image. Then, we get the perspective transform from the two given set of points and wrap it with the original image.

We use cv2.getPerspectiveTransform and then cv2.warpPerspective .

<img src="https://github.com/HarshitDolu/OpenCv_Basics/blob/main/demo/5.png" width="800">

## Thresholding

Thresholding is a technique in OpenCV, which is the assignment of pixel values in relation to the threshold value provided. In thresholding, each pixel value is compared with the threshold value. If the pixel value is smaller than the threshold, it is set to 0, otherwise, it is set to a maximum value (generally 255).

<img src="https://github.com/HarshitDolu/OpenCv_Basics/blob/main/demo/6.png" width="800">

## Smoothing

After loading an image, this code applies a linear image filter and show the filtered images sequentially.

The filter used here the most simplest one called homogeneous smoothing or box filter.

It does smoothing by sliding a kernel (filter) across the image. Each pixel value will be calculated based on the value of the kernel and the overlapping pixel's value of the original image. Mathematically speaking, we do convolution operation on an image with a kernel. What kernel we're applying to an image makes difference to the the result of the smoothing. What we do for this filter is assigning an average values of a pixel's neighbors.

<img src="https://github.com/HarshitDolu/OpenCv_Basics/blob/main/demo/7.png" width="800">

## Color Tracking
<img src="https://github.com/HarshitDolu/OpenCv_Basics/blob/main/demo/8.png" width="800">

## Image masking

When talking about editing and processing images the term 'masking' refers to the practice of using a mask to protect a specific area of an image, just as you would use masking tape when painting your house. Masking an area of an image protects that area from being altered by changes made to the rest of the image.

<img src="https://github.com/HarshitDolu/OpenCv_Basics/blob/main/demo/9.jpeg" width="800">

## Contours

Contours help us identify the shapes present in an image. Contours are defined as the line joining all the points along the boundary of an image that are having the same intensity. The findContours function in OPenCV helps us identify the contours. Similarly the drawContours function help us draw the contours.

<img src="https://github.com/HarshitDolu/OpenCv_Basics/blob/main/demo/10.png" width="800">

## image histogram

An image histogram is a type of histogram that acts as a graphical representation of the tonal distribution in a digital image.[1] It plots the number of pixels for each tonal value. By looking at the histogram for a specific image a viewer will be able to judge the entire tonal distribution at a glance.

<img src="https://github.com/HarshitDolu/OpenCv_Basics/blob/main/demo/11.png" width="800">

## Morphological Transformations

Morphology is a broad set of image processing operations that process images based on shapes. ... In a morphological operation, the value of each pixel in the output image is based on a comparison of the corresponding pixel in the input image with its neighbors.

<img src="https://github.com/HarshitDolu/OpenCv_Basics/blob/main/demo/12.png" width="800">

## Hough Transform

The Hough Transform is a method that is used in image processing to detect any shape, if that shape can be represented in mathematical form. It can detect the shape even if it is broken or distorted a little bit.

<img src="https://github.com/HarshitDolu/OpenCv_Basics/blob/main/demo/13.png" width="800">

## Harris corner detector

Harris Corner detection algorithm was developed to identify the internal corners of an image. The corners of an image are basically identified as the regions in which there are variations in large intensity of the gradient in all possible dimensions and directions. Corners extracted can be a part of the image features, which can be matched with features of other images, and can be used to extract accurate information. Harris Corner Detection is a method to extract the corners from the input image and to extract features from the input image.

<img src="https://github.com/HarshitDolu/OpenCv_Basics/blob/main/demo/14.png" width="800">

## Face detection

Face detection using Haar cascades is a machine learning based approach where a cascade function is trained with a set of input data. OpenCV already contains many pre-trained classifiers for face, eyes, smiles, etc.<br>
The detection works only on grayscale images. So it is important to convert the color image to grayscale. <br>
detectMultiScale function (line 10) is used to detect the faces. It takes 3 arguments — the input image, scaleFactor and minNeighbours.

<img src="https://github.com/HarshitDolu/OpenCv_Basics/blob/main/demo/15.png" width="800">

## Face Recognition

Automatic face recognition is all about extracting those meaningful features from an image, putting them into a useful representation and performing some kind of classification on them.

Face recognition based on the geometric features of a face is probably the most intuitive approach to face recognition. One of the first automated face recognition systems was described in : marker points (position of eyes, ears, nose) were used to build a feature vector (distance between the points, angle between them.

<img src="https://github.com/HarshitDolu/OpenCv_Basics/blob/main/demo/16.png" width="800">


