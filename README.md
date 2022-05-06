![](extra/UTA-DataScience-Logo.png)
# imageSearch Image Search Engine

This project uses ML models and feature extraction to make an engine for ranking image similarity. The engine is then used to find the closest frames of a video to a given searched image.

## Overview
* **The Task:** Make an engine that takes a video and a search image and returns similar frames.
* **The Approach:** Take a categorization ML model (resNet18), cut the model for feature extraction, then write a program

## Summary of Work Done
### Data  
* **Example Video** (F1 Race Highlights):
	*  Type: .mp4 video
	*   Input: 6:51, 144p, 25 fps 
    *  Size: 9.9 MB
    *  youtube.com/watch?v=vL0yww9nk9o&t=140s

* **Example Image 1** (car):
	*  Type: .jpg image
	*  Input: 2000 x 1000
    *  Size: 179 kb

* **Example Image 2** (bike):
	*  Type: .jpg image
	*   Input: 1200 x 738
    *  Size: 117 kb

### Process
1. use a function in package to extract frames of a video and save it in a folder
2. each file is resized into 224x224 and using a function is run through a Tensorflow model outputting an array  
3. The searched image is also run through a Tensorflow model outputting an array
4. The array of the searched image is then compared to the arrays of the video frames
5. The file names of the closest frames are then returned in a list

### Future Work
* Expand the number of models in package
* Use different methods to rank similarity
* Comparison study for different models used for search engine

## How to reproduce results
To reproduce results, follow main.ipynb
or
To use package:
> import main as ims
* **BYOD (bring your own data)**
	* Use included utility to extract video frames into a folder
		> ims.utils.cutvideo(video, folder, faat=1)
		
		* video: file location of video
		* folder: folder name for storing images
		* faat: extract every nth frame from the video
	* Use folder containing pre-gathered or non-video frames
		> ims.closestfilefromfile(image, folder)
		
		* image: searched image
		* folder: search base folder to compare to image
* **BYOM (bring your own model)**
	* Replace default model with other
	> ims.closestfilefromfile(image, folder, model)
	
	* image: searched image
	* folder: search base folder to compare to image
	* model: tensorflow model that can predict an array

### Overview of files in repository

* main.py: main python file for package
* main.ipynb: example of package use
* imsearch: folder for rest of python package
* exampleimages: images used for the main.ipynb example
* data: Default location where videos are processed into images


### Software Setup

* main.py
	* scikit-image
	* numpy
* models.py
	* tensorflow
* utils.py
	* scikit-image
	* ffmpeg
	* os
	* glob
