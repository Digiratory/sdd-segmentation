import numpy as np
import scipy
import matplotlib.pyplot as plt
from sdd_segmentation.sdd import sdd_threshold_selection
# Synthesizing the image
S = 30
C1 = 50+S*np.random.randn(128, 128)
Center1 = 100+S*np.random.randn(64, 64)
Center2 = 150+S*np.random.randn(64, 64)
C1[12:76, 12:76] = Center1
C1[52:116, 52:116] = Center2
C = C1
# plt.figure()
#plt.imshow(C, cmap='gray')
# plt.show()

IS = C1.shape
Seg1 = C1.astype(float)
S = Seg1.shape

Seg = scipy.ndimage.generic_filter(Seg1, np.mean, size=(3, 3), mode='nearest')

# plt.figure()
#plt.imshow(Seg, cmap='gray')
# plt.show()
#plt.hist(Seg.flatten(), bins=255, range=(0, 255), density=False)
# plt.show()

# Zhenzhou threshold selection method
T = sdd_threshold_selection(Seg.astype(float), 15)
bSeg = Seg1 > T[0]
plt.figure()
plt.imshow(bSeg, cmap='gray')
plt.show()
