import cv2


# first way to read an image is using its path to read it from our disc
def read_image(image_path):
    # this function of opencv reads an image from disc and returns it as a numpy array
    # the numpy array is an image with three dimensions (height, width, channels)
    image = cv2.imread(image_path)

    # show the image using cv2.imshow() function
    cv2.imshow(winname="read by image path", mat=image)


# in this function we will read video frames using opencv capture object
def read_video(video_value):
    """
    This function reads video frames using opencv capture object
    :param video_value: video file path or webcam index
    :return: void
    """
    if type(video_value) == str:
        print("reading video from file")
    elif type(video_value) == int:
        print("reading video from webcam")
    else:
        print("Invalid video source")
        return

    # create a capture object
    capture = cv2.VideoCapture(video_value)
    while True:
        # read function returns a boolean value and the frame
        # the boolean value is True if the frame is read correctly, otherwise False
        ret, frame = capture.read()

        # if the user presses 'q' key, break the loop
        if cv2.waitKey(1) & 0xFF == ord('q'):

            # release the capture object and destroy all windows
            capture.release()

            # this function will destroy all windows created by cv2.imshow() function
            cv2.destroyAllWindows()
            break

        if ret:
            # show the frame using cv2.imshow() function
            cv2.imshow(winname="read by video", mat=frame)

        else:
            # if the frame is not read correctly, continue to the next iteration
            continue


# example usage

read_image(r"src/no_entry_test.jpg")

# this function will help us to wait until the user presses any key
cv2.waitKey(0)
cv2.destroyAllWindows()

read_video(r"src/drive.mp4")

read_video(0)
