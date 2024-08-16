import cv2


def find_contours(img):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    return contours


image = cv2.imread(r"src/no_entry_test.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
threshold, gray = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

contours = find_contours(gray)

cv2.drawContours(image, contours, -1, (0, 255, 0), 3)

for contour in contours:
    contour_area = cv2.contourArea(contour)
    if contour_area > 5000:
        print(contour_area)
        draw_contour = cv2.drawContours(image, [contour], -1, (0, 0, 255), -1)

cv2.imshow("Contours", image)
cv2.waitKey(0)
