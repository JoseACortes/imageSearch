from skimage.io import imread
from skimage.io import imshow

import ffmpeg
import os

def cutvideo(videofile, foldername, faat = 1):
    try:
        os.mkdir('./data/'+foldername)
    except:
        pass
    probe = ffmpeg.probe(videofile)
    time = float(probe['streams'][0]['duration']) // 2
    width = probe['streams'][0]['width']
    parts = int(int(probe['streams'][0]['nb_frames'])/faat)
    intervals = time // parts
    intervals = int(intervals)
    interval_list = [(i * intervals, (i + 1) * intervals) for i in range(parts)]
    i = 0
    for item in interval_list:
        (
            ffmpeg
            .input(videofile, ss=item[1])
            .filter('scale', width, -1)
            .output('./data/'+foldername+'/Image' + str(i) + '.jpg', vframes=1)
            .run()
        )
        i += 1

import glob

def folderlist(foldername):
    return glob.glob("./data/"+foldername+"/*.jpg")