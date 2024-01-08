from moviepy.editor import VideoFileClip, vfx
import os

for gifs in os.listdir(os.getcwd()):
	clip = VideoFileClip(gifs)
	reversed_clip = clip.fx(vfx.mirror_x)
	reversed_clip.write_gif(gifs)