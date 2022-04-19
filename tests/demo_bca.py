'''
Additional requirements:

pip install -U bio-cntrs-analyzer
'''
import cv2
from glob import glob
import matplotlib.pyplot as plt

from bcanalyzer.image_processing.image_processor import process_image
from bcanalyzer.common.io import im_load, im_save

from sdd_segmentation.sdd import sdd_threshold_selection

MCF7_IMAGES = "tests/MCF-7 cell populations Dataset/images/*.png"
MCF7_MASKS = "tests/MCF-7 cell populations Dataset/masks/*.png"

src_files = glob(MCF7_IMAGES)

params = {}
params['thre'] = 50
params['thre_abs'] = None
params['use_abs_threshhold'] = False
params['is_single_object'] = False
params['do_bg_removing'] = False
params['do_otsu_thresholding'] = False
params['win_size'] = 25
params['channel_r'] = True
params['channel_g'] = True
params['channel_b'] = True


def analyze_image(im_path, plot=False):
    image_np = im_load(im_path)
    if plot:
        plt.figure()
        plt.imshow(cv2.cvtColor(image_np, cv2.COLOR_BGR2RGB))

    preview, img_thresh, res_meta = process_image(im_path, params)

    if plot:
        pass
        # plt.imshow(img_thresh, cmap='hot', alpha=0.3)
        # plt.colorbar()

    T = sdd_threshold_selection(img_thresh.astype(float), 15)

    bSeg = img_thresh > T[-1]
    if plot:

        plt.imshow(bSeg, alpha=0.3)
        plt.axis('off')
        plt.show()


analyze_image(src_files[-1], plot=True)
