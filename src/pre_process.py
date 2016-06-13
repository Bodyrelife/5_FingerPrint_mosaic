#coding=utf-8

import os
import sys
import glob

import Image
import numpy as np

database = '.\database'

def loadimage(pic_folder):
	pics = os.listdir(pic_folder)
	image = []
	for pic in pics:
		if os.path.splitext(pic)[1] == '.bmp':
			image.append(Image.open(os.path.join(pic_folder, pic)))
			image[-1].show()
			os.system('pause')
	print "->", pics

def main():
	pic_folders = os.listdir(database)
	for pic_folder in pic_folders:
		print os.path.join(database, pic_folder)
		loadimage(os.path.join(database, pic_folder))

if __name__ == "__main__":
	main()