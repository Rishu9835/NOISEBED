# for extracting audio from a video file using MoviePy
from moviepy.editor import VideoFileClip

video = VideoFileClip("input_video.mp4")
video.audio.write_audiofile("original_audio.wav")