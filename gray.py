import sys
import cv2
import numpy as np

I = cv2.imread(sys.argv[1], cv2.IMREAD_GRAYSCALE).astype(float)
def halftone(I):
    for i in range(2, len(I) - 2):
        for j in range(2, len(I[0]) - 2):
            e = I[i][j] if I[i][j] < 128 else I[i][j] - 255
            I[i][j] = 0 if I[i][j] < 128 else 255
            I[i:i+3, j-2:j+3] += np.array([[0, 0, 0, 7, 5], [3, 5, 7, 5, 3], [1, 3, 5, 3, 1]]) / 48 * e
    return I[2:-2, 2:-2]
I = halftone(np.pad(I, 2))

O = [np.empty([i * 2 for i in I.shape]) for _ in range(2)]
P = [np.array([[1, 0], [0, 1]]), np.array([[0, 1], [1, 0]])]
for i in range(0, len(I), 2):
    for j in range(0, len(I[0]), 2):
        p = np.random.randint(2)
        if I[i][j] == 0:
            O[p][i*2:i*2+2, j*2:j*2+2] = P[0]
            O[1-p][i*2:i*2+2, j*2:j*2+2] = P[1]
        else:
            O[p][i*2:i*2+2, j*2:j*2+2] = P[p]
            O[1-p][i*2:i*2+2, j*2:j*2+2] = P[p]

cv2.imwrite('out1.jpg', O[0].astype(np.uint8) * 255)
cv2.imwrite('out2.jpg', O[1].astype(np.uint8) * 255)
