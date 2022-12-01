import numpy
import cv2

def get_img_from_bytes():
    image_np = np.frombuffer(im_b, np.uint8)
    img_np = cv2.imdecode(image_np, cv2.IMREAD_COLOR)  

    im_cv = cv2.imread(im_path)

    print('Same image: {}'.format(np.all(im_cv == img_np)))
