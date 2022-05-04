import imsearch.models as models
import imsearch.utils as utils

from skimage.io import imread
from skimage.transform import resize

import numpy as np

def imgload(file, model = models.rn18):
    x = imread(file)
    x = resize(x, (224, 224)) * 255
    x = models.preprocess_input(x)
    x = np.expand_dims(x, 0)
    return model.predict(x)

def imgscan(filelist, model = models.rn18):
    scanlist = list()
    for f in filelist:
        scanlist.append(imgload(f, model=model)[0])
    return scanlist

def closest(comp, scanlist):
    _lis = []
    for x, s in enumerate(scanlist):
        _ = np.linalg.norm(s-comp)
        _lis.append(_)
    return np.argsort(_lis)

def closestfilefromfile(compfile, filelist, model=models.rn18):
    _ = closest(imgload(compfile, model=model), imgscan(filelist, model=model))
    return [filelist[i] for i in _]

