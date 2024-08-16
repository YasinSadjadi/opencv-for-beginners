import cv2


def resizing_image(image, image_size: tuple):
    """
    This function resizes the image to the given size.
    :param image: entry image
    :param image_size: a tuple of (width, height)
    :return: resized image
    """
    return cv2.resize(image, image_size)


def cutting_image(image, down_left_corner: tuple, up_right_corner: tuple):
    """
    This function cuts the image from the given down_left_corner to the given up_right_corner.
    :param image: entry image
    :param down_left_corner: a tuple of (x, y)
    :param up_right_corner: a tuple of (x, y)
    :return: cut image
    """
    cutted = image[down_left_corner[1]:up_right_corner[1], down_left_corner[0]:up_right_corner[0]]

    return cutted


loaded_image = cv2.imread('src/no_entry_test.jpg')

resized_image = resizing_image(loaded_image, (250, 200))
cv2.imshow('Resized Image', resized_image)
cutted_image = cutting_image(loaded_image, (100, 100), (400, 400))
cv2.imshow('Cutted Image', cutted_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
