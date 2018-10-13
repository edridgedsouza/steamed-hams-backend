import os
import subprocess
from pytube import YouTube

class Downloader:
	def __init__(self):
		self.url = 'https://www.youtube.com/watch?v=Y4lnZr022M8'
		self.yt = YouTube(self.url)

		self.video = self.yt.streams.filter(adaptive=True).filter(mime_type='video/mp4').first()
		self.audio = self.yt.streams.filter(adaptive=True).filter(mime_type='audio/mp4').first()

	def download(self):
		if not os.path.exists('media'):
			os.makedirs('media')
		if not os.path.exists('media/video.mp4'):
			self.video.download('media', 'video')
		if not os.path.exists('media/audio.mp4'):
			self.audio.download('media', 'audio')

		self.video_to_frames()

	def video_to_frames(self):
		subprocess.call(['ffmpeg', '-i', 'media/video.mp4', 'media/frame%03d.png'])


if __name__ == '__main__':
	Downloader().download()