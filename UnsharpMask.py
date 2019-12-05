from __future__ import print_function
import cv2 as cv
import numpy as np


def unsharp_mask(image, kernel_size=(5, 5), sigma=1.0, amount=1.0, threshold=0):
    blurred = cv.GaussianBlur(image, kernel_size, sigma)
    sharpened = float(amount + 1) * image - float(amount) * blurred
    sharpened = np.maximum(sharpened, np.zeros(sharpened.shape))
    sharpened = np.minimum(sharpened, 255 * np.ones(sharpened.shape))
    sharpened = sharpened.round().astype(np.uint8)
    if threshold > 0:
        low_contrast_mask = np.absolute(image - blurred) < threshold
        np.copyto(sharpened, image, where=low_contrast_mask)
    return sharpened


image = cv.imread('test_image.jpg')
sharpened_image = unsharp_mask(image)
cv.imwrite('unsharpmask_test_image.jpg', sharpened_image)


img = cv.imread(cv.samples.findFile('unsharpmask_test_image.jpg'))
if img is None:
    print('Could not open or find the image: ', 'unsharpmask_test_image.jpg')
    exit(0)

contrast = 3.0
brightness = 33

new_img = cv.convertScaleAbs(img, alpha = contrast, beta = brightness)
cv.imwrite('unsharpmask_test_image.jpg', new_img)
cv.waitKey()
