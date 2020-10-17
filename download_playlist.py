import re
from pytube.exceptions import RegexMatchError,ExtractError,VideoUnavailable
from pytube import Playlist, YouTube

url = 'https://www.youtube.com/playlist?list=PLX2gX-ftPVXU3oUFNATxGXY90AULiqnWT'

playlist = Playlist(url)

# this fixes the empty playlist.videos list
playlist._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")

num_videos = len(playlist.video_urls)

print('Number of videos in playlist: %s' % num_videos)

for link in playlist.video_urls:
    try:
      ytube = YouTube(link)
      print(link, ytube.title)
      stream = ytube.streams[0]
      stream.download(output_path='./')
    except RegexMatchError:
      print('The Regex pattern did not return any matches for the video: {}'.format(link))
    
    except ExtractError:
      print ('An extraction error occurred for the video: {}'.format(link))
    
    except VideoUnavailable:
      print('The following video is unavailable: {}'.format(link))

    except KeyError:
      print('Key error: {}'.format(link))

print('Playlist has been sucessfully downloaded')

##if num_videos > 0:
##   playlist.download_all('./')
