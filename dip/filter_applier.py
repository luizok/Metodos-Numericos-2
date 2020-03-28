import cv2 as cv
import numpy as np
from filters import line_detector


def read_image(img_path, target_size=(400, 300)):

    img = cv.imread(img_path)
    img = cv.resize(img, target_size)
    img = np.sum(img, axis=2) / 3
    img = img / 255.

    rows, cols = img.shape
    expanded_img = np.zeros((rows + 2, cols + 2))
    expanded_img[1:-1, 1:-1] = img

    return expanded_img


if __name__ == '__main__':

    img_paths = ['test_1.jpg', 'test_2.webp', 'test_3.jpeg']
    
    full_row = []
    for img_p in img_paths:
        img = read_image(img_p, (250, 200))
        v_img = line_detector(img, 'v')
        h_img = line_detector(img, 'h')

        full_row.append(np.hstack([img, v_img, h_img, v_img+h_img]))

    cv.imshow('Original / V-Lines / H-Lines / Both', np.vstack(full_row))
    k = cv.waitKey(0)