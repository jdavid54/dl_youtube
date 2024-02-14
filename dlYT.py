#https://pytube.io/en/latest/user/playlist.html
import requests
from pytube import YouTube, Playlist
from tqdm import tqdm
from time import sleep

# take reso title and video size
def get_video_info(url, display=True):
    video = YouTube(url)
    title = video.title
    #resolution = video.streams.get_lowest_resolution()
    resolution = video.streams.get_by_resolution('720p')
    
    #print(video.streams)
    response = requests.head(resolution.url)
    file_size = int(response.headers.get('content-length', 0))  # return 0 if key not found
    if file_size>0 and display:
        #print(response.headers)  # use help
        print(f"video name : {title}")
        print(f"reso : {resolution.resolution}")
        print(f"video size : {file_size / (1024 * 1024):.2f} MB")
    return title, resolution, file_size

def get_playlist_info(url):
    p = Playlist(url)
    for i,k in enumerate(p):
        print(i+1,k)
        try:
            title, resolution, file_size = get_video_info(k)                          
        except:
            pass

def save_playlist(url):
    p = Playlist(url)
    id = url.split('list=')[1]
    buffer = ''
    for i,k in enumerate(p):
        try:
            title, resolution, file_size = get_video_info(k,False)
            print(title)
            buffer += f'{title} ({file_size / (1024 * 1024):.2f} MB)\n'
        except:
            pass
    with open(f'{id}.txt','w',encoding='utf8',errors='ignore') as f:
        f.write(buffer)
    

#download with progress bar
def download_video(url, resolution, file_size):
    video = YouTube(url)
    stream = video.streams.get_by_resolution(resolution.resolution)
    
    print(f"starting download ({resolution.resolution})...")
    
    # progess bar
    progress_bar = tqdm(total=file_size, unit='B', unit_scale=True)
    def on_progress(chunk, file_handle, bytes_remaining):
        progress_bar.update(len(chunk))
    stream.on_progress = on_progress  # associate stream progress with tqdm progress bar
    
    chunk_size = 1024 * 1024
    num_chunks = file_size // chunk_size + 1
        
    for i in range(num_chunks):
        start_byte = i * chunk_size
        end_byte = min((i + 1) * chunk_size, file_size)
        bytes_range = f"bytes={start_byte}-{end_byte-1}"
        headers = {"Range": bytes_range}
        response = requests.get(stream.url, headers=headers, stream=True)
        
        #save chunk by chunk to file
        with open(f"{video.title[:20]}_{resolution.resolution}.mp4", "ab") as file:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    file.write(chunk)
                    on_progress(chunk, file, end_byte - start_byte)
        
        
    progress_bar.close()
    print("complete download")

def download_playlist(url):
    p = Playlist(url)
    print(p)
    for i,k in enumerate(p):
        print(i+1,k)
        try:
            title, resolution, file_size = get_video_info(k)
            print(file_size)
            #sleep(5)
            if file_size>0:
                print('Downloading...')
                download_video(k, resolution, file_size)                
        except:
            pass



#========DOWLOAD=========================================
def download(url):
    # url:str ="https://www.youtube.com/watch?v=l4SjSHlxXOQ"   # put link video here
    #url:str ="https://www.youtube.com/watch?v=WOEO1UuCRcc"
    #url:str = "https://www.youtube.com/watch?v=CDonLjhYj28"
    file_size=0
    while file_size==0:
        title, resolution, file_size = get_video_info(url)
        #print(resolution, file_size)

    print(f'Download Y/n ?')
    if input()=='n':return

    if file_size>0:
        download_video(url, resolution, file_size)

# help(video.streams)

# download 1 video
# download(url)


#===========PLAYLIST=====================================
url:str='https://www.youtube.com/playlist?list=PLy_OaHcu9ip98SNRy8qH4hXp4o76C5Y_6'
url = 'https://www.youtube.com/playlist?list=PLKVMH2x-Imghzdb42BruShPgjY4Ghj7nN'
# get list info   
#get_playlist_info(url)

# download playlist
#download_playlist(url)