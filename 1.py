import moviepy.editor

video = moviepy.editor.VideoFileClip('VID-20220703-WA0182.mp4')
audio = video.audio
audio.write_audiofile('VID-20220703-WA0182.mp3')