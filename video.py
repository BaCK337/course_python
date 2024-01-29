from time import sleep
import cv2


percent = 100
# percent = 10 0


if __name__ == '__main__':
    cap = cv2.VideoCapture(0)
    # cap = cv2.VideoCapture('/home/dzmitry/Videos/vokoscreen-2023-05-04_12-01-10.mkv')
    # cap = cv2.VideoCapture('/home/dzmitry/Videos/vokoscreen-2023-11-26_19-07-06.mkv')

    while True:
        ret, frame = cap.read()
        frame = cv2.resize(
            frame,
            (
                int(frame.shape[1] * percent / 100),
                int(frame.shape[0] * percent / 100)
            )
        )
        frame = cv2.flip(frame, 1)
        cv2.imshow('Camera', frame)
        sleep(0.015)
        
        if cv2.waitKey(1) in (ord('q'), 202):
        # if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
    cap.release()
    cv2.destroyAllWindows()