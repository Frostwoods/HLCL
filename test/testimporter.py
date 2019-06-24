# -*- coding: utf-8 -*-
# @Poroject Name: HLCL
# @File Name: testimporter.py
# @Author: Yang Zhao psy
# @Emial: frostwoods@foxmail.com
# @Date:   2019-06-09 14:22:13
# @Last Modified by:   Yang Zhao psy
# @Last Modified time: 2019-06-09 16:03:39
"""
Descripition:



Change Activity:



"""
import test_spline as ts
from skimage.morphology import skeletonize
from skimage import data
import matplotlib.pyplot as plt


# Invert the horse image
image = data.horse()
print image.shape
# perform skeletonization
skeleton = skeletonize(image)

# display results
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(8, 4),
                         sharex=True, sharey=True)

ax = axes.ravel()

ax[0].imshow(image, cmap=plt.cm.gray)
ax[0].axis('off')
ax[0].set_title('original', fontsize=20)

ax[1].imshow(skeleton, cmap=plt.cm.gray)
ax[1].axis('off')
ax[1].set_title('skeleton', fontsize=20)

fig.tight_layout()
plt.show()
