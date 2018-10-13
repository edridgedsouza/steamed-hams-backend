#!/usr/bin/env python3

import subprocess
import os

class Renderer:
	def __init__(self, cwd=os.getcwd()):
		self.cwd = cwd

	def create_video(self):
		yes = subprocess.Popen(['yes'], stdout=subprocess.PIPE, cwd = self.cwd)
		output = subprocess.Popen(['ffmpeg', '-framerate', '25', 
			'-i', 'media/original/frame%04d.png', 
			'-i', 'media/audio.mp4', 
			'-strict', '-2', 'media/output.mp4'], 
			stdin=yes.stdout, cwd=self.cwd)