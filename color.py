import sys
import numpy as np
from PIL import Image
from numba import jit

# 分離CMY channels
I = np.array(Image.open(sys.argv[1]).convert('CMYK')).astype(float)
I = [I[::, ::, i] for i in range(3)]

# halftone
@jit(cache=True, fastmath=True)
def halftone(I):
    for i in range(2, len(I) - 2):
        for j in range(2, len(I[0]) - 2):
            e = I[i][j] if I[i][j] < 128 else I[i][j] - 255
            I[i][j] = 0 if I[i][j] < 128 else 255
            I[i:i+3, j-2:j+3] += np.array([[0, 0, 0, 7, 5], [3, 5, 7, 5, 3], [1, 3, 5, 3, 1]]) / 48 * e
    return I[2:-2, 2:-2]
I = [halftone(np.pad(x, 2)) for x in I]

# 分別把CMY切成兩張圖
S = [[np.zeros(2 * np.array(I[0].shape)) for _ in range(4)] for _ in range(2)]
P = [np.array([[1, 0], [0, 1]]), np.array([[0, 1], [1, 0]])]
for n in range(3):
    for i in range(I[0].shape[0]):
        for j in range(I[0].shape[1]):
            p = np.random.randint(2)
            if I[n][i][j] == 255:
                S[p][n][i*2:i*2+2, j*2:j*2+2] = P[0]
                S[1-p][n][i*2:i*2+2, j*2:j*2+2] = P[1]
            else:
                S[p][n][i*2:i*2+2, j*2:j*2+2] = P[p]
                S[1-p][n][i*2:i*2+2, j*2:j*2+2] = P[p]

#把C1,M1,Y1合成S[0]，S[1]同理，並輸出模擬疊合圖
for i in range(2):
    S[i] = np.stack(S[i], -1).astype(np.uint8) * 255
    Image.fromarray(S[i], 'CMYK').save(f'share{i+1}.jpg')
    
Image.fromarray(S[0] + S[1], 'CMYK').save('result.jpg')
