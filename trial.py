import os
import cv2
import dlib
import sys
# import dotenv
import use
import numpy as np

def faces(image_np):
    detector = dlib.get_frontal_face_detector()
    # path = "test_data/" + path
    # with open(path, 'rb') as fp:
    #     im_b = fp.read()
    # image_np = np.frombuffer(im_b, np.uint8)
    frame = cv2.imdecode(image_np, cv2.IMREAD_COLOR)
    cv2.imshow("frame", frame)
    cv2.waitkey(0)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = detector(gray)
    # detect the face
    for counter, face in enumerate(faces):
        x1, y1 = face.left(), face.top()
        x2, y2 = face.right(), face.bottom()
        cv2.rectangle(frame, (x1, y1), (x2, y2), (220, 255, 220), 1)
        img_to_save = frame[y1:y2, x1:x2]
        cv2.imwrite(f"faces/face{counter}.jpg", img_to_save)


def remove_dir(path):
    try:
        for i in os.listdir(path):
            os.remove(f"{path}/{i}")
        os.rmdir(path)
    except:
        pass


if __name__ == "__main__":
    # load_dotenv()
    # idx = 1
    # for i in os.listdir("test_data"):
    #     remove_dir(f"faces{idx}")
    #     os.mkdir(f"faces{idx}")
    #     faces(i, str(idx))
    # idx += 1

    image_name = "collage.jpg"
    # remove_dir("faces")
    os.mkdir("faces")
    faces(sys.argv[1])
    for i in os.listdir("faces"):
        bytes = open(f"faces/{i}", "rb").read()
        # use.get_label(bytes)
    # remove_dir("faces")