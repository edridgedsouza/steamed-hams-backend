#!/usr/bin/env python3
import os
import shutil
from os.path import join
import zipfile
from renderer import Renderer
from PIL import Image

class CompositeVideo:
	def __init__(self, cwd = os.getcwd()):
		self.cwd = cwd
		self.NUMFRAMES = 4076
		self.WIDTH = 320
		self.HEIGHT = 240

	def make_new_video(self):
		self.download_frames()
		valid = self.validate_frames()
		if valid:
			self.render_video()
		else:
			pass # FIX THIS!! ############ TODO
		
	def download_frames(self): ########### TODO
		# Download all frames as 1 ZIP file
		zip_dir = join(self.cwd, 'media')
		zip_path = join(zip_dir, 'frames.zip')
		output_path = join(zip_dir, 'modified_temp')
		if not os.path.exists(output_path):
			os.makedirs(output_path)

		with zipfile.ZipFile(zip_path, 'r') as z:
			z.extractall(output_path)

	def validate_frames(self):
		newFrameDir = join(cwd, 'media/modified_temp')
		newFrames = os.listdir(newFrameDir)
		if len(newFrames) != self.NUMFRAMES:
			return False
		for frame in newFrames:
			im = Image.open(join(newFrameDir frame))
			width, height = im.size
			if width != self.WIDTH or height != self.HEIGHT:
				return False

		# If right number and right dimensions, then pass the test
		shutil.rmtree(join(cwd, 'media/modified'))
		shutil.move(newFrameDir, 
			join(cwd, 'media/modified'))
		return True

	def render_video(self):
		renderer = Renderer(self.cwd)
		renderer.create_video()
