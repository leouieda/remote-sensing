"""
Utility functions used in different notebooks.
"""
from pathlib import Path
import skimage.io
import skimage.exposure
import numpy as np
import matplotlib.pyplot as plt


def rgb_composite(scene, in_range="image"):
    """
    Create an RGB composite for plotting with matplotlib.
    """
    nrows, ncols = scene[2].shape
    truecolor = np.empty((nrows, ncols, 3), dtype="uint8")    
    for i, band in enumerate([4, 3, 2]):
        truecolor[:, :, i] = skimage.exposure.rescale_intensity(scene[band], in_range=in_range, out_range="uint8")
    return truecolor


def load_scene(folder, pattern):
    """
    Read the images from a folder and returm them in a dictionary.
    """
    files = list(Path(folder).glob(f"*_B{pattern}.TIF"))
    assert files
    scene = dict()
    for fname in files:
        band = int(str(fname)[:-4].split("_")[-1][1:])
        scene[band] = skimage.io.imread(fname)
    return scene


def crop_scene(scene, region=None):
    """
    Crop all bands in a scene to the given pixel interval.
    """
    if region is None:
        return scene
    w, e, s, n = region
    cropped = dict()
    for band in scene:
        cropped[band] = scene[band][s:n, w:e]
    return cropped


def save_scene(scene, destination, prefix=""):
    """
    Save all bands of a scene to the destination in TIF format.
    The file names are "{prefix}B{band}.TIF".
    """
    destination = Path(destination)
    destination.mkdir(exist_ok=True, parents=True)
    for band in scene:
        fname = destination / f"{prefix}B{band}.TIF"
        skimage.io.imsave(fname, scene[band])