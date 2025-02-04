import cv2
from cvzone.PoseModule import PoseDetector

# you can also replace 'video.mp4' with the number 0 (or any other number based on which webcam are you using) to have your movement recorded realtime
cap = cv2.VideoCapture(0)

detector = PoseDetector()
position_list = []

while True:
    success, img = cap.read()
    # img = cv2.flip(img, 1)
    img = detector.findPose(img)
    landmark_list, bounding_box_info = detector.findPosition(img)

    if bounding_box_info:
        landmark_string = ''
        for landmark in landmark_list:
            landmark_string += f'{landmark[1]},{img.shape[0] - landmark[2]},{landmark[3]},'
        position_list.append(landmark_string)

    # print(position_list)

    cv2.imshow("Image", img)
    key = cv2.waitKey(1)
    if key == ord('s'):
        with open("AnimationFile.txt", "w") as f:
            f.writelines(["%s\n" % item for item in position_list])
            break
