import numpy as np


detectors = {
    'H': lambda img, x, y: abs(img[x, y-1] - img[x, y+1]),
    'V': lambda img, x, y: abs(img[x-1, y] - img[x+1, y])
}

def line_detector(img, orientation='H'):

    orientation = orientation.upper()
    filtered_img = np.zeros(img.shape)

    rows, cols = img.shape
    for x in range(1, rows-1, 1):
        for y in range(1, cols-1, 1):
            filtered_img[x, y] = detectors[orientation](img, x, y)
    
    return filtered_img
