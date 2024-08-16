import cv2


def average_blur(img, kernel_size: int):
    """
    This function applies Average Blur to the input image.
    :param img: entry image
    :param kernel_size: an odd value for the kernel size
    :return: blurred image
    """
    return cv2.blur(img, (kernel_size, kernel_size))


def gaussian_blur(img, kernel_size: tuple):
    """
    This function applies Gaussian Blur to the input image.
    Gaussian blur makes our image more smooth and blurred.
    :param img: entry image
    :param kernel_size: a tuple with odd values for the kernel size in x and y direction
    :return: blurred image
    """
    return cv2.GaussianBlur(img, kernel_size, 0)


def median_blur(img, kernel_size: int):
    """
    This function applies Median Blur to the input image.
    median blur removes the salt and pepper like noises from the image.
    :param img: entry image
    :param kernel_size: an odd value for the kernel size
    :return: blurred image
    """
    return cv2.medianBlur(img, kernel_size)


def bilateral_filter(img, d: int, sigma_color: int, sigma_space: int):
    """
    This function applies Bilateral Filter to the input image.
    Bilateral filter is a non-linear filter that preserves the edges.
    :param img: entry image
    :param d: an odd value for the diameter of each pixel neighborhood that is used during filtering.
    :param sigma_color: filter sigma in the color space.
    :param sigma_space: filter sigma in the coordinate space.
    :return: filtered image
    """
    return cv2.bilateralFilter(img, d, sigma_color, sigma_space)


image = cv2.imread(r"src/no_entry_test.jpg")
cv2.imshow("Original Image", image)

# Applying Average Blur
blurred_image = average_blur(image, 7)
cv2.imshow("Average Blur", blurred_image)
cv2.waitKey(0)
cv2.destroyWindow("Average Blur")

# Applying Gaussian Blur
blurred_image = gaussian_blur(image, (7, 7))
cv2.imshow("Gaussian Blur", blurred_image)
cv2.waitKey(0)
cv2.destroyWindow("Gaussian Blur")

# Applying Median Blur
blurred_image = median_blur(image, 7)
cv2.imshow("Median Blur", blurred_image)
cv2.waitKey(0)
cv2.destroyWindow("Median Blur")
# Applying Bilateral Filter
filtered_image = bilateral_filter(image, 7, 75, 75)
cv2.imshow("Bilateral Filter", filtered_image)

cv2.waitKey(0)
cv2.destroyAllWindows()

