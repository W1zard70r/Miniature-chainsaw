from moviepy.editor import *

clips_1 = ImageClip('imafges.jpg').set_duration(2)
clips_2 = ImageClip('kreking.jpg').set_duration(2)
clips_3 = ImageClip('pudge.jpeg').set_duration(2)
clips_4 = ImageClip('saew.jpg').set_duration(2)
final_clip = concatenate_videoclips([clips_1,clips_2,clips_3,clips_4], method = 'compose')
final_clip.write_videofile('test.mp4', fps = 24)