import cv2

# 웹캠영상을 비디오로 띄우기
cam = cv2.VideoCapture(0)

while True:
    #동영상이 끝났을 때 ret = false가 됨
    ret, img = cam.read()

    if ret == False:
        break;
    
    # 사이즈 변경
    img = cv2.resize(img, dsize=(640,380))
    # 이미지 보여주기
    cv2.imshow('result',img)

        #100ms 기다렸다 다음 프레임 읽어오기
    if cv2.waitKey(100) == ord('q'):
        break;