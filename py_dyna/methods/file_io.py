
import os
import numpy as np
from datetime import datetime
from glob import glob

import re
'''
Really janky way of seperating methods into different folders by having the cfile object inherit these methods
If there is a better way tell me!

Only Use this with the cfile object!!
This contains all the methods to write to the cfile file.

'''

def OpenFile(dsplotName,cwd):
    path = os.path.join(cwd,dsplotName)
    return f'open d3plot "{path}"'

def set_info(author = None):
    return f'$# LS-PrePost command file created by {author if author else "University of Sydney"}\n$# Created on {datetime.today().strftime("%Y-%m-%d %H:%M:%S")}'


def screenshot(imgName,cwd = '',window = 'OGL1x', gamma = 1.24 ,invert = None):
    '''
    Screenshot the current window
    Inputs:

        imgName (str): image name with file extension (e.g. img.png) extension determines the image format
        cwd (str): current directory to save image default is same location as cfile execution
        window (str): window to which to screenshot. The Default OGL1x will screenshot the main window.
        gamma (float): set gamma value of the image
        invert (float) : set inversion amount of black and white. Default is none in which case no inversion and background color is current colour

    '''
    #Split file name into name and extension  
    filename ,file_ext = imgName.split('.')

    #Check for valid photo format
    valid_formats = {'png','jpeg','jpg','bmp','tiff'}
    if file_ext not in valid_formats:
        ValueError(f'Please use a supported file firmat: \n{valid_formats}')

    
    full_path = os.path.join(cwd,imgName)
    if invert is not None:
        return f'print {file_ext} "{full_path}" gamma {gamma} transparent invert {invert} enlisted "{window}"'
    else:
        return f'print {file_ext} "{full_path}" gamma {gamma} opaque enlisted "{window}"'
def movie(mov_name = 'py_movie',format = 'MP4/H264',resolution = (1980,1080),gamma = 1.0, FPS = 10.0, cwd = os.getcwd()):
    '''
    Writes out the cmd for a movie
    Inputs:

        formats (str): MP4/H264, JPEG , GIF, MOV/MPEG4 , WMV/WMV ,AVI/RLE, AVI/24BIT , AVI/MPEG2 , AVI/MPEG4 , MKV/H264 

        resolution (tuple(int,int)): (width,height) default is 1080p
        
        cwd (str): current working directory
        
        gamma (float): Only available for JPEG,GIF, AVI/RLE, AVI/24BIT

        FPS (float) : frames per second default = 10

    Output:

        string: movie {format} {resolution} {path} /{gamma}/ {FPS}

        e.g. movie MP4/H264 1848x910 \"C:\\Users\\ShyGuy\\Desktop\\HelloWorld\\movie_000\\" 10
    '''

    if format.lower() == 'mp4':
        format = 'MP4/H264'
    valid_formats = {'MP4/H264', 'JPEG','GIF','MOV/MPEG4','WMV/WMV','AVI/24BIT','AVI/MPEG2','AVI/MPEG4','MP4/H.264','MKV/H.264'}

    if format not in valid_formats:
        raise ValueError('Please choose a correct format. see movie.__doc__ for details')
    # else:
    #     ext = re.sub('/*','',format)

    if format not in {'JPEG','GIF', 'AVI/RLE', 'AVI/24BIT'}:
        gamma = ''

    file_name = f'{mov_name}'
    full_path = os.path.join(cwd,file_name)
    resolution = f'{resolution[0]}x{resolution[1]}'

    return f'movie {format} {resolution} "{full_path}" {gamma} {FPS}'

    
def comment(text):
    '''
    Add a comment to text file
    '''
    return f'$# {text}'