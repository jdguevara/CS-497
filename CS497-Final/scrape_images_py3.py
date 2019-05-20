from imutils import paths
import pandas as pd
import requests
import cv2
import os
from os import listdir
from os.path import isfile, join
import os.path as osp
from tqdm import tqdm_notebook as tqdm
from google_images_download import google_images_download

img_folder = '.'

def build_arguments(word):
    args = {}
    args['keywords'] = word
    args['limit'] = 200
    args['format'] = 'png'
    #args['usage_rights'] = 'labeled-for-nocommercial-reuse'
    return args

response = google_images_download.googleimagesdownload()

# Get Images 
word = input("What images would you like to download?:  ")
type(word)
absolute_image_paths = response.download(build_arguments(word))
