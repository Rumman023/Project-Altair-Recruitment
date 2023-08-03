import cv2 as cv
import numpy as np


def resize_window(image, result):
        # Resizing the window with new width and height
        down_width = 800
        down_height = 600
        down_points = (down_width, down_height)
        resize_down_original = cv.resize(image, down_points, interpolation=cv.INTER_LINEAR)
        resize_down_rwcolor = cv.resize(result, down_points, interpolation=cv.INTER_LINEAR)
        
        # Window pop out
        cv.imshow('Ankara Messi (Original)', resize_down_original)
        cv.imshow('Ankara Messi (Red & White Region)', resize_down_rwcolor)


def detect_red_and_white_regions(image):
        # Image conversion from BGR to HSV color space
        hsv_img = cv.cvtColor(image, cv.COLOR_BGR2HSV)

        # lower range of red color in HSV
        lower_range_red = (0, 100, 20)
        # upper range of red color in HSV
        upper_range_red = (10, 255, 255)

        # lower range of white color in HSV
        lower_range_white = (75, 0, 99)
        # upper range of white color in HSV
        upper_range_white = (179, 62, 255)

        # Mask creation for both red and white regions
        red_mask = cv.inRange(hsv_img, lower_range_red, upper_range_red)
        white_mask = cv.inRange(hsv_img, lower_range_white, upper_range_white)

        # Adding the masks to get regions with red and white colors
        red_and_white_mask = red_mask + white_mask

        # Applying the combined mask to the original image to extract the red and white regions
        red_and_white_regions = cv.bitwise_and(image, image, mask=red_and_white_mask)

        return red_and_white_regions


def analyze_goat(image_array):
        # Finding the minimumm and maximum pixel values in the image [2]
        min_value = np.min(image_array)
        max_value = np.max(image_array)

        # Finding the average pixel value in the image [3]
        mean_value = np.average(image_array)

        # Finding the total number of non-zero (foreground) pixels in the image [4]
        nonzero_pixels = np.count_nonzero(image_array)

        # Finding the total number of zero (background) pixels in the image [5]
        zero_pixels = np.size(image_array) - nonzero_pixels

        # Printing the calculated results on the terminal
        print("The minimum pixel value in the image is: ", min_value)
        print("The maximum pixel value in the image is: ", max_value)
        print("The average pixel value in the image is: ", mean_value)
        print("The number of foreground pixels is: ", nonzero_pixels)
        print("The number of background pixels is: ", zero_pixels)




# Read the input image from a file
image = cv.imread('GOAT.jpg')
# Call the detect_red_and_white_regions function and save the result image
result = detect_red_and_white_regions(image)

# Convert the input image from BGR to grayscale color space
image_array = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

# Call the analyze_goat function and save the display image
analyze_goat(image_array)

# Calling the window to execute and show the images
resize_window(image, result)


cv.waitKey(0)
cv.destroyAllWindows()
