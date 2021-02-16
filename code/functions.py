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
    return composite(scene, [4, 3, 2], in_range=in_range)


def composite(scene, bands, in_range="image"):
    """
    Create a composite for plotting with matplotlib.
    """
    nrows, ncols = scene[bands[0]].shape
    truecolor = np.empty((nrows, ncols, 3), dtype="uint8")    
    for i, band in enumerate(bands):
        truecolor[:, :, i] = skimage.exposure.rescale_intensity(scene[band], in_range=in_range, out_range="uint8")
    return truecolor


def crop_scene(scene, region=None):
    """
    Crop all bands in a scene to the given pixel interval.
    """
    if region is None:
        return scene
    w, e, s, n = region
    cropped = dict()
    for band in scene:
        if band == "metadata":
            cropped[band] = scene[band]
        else:
            cropped[band] = scene[band][s:n, w:e]
    return cropped


def load_scene(folder, pattern):
    """
    Read the images from a folder and returm them in a dictionary.
    """
    scene = dict()
    folder = Path(folder)
    files = list(folder.glob(f"*_B{pattern}.TIF"))
    assert files
    for fname in files:
        band = int(str(fname)[:-4].split("_")[-1][1:])
        scene[band] = skimage.io.imread(fname)
    mtl_files = list(folder.glob("*_MTL.txt"))
    assert len(mtl_files) == 1
    with open(mtl_files[0]) as f:
        scene["metadata"] = f.readlines()
    return scene


def save_scene(scene, destination, prefix=""):
    """
    Save all bands of a scene to the destination in TIF format.
    The file names are "{prefix}B{band}.TIF".
    """
    destination = Path(destination)
    destination.mkdir(exist_ok=True, parents=True)
    for band in scene:
        if band == "metadata":
            with open(destination / f"{prefix}MTL.txt", "w") as f:
                f.writelines(scene[band])            
        else:
            fname = destination / f"{prefix}B{band}.TIF"
            skimage.io.imsave(fname, scene[band])