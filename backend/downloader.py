#!/usr/bin/env python3

import os
from os.path import join
import subprocess
from pytube import YouTube

class Downloader:
	def __init__(self, cwd=os.getcwd()):
		self.cwd = cwd
		self.url = 'https://www.youtube.com/watch?v=Y4lnZr022M8'
		self.yt = YouTube(self.url)

		self.video = self.yt.streams.filter(adaptive=True).filter(mime_type='video/mp4').first()
		self.audio = self.yt.streams.filter(adaptive=True).filter(mime_type='audio/mp4').first()

	def download(self):
		if not os.path.exists(join(self.cwd,'media')):
			os.makedirs(join(self.cwd, 'media'))
		if not os.path.exists(join(self.cwd,'media/video.mp4')):
			print('Downloading video')
			self.video.download(join(self.cwd,'media'), 'video')
		if not os.path.exists('media/audio.mp4'):
			print('Downloading audio')
			self.audio.download(join(self.cwd,'media'), 'audio')

		self.video_to_frames()

	def video_to_frames(self):
		print('Video to frames')
		if not os.path.exists(join(self.cwd,'media/original')):
			os.makedirs(join(self.cwd,'media/original'))
		subprocess.call(['ffmpeg', '-i', 'media/video.mp4', 'media/original/frame%04d.png'], 
			cwd = self.cwd)


if __name__ == '__main__':
	Downloader().download()