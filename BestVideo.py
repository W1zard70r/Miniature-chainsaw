from PIL import Image, ImageDraw, ImageFont
from moviepy.editor import *
import random
from random import randint
import os
def f(b):
    s=randint(40,60)
    x=randint(50,950)
    y=randint(50,950)
    colors=['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    J=random.choice(colors)
    V=random.choice(colors)
    R=random.choice(colors)
    G=random.choice(colors)
    im = Image.new('RGB',(1000,1000), color=(f'#{R}A{J}FAA'))
    draw_text= ImageDraw.Draw(im)
    font = ImageFont.truetype("arial.ttf", s)
    draw_text.text((x,y), f'{str(int(b))}',font=font, fill=(f'#{G}{V}06{J}6'))
    im.save(f'C:/Users/student/Documents/i122b/Sanya/{b}.png')

t=["0","01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20"]
for i in t:
    f(i)
directory = 'C:/Users/student/Documents/i122b/Sanya'
files = os.listdir(directory)
imges = list(filter(lambda x: x.endswith('.png'), files))
clips = [ImageClip(m).set_duration(2) for m in imges]
final_clip= concatenate_videoclips(clips, method='compose')
final_clip.write_videofile('NICEEE.mp4',fps=24)