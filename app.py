import youtube_dl
import pytube

def get_mp3(path):
    video_info = youtube_dl.YoutubeDL().extract_info(
        url = path, download = False
    )
    options = {
        'format' : 'bestaudio/best',
        'keepvideo' : False,
        'outtmpl' : f"D:/music/{video_info['title']}.mp3", 
        'abort-on-error' : False,
    }
    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download([video_info['webpage_url']])


url = input("Youtube playlist link: ")
videos = pytube.contrib.playlist.Playlist(url).video_urls

for video_url in videos:
    get_mp3(video_url)