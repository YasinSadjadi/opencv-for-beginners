import cv2


def thresh_binary(img, threshold=127):
    """
    This function applies binary thresholding to the input image.
    :param img: enter the image
    :param threshold: threshold value, default is 127
    :return:
    """
    return cv2.threshold(img, threshold, 255, cv2.THRESH_BINARY)[1]


def inverse_thresh_binary(img, threshold=127):
    """
    This function applies inverse binary thresholding to the input image.
    :param img: enter the image
    :param threshold: threshold value, default is 127
    :return:
    """
    return cv2.threshold(img, threshold, 255, cv2.THRESH_BINARY_INV)[1]


def otsu_thresh_binary(img):
    """
    This function applies Otsu's binary thresholding to the input image.
    :param img: enter the image
    :return:
    """
    return cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]


def trunc_thresh_binary(img, threshold=127):
    """
    This function applies truncated binary thresholding to the input image.
    :param img: enter the image
    :param threshold: threshold value, default is 127
    :return:
    """
    return cv2.threshold(img, threshold, 255, cv2.THRESH_TRUNC)[1]


def tozero_thresh_binary(img, threshold=127):
    """
    This function applies tozero binary thresholding to the input image.
    :param img: enter the image
    :param threshold: threshold value, default is 127
    :return:
    """
    return cv2.threshold(img, threshold, 255, cv2.THRESH_TOZERO)[1]


def tozero_inv_thresh_binary(img, threshold=127):
    """
    This function applies inverse tozero binary thresholding to the input image.
    :param img: enter the image
    :param threshold: threshold value, default is 127
    :return:
    """
    return cv2.threshold(img, threshold, 255, cv2.THRESH_TOZERO_INV)[1]


def adaptive_thresh_gaussian(img, block_size=11, C=2):
    """
    This function applies adaptive binary thresholding to the input image.
    :param img: enter the image
    :param block_size: block size, default is 11
    :param C: constant, default is 2
    :return:
    """
    return cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, block_size, C)


def adaptive_thresh_mean(img, block_size=11, C=2):
    """
    This function applies adaptive binary thresholding to the input image.
    :param img: enter the image
    :param block_size: block size, default is 11
    :param C: constant, default is 2
    :return:
    """
    return cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, block_size, C)


image = cv2.imread("src/no_entry_test.jpg", cv2.IMREAD_GRAYSCALE)
cv2.imshow("Original Image", image)

# Applying binary thresholding
binary_image = thresh_binary(image, 127)
cv2.imshow("Binary Image", binary_image)
cv2.waitKey(0)
cv2.destroyWindow("Binary Image")

# Applying inverse binary thresholding
inverse_binary_image = inverse_thresh_binary(image, 127)
cv2.imshow("Inverse Binary Image", inverse_binary_image)
cv2.waitKey(0)
cv2.destroyWindow("Inverse Binary Image")

# Applying Otsu's binary thresholding
otsu_binary_image = otsu_thresh_binary(image)
cv2.imshow("Otsu Binary Image", otsu_binary_image)
cv2.waitKey(0)
cv2.destroyWindow("Otsu Binary Image")

# Applying truncated binary thresholding
trunc_binary_image = trunc_thresh_binary(image, 127)
cv2.imshow("Truncated Binary Image", trunc_binary_image)
cv2.waitKey(0)
cv2.destroyWindow("Truncated Binary Image")

# Applying tozero binary thresholding
tozero_binary_image = tozero_thresh_binary(image, 127)
cv2.imshow("Tozero Binary Image", tozero_binary_image)
cv2.waitKey(0)
cv2.destroyWindow("Tozero Binary Image")


# Applying inverse tozero binary thresholding
tozero_inv_binary_image = tozero_inv_thresh_binary(image, 127)
cv2.imshow("Inverse Tzero Binary Image", tozero_inv_binary_image)
cv2.waitKey(0)
cv2.destroyWindow("Inverse Tzero Binary Image")

# Applying adaptive gaussian thresholding
adaptive_gaussian_image = adaptive_thresh_gaussian(image, 11, 2)
cv2.imshow("Adaptive Gaussian Image", adaptive_gaussian_image)
cv2.waitKey(0)
cv2.destroyWindow("Adaptive Gaussian Image")

# Applying adaptive mean thresholding
adaptive_mean_image = adaptive_thresh_mean(image, 11, 2)
cv2.imshow("Adaptive Mean Image", adaptive_mean_image)
cv2.waitKey(0)
cv2.destroyWindow("Adaptive Mean Image")
