'''
Youtube Video Downloader
Author: Munna kumar
'''

#import the package
from pytube import YouTube

url ="Enter yout Url"
my_video = YouTube(url)

print("*****************Video Title***************")
#get video title
print(my_video.title)

print("***************Thumbnail image***************")
#get thumbnail image
print(my_video.thumbnail_url)

print("***************Download Video*************")
#get all the stream resolution for the 
for stream in my_video.streams:
    print(stream)

#set stream resolution
my_video = my_video.streams.get_highest_resolution()

#or
#my_video = my_video.streams.first()

#Download Video
my_video.download()
