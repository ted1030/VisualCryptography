# VisualCryptography
Visual Cryptography with color/gray

usage:
```shell
python color.py/gray.py xxx.xxx
```
Overlap the two generated images would get the secret image.

algorithm:
1. read the input image in CMYK color space.
2. spilit it to C, M, Y channels.
3. generate halftone images.
4. for every channel, generate two secret images.
5. combine three channels respectively.
6. overlap the two images and get result.

references: https://www.sciencedirect.com/science/article/pii/S0031320302002583
