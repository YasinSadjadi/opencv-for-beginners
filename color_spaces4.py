import cv2


def rgb_color_space(img):
    """
    the read image of opencv is always in BGR format
    this function will convert the image to RGB color space
    :param img: entry image
    :return: RGB image
    """
    return cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


def hsv_color_space(img):
    """
    this function will convert the image to HSV color space
    HSV stands for Hue, Saturation, and Value
    this color space is useful for color detection and segmentation
    :param img: enter image
    :return: HSV image
    """
    return cv2.cvtColor(img, cv2.COLOR_BGR2HSV)


def yuv_color_space(img):
    """
    this function will convert the image to YUV color space
    YUV stands for Y (luminance), U (chrominance), and V (chrominance)
    this color space is useful for video processing and compression
    :param img: entry image
    :return: YUV image
    """
    return cv2.cvtColor(img, cv2.COLOR_BGR2YUV)


def gray_color_space(img):
    """
    this function will convert the image to gray scale
    the gray scale image is a single channel image.
    this color space is useful for image processing and segmentation
    :param img:
    :return: gray scale image
    """
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


def lab_color_space(img):
    """
    this function will convert the image to LAB color space
    LAB stands for Lightness, A (green-red), and B (blue-yellow)
    this color space is useful for color detection and segmentation
    :param img: entry image
    :return: LAB image
    """
    return cv2.cvtColor(img, cv2.COLOR_BGR2LAB)


def xyz_color_space(img):
    """
    this function will convert the image to XYZ color space
    XYZ stands for X (red), Y (green), and Z (blue)
    this color space is useful for color detection and segmentation
    :param img: entry image
    :return: XYZ image
    """
    return cv2.cvtColor(img, cv2.COLOR_BGR2XYZ)


def yCrCb_color_space(img):
    """
    this function will convert the image to YCrCb color space
    YCrCb stands for Y (luminance), Cr (red chrominance), and Cb (blue chrominance)
    this color space is useful for video processing and compression
    :param img: entry image
    :return: YCrCb image
    """
    return cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)


def hls_color_space(img):
    """
    this function will convert the image to HLS color space
    HLS stands for Hue, Lightness, and Saturation
    this color space is useful for color detection and segmentation
    :param img: entry image
    :return: HLS image
    """
    return cv2.cvtColor(img, cv2.COLOR_BGR2HLS)


def luv_color_space(img):
    """
    this function will convert the image to LUV color space
    LUV stands for Lightness, U (green-red chrominance), and V (blue-yellow chrominance)
    this color space is useful for color detection and segmentation
    :param img: entry image
    :return: LUV image
    """
    return cv2.cvtColor(img, cv2.COLOR_BGR2LUV)


def cie_lab_color_space(img):
    """
    this function will convert the image to CIE-LAB color space
    CIE-LAB stands for CIE-based L*a*b* color space
    this color space is useful for color detection and segmentation
    :param img: entry image
    :return: CIE-LAB image
    """
    return cv2.cvtColor(img, cv2.COLOR_BGR2Lab)


def cie_luv_color_space(img):
    """
    this function will convert the image to CIE-LUV color space
    CIE-LUV stands for CIE-based L*u*v* color space
    this color space is useful for color detection and segmentation
    :param img: entry image
    :return: CIE-LUV image
    """

    return cv2.cvtColor(img, cv2.COLOR_BGR2Luv)


image = cv2.imread('src/no_entry_test.jpg')
cv2.imshow('Original Image', image)

# converting the image to RGB color space
rgb_image = rgb_color_space(image)
cv2.imshow('RGB Image', rgb_image)
cv2.waitKey(0)
cv2.destroyWindow('RGB Image')

# converting the image to HSV color space
hsv_image = hsv_color_space(image)
cv2.imshow('HSV Image', hsv_image)
cv2.waitKey(0)
cv2.destroyWindow('HSV Image')

# converting the image to YUV color space
yuv_image = yuv_color_space(image)
cv2.imshow('YUV Image', yuv_image)
cv2.waitKey(0)
cv2.destroyWindow('YUV Image')

# converting the image to gray scale
gray_image = gray_color_space(image)
cv2.imshow('Gray Image', gray_image)
cv2.waitKey(0)
cv2.destroyWindow('Gray Image')

# converting the image to LAB color space
lab_image = lab_color_space(image)
cv2.imshow('LAB Image', lab_image)
cv2.waitKey(0)
cv2.destroyWindow('LAB Image')

# converting the image to XYZ color space
xyz_image = xyz_color_space(image)
cv2.imshow('XYZ Image', xyz_image)
cv2.waitKey(0)
cv2.destroyWindow('XYZ Image')

# converting the image to YCrCb color space
yCrCb_image = yCrCb_color_space(image)
cv2.imshow('YCrCb Image', yCrCb_image)
cv2.waitKey(0)
cv2.destroyWindow('YCrCb Image')

# converting the image to HLS color space
hls_image = hls_color_space(image)
cv2.imshow('HLS Image', hls_image)
cv2.waitKey(0)
cv2.destroyWindow('HLS Image')

# converting the image to LUV color space
luv_image = luv_color_space(image)
cv2.imshow('LUV Image', luv_image)
cv2.waitKey(0)
cv2.destroyWindow('LUV Image')

# converting the image to CIE-LAB color space
cie_lab_image = cie_lab_color_space(image)
cv2.imshow('CIE-LAB Image', cie_lab_image)
cv2.waitKey(0)
cv2.destroyWindow('CIE-LAB Image')

# converting the image to CIE-LUV color space
cie_luv_image = cie_luv_color_space(image)
cv2.imshow('CIE-LUV Image', cie_luv_image)
cv2.waitKey(0)
cv2.destroyWindow('CIE-LUV Image')
