import cv2
from djitellopy import Tello

#Tello class 객체를 생성합니다. 
tello = Tello()

#tello 클래스의 적절한 메소드들을 사용하여 드론과 연결합니다.
#############################
#                           #
#                           #
#############################

#drone은 frame 단위로 정보를 가지고 있으니 loop문으로 데이터를 처리 
while(True):
    #tello 클래스의 적절한 메소드를 활용하여 frame으로 데이터를 처리
    #Hinst, 6주차 TelloTV.py에서 frameRet 변수
    ############################# 
    #                           #
    #                           #
    #############################

    ##opencv라이브러리를 활용하는경우
    #cv2의 적절한 메소드 활용
    ############################# 
    #                           #
    #                           #
    #############################


    #cv2의 imshow메소드를 활용하여 화면에 drone 카메라로 인식된 화면 띄우기
    ############################# 
    #                           #
    #############################

#드론 연결종료
tello.end()
#화면 끄기
cv2.destroyAllWindows()

