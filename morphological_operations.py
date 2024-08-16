import cv2
import numpy as np


def erosion(img, kernel):
    """
    Performs erosion on the image using the given kernel.
    erosion is a mathematical morphology operation that is used to remove small objects
     from the foreground of an image.
    :param img: entry image
    :param kernel: kernel to be used for erosion
    :return: eroded image
    """
    return cv2.erode(img, kernel)


def dilation(img, kernel):
    """
    Performs dilation on the image using the given kernel.
    dilation is a mathematical morphology operation that is used to enlarge the foreground of an image.
    :param img: entry image
    :param kernel: kernel to be used for dilation
    :return: dilated image
    """
    return cv2.dilate(img, kernel)


def opening(img, kernel):
    """
    Performs opening on the image using the given kernel.
    opening is a mathematical morphology operation that is used to remove small objects
     from the foreground of an image and then dilates the resulting image.
    :param img: entry image
    :param kernel: kernel to be used for opening
    :return: opened image
    """
    return cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)


def closing(img, kernel):
    """
    Performs closing on the image using the given kernel.
    closing is a mathematical morphology operation that is used to dilate the foreground of an image
     and then removes small objects from the resulting image.
    :param img: entry image
    :param kernel: kernel to be used for closing
    :return: closed image
    """
    return cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)


def gradient(img, kernel):
    """
    Performs gradient on the image using the given kernel.
    gradient is a mathematical morphology operation that is used to find the edges of an image.
    :param img: entry image
    :param kernel: kernel to be used for gradient
    :return: gradient image
    """
    return cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)


def top_hat(img, kernel):
    """
    Performs top hat on the image using the given kernel.
    top hat is a mathematical morphology operation that is used to subtract the background of an image
     from the foreground of an image.
    :param img: entry image
    :param kernel: kernel to be used for top hat
    :return: top hat image
    """
    return cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)


def black_hat(img, kernel):
    """
    Performs black hat on the image using the given kernel.
    black hat is a mathematical morphology operation that is used to subtract the foreground of an image
     from the background of an image.
    :param img: entry image
    :param kernel: kernel to be used for black hat
    :return: black hat image
    """
    return cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)


def canny(img, threshold1, threshold2):
    """
    Performs canny edge detection on the image using the given thresholds.
    canny edge detection is a mathematical morphology operation that is used to find the edges of an image.
    :param img: entry image
    :param threshold1: canny threshold1
    :param threshold2: canny threshold2
    :return: cannied image
    """
    return cv2.Canny(img, threshold1, threshold2)


# Example usage:
# np.ones creates a 5x5 kernel with all elements set to 1.(the I matrix in math)
kernel = np.ones((5, 5), np.uint8)

# read the image
image = cv2.imread(r"src/no_entry_test.jpg")
cv2.imshow("Original Image", image)

# perform erosion on the image using the kernel
erosion_image = erosion(image, kernel)
cv2.imshow("Erosion Image", erosion_image)
cv2.waitKey(0)
cv2.destroyWindow("Erosion Image")

# perform dilation on the image using the kernel
dilation_image = dilation(image, kernel)
cv2.imshow("Dilation Image", dilation_image)
cv2.waitKey(0)
cv2.destroyWindow("Dilation Image")

# perform opening on the image using the kernel
opening_image = opening(image, kernel)
cv2.imshow("Opening Image", opening_image)
cv2.waitKey(0)
cv2.destroyWindow("Opening Image")

# perform closing on the image using the kernel
closing_image = closing(image, kernel)
cv2.imshow("Closing Image", closing_image)
cv2.waitKey(0)
cv2.destroyWindow("Closing Image")

# perform gradient on the image using the kernel
gradient_image = gradient(image, kernel)
cv2.imshow("Gradient Image", gradient_image)
cv2.waitKey(0)
cv2.destroyWindow("Gradient Image")

# perform top hat on the image using the kernel
top_hat_image = top_hat(image, kernel)
cv2.imshow("Top Hat Image", top_hat_image)
cv2.waitKey(0)
cv2.destroyWindow("Top Hat Image")


# perform black hat on the image using the kernel
black_hat_image = black_hat(image, kernel)
cv2.imshow("Black Hat Image", black_hat_image)
cv2.waitKey(0)
cv2.destroyWindow("Black Hat Image")


# perform canny edge detection on the image using the given thresholds
canny_image = canny(image, 100, 200)
cv2.imshow("Canny Image", canny_image)
cv2.waitKey(0)
cv2.destroyWindow("Canny Image")

