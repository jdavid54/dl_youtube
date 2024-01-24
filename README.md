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

ex :

resolution = video.streams.get_by_resolution('720p')

resolution :

<Stream: itag="22" mime_type="video/mp4" res="720p" fps="30fps" vcodec="avc1.64001F" acodec="mp4a.40.2" progressive="True" type="video">

resolution.url :

'https://rr1---sn-n4g-jqbek.googlevideo.com/videoplayback?expire=1706152267&ei=63yxZd_7LNWCp-oPwviO2A4&ip=81.65.151.83&id=o-ADwgIXwmokatoL_l-UACLn6KXQ-yJnUMGZWbRLGYwBab&itag=22&source=youtube&requiressl=yes&xpc=EgVo2aDSNQ%3D%3D&mh=Tz&mm=31%2C26&mn=sn-n4g-jqbek%2Csn-h5q7knee&ms=au%2Conr&mv=m&mvi=1&pl=22&initcwndbps=1145000&vprv=1&mime=video%2Fmp4&cnr=14&ratebypass=yes&dur=341.054&lmt=1701035139490818&mt=1706130319&fvip=4&fexp=24007246&c=ANDROID_MUSIC&txp=5532434&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cxpc%2Cvprv%2Cmime%2Ccnr%2Cratebypass%2Cdur%2Clmt&sig=AJfQdSswRQIgJH3maejUQFGMzE2a3ukcNIJd34goJwQGjpVsT4jioO8CIQCz6j1v_SKjwzwC3EbqiYipV0Ys1erB8RTt3N1BgoFVLg%3D%3D&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AAO5W4owRQIgfv_SKtmKl4I7JPZjtbDXkn9o4FF9YDgVzhAr7iA7D98CIQDrOanPDS9jvQj0L87e_eFLTm3cVjNHLi_JwIUUodFGXg%3D%3D'

response = requests.head(resolution.url)

response.headers is a dictionary :

{'Last-Modified': 'Sun, 26 Nov 2023 21:45:39 GMT', 'Content-Type': 'video/mp4', 'Date': 'Wed, 24 Jan 2024 21:21:47 GMT', 'Expires': 'Wed, 24 Jan 2024 21:21:47 GMT', 'Cache-Control': 'private, max-age=20028', 'Accept-Ranges': 'bytes', 'Content-Length': '38787660', 'Connection': 'close', 'Alt-Svc': 'h3=":443"; ma=2592000,h3-29=":443"; ma=2592000,h3-Q046=":443"; ma=2592000,quic=":443"; ma=2592000; v="46"', 'Vary': 'Origin', 'Cross-Origin-Resource-Policy': 'cross-origin', 'X-Content-Type-Options': 'nosniff', 'Server': 'gvs 1.0'}

where you can get the file size with response.headers['Content-Length'] => '38787660'
