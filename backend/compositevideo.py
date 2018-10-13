#!/usr/bin/env python3
import os
from renderer import Renderer

class CompositeVideo:
	def __init__(self, cwd = os.getcwd()):
		self.cwd = cwd
	def make_new_video(self):
		self.download_frames()
		# Do some error-checking of each image
		# Make sure there are right number of images
		self.render_video()
		pass
	def download_frames(self):
		# Download all frames as 1 ZIP file
		pass
	def render_video(self):
		
		renderer = Renderer(self.cwd)
		renderer.create_video()
