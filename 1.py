import moviepy.editor
from pathlib import Path

video_file = Path('VID-20220703-WA0182.mp4')
video = moviepy.editor.VideoFileClip(f'{video_file}')
audio = video.audio
audio.write_audiofile(f'{video_file.stem}.stem.mp3')