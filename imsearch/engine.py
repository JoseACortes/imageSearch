from skimage.io import imread
from skimage.transform import resize

import numpy as np

class engine():

    def printDisplay(self, i):
        if i == 0:
            print('achivement unlocked: found something you didnt have to')
        elif i == 1:
            pass

    def runImage(self, img, model, resolution, preprocess = None):

        x = np.empty((2, 2))

        if type(img) == str:
            x = imread(img)
            x = resize(x, resolution) * 255

        elif type(img) == np.ndarray:
            x = img

        else:
            pass
        
        if preprocess is not None:
            x = preprocess(x)
        
        x = np.expand_dims(x, 0)

        return model.predict(x)[0]

    def indexImage(self, img, model, resolution, preprocess = None, index=None):

        if type(img) == str:
            self.index.append(img)

        elif type(img) == np.ndarray:
            if index == None:
                self.index.append('untitled_image_'+str(self.emptycount))
                self.emptycount += 1
            else:
                self.index.append(index)

        else:
            pass
        
        ran = self.runImage(img, model, resolution, preprocess)
        self.database.append(ran)

    def __init__(self, files, model, resolution, preprocess = False, scan_buffer = None, save = False, disp = False):
        
        self.emptycount = 0

        self.model = model
        self.database = list()
        self.index = list()

        for f in files:
            self.indexImage(f, model, resolution, preprocess)

    def search(self, item, distance_metric, model, resolution, preprocess = None, n=None):

        _lis = []

        item = self.runImage(img = item, model = model, resolution = resolution, preprocess = preprocess)

        for x in self.database:
            _ = distance_metric(x, item)
            _lis.append(_)
        
        sorted_list =  [self.index[i] for i in np.argsort(_lis)]

        if n == None:
            return sorted_list
        
        else:
            return sorted_list[:n]