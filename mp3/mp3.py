#! /usr/bin/env python3
import os
import eyed3
import time
from moviepy.editor import concatenate_audioclips, AudioFileClip

path_to_files = os.path.join(os.getcwd(),'ソロギターで弾く スタジオジブリ作品集')
mp3_files = os.listdir(path_to_files)

accu_time=0

clips =[]
with open("output.txt","w") as output:
  for f in mp3_files:
    file_path=os.path.join(path_to_files, f)
    #put and parse song to list
    clips.append(AudioFileClip(file_path))
    # get the timestamp
    duration = eyed3.load(file_path).info.time_secs
    accu_time +=duration
    print(time.strftime('%H:%M:%S', time.gmtime(accu_time)), f)
    output.write(time.strftime('%H:%M:%S', time.gmtime(accu_time)) +" "+f+"\n")

print(accu_time)

# combine songs and export it
final_clip = concatenate_audioclips(clips)
final_clip.write_audiofile("output.mp3")


