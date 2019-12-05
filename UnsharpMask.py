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


image = cv.imread('test.jpg')
sharpened_image = unsharp_mask(image)
cv.imwrite('my-sharpened-image.png', sharpened_image)


image = cv.imread(cv.samples.findFile('my-sharpened-image.png'))
if image is None:
    print('Could not open or find the image: ', 'test.jpg')
    exit(0)
new_image = np.zeros(image.shape, image.dtype)

alpha = 3.0
beta = 33

new_img = cv.convertScaleAbs(image, alpha = alpha, beta = beta)
cv.imwrite('test_sharp&bright.jpg', new_img)
cv.waitKey()
