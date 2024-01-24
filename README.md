# Python - Download Youtube videos   

## libraries needed :
- import requests
- from pytube import YouTube : class to instantiate with your url (attribs : title, streams, ....)
- from tqdm import tqdm : to show download progress bar

## 2 methods :
- get_video_info(url) to get some infos : resolution, file_size
- download_video(url, resolution, file_size) to download the file by chunks of 1MB (1024*1024)

## use help on instance of class Youtube:
- instanciation : video = Youtube(url)
- help(video) to see class attribs and methods (streams, resolution, ...)
- help(video.streams) to get all methods like get_lowest_resolution() to get resolution, etc..
- use requests to get all the enable resolutions (720p, ..) and file size
