
import requests
from pytube import YouTube
from tqdm import tqdm

# take reso title and video size
def get_video_info(url):
    video = YouTube(url)
    title = video.title
    #resolution = video.streams.get_lowest_resolution()
    resolution = video.streams.get_by_resolution('720p')
    
    #print(video.streams)
    response = requests.head(resolution.url)
    file_size = int(response.headers.get('content-length', 0))  # return 0 if key not found
    #print(response.headers)  # use help
    print(f"video name : {title}")
    print(f"reso : {resolution.resolution}")
    print(f"video size : {file_size / (1024 * 1024):.2f} MB")
    return video, resolution, file_size

def on_progress(chunk, file_handle, bytes_remaining):
        progress_bar.update(len(chunk))

#download with progress bar
def download_video(url, resolution, file_size):
    video = YouTube(url)
    stream = video.streams.get_by_resolution(resolution.resolution)
    
    print(f"starting download ({resolution.resolution})...")
    
    progress_bar = tqdm(total=file_size, unit='B', unit_scale=True)
    def on_progress(chunk, file_handle, bytes_remaining):
        progress_bar.update(len(chunk))
    stream.on_progress = on_progress
    
    chunk_size = 1024 * 1024
    num_chunks = file_size // chunk_size + 1
        
    for i in range(num_chunks):
        start_byte = i * chunk_size
        end_byte = min((i + 1) * chunk_size, file_size)
        bytes_range = f"bytes={start_byte}-{end_byte-1}"
        headers = {"Range": bytes_range}
        response = requests.get(stream.url, headers=headers, stream=True)
        
        with open(f"{video.title[:20]}_{resolution.resolution}.mp4", "ab") as file:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    file.write(chunk)
                    on_progress(chunk, file, end_byte - start_byte)
        
        
    progress_bar.close()
    print("complete download")

# url:str ="https://www.youtube.com/watch?v=l4SjSHlxXOQ"   # put link video here

url:str ="https://www.youtube.com/watch?v=VonkoVZxHn4"
video, resolution, file_size = get_video_info(url)
#print(video, resolution, file_size)

print('Download ?')
input()
if file_size!=0:
    download_video(url, resolution, file_size)

# help(video.streams)