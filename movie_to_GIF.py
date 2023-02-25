from moviepy.editor import VideoFileClip

clip = VideoFileClip("example.mp4")
clip.write_gif("use_your_head.gif")