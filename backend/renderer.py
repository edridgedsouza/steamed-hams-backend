#!/usr/bin/env python3

import subprocess
import os
from os.path import join

class Renderer:
	def __init__(self, cwd=os.getcwd()):
		self.cwd = cwd

	def create_video(self):
		yes = subprocess.Popen(['yes'], stdout=subprocess.PIPE, cwd = self.cwd)
		output = subprocess.Popen(['ffmpeg', '-framerate', '25', 
			'-i', 'media/modified/frame%04d.png', 
			'-i', 'media/audio.mp4', 
			'-strict', '-2', 'media/output_tmp.mp4'], 
			stdin=yes.stdout, cwd=self.cwd)

		streamdata = output.communicate()[0]
		if output.returncode == 0:
			os.rename(join(self.cwd, 'media/output_tmp.mp4'), join(self.cwd, 'media/output.mp4'))
			return True
		else:
			return False