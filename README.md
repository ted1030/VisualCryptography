# VisualCryptography
Visual Cryptography with color/gray

usage:
```shell
python color.py/gray.py xxx.xxx
```
Overlap the two generated images would get the original image.

algorithm:
1. Read the input image in CMYK color space.
2. Split it to C, M, Y channels.
3. Generate halftone images.
4. For every channel, generate two secret images.
5. Combine three channels respectively.
6. Overlap the two images and get result.

references: https://www.sciencedirect.com/science/article/pii/S0031320302002583
