from tkinter import *
import os
import pygame
root = Tk()

root.title("Psycho Music Player")
root.geometry("300x300")
musics = os.listdir()
soundObj = None
currentMusicIndex = 0
volumeVar = DoubleVar()
volumeVar.set(100.0)

def pauseMusic():
	pygame.mixer.music.pause()
	pauseBtn.config(text="Resume", command=resumeMusic)

def resumeMusic():
	pygame.mixer.music.unpause()
	pauseBtn.config(text="Pause", command=pauseMusic)

def initialMusic():
	print("Initialization Done!")
	global soundObj
	global currentIndex
	pygame.init()
	soundObj =  pygame.mixer.music.load(musics[currentMusicIndex])

initialMusic()

def playMusic():
	pygame.mixer.music.play()


def changeVolume(event):
	pygame.mixer.music.set_volume(volume.get()/100)


title = Label(root, text="Music Player", font=("Calibri", 20, "bold"))
title.pack()

music = Label(root, text=musics[currentIndex])
music.pack()

playBtn = Button(root, text="Play", command=playMusic)
playBtn.pack()


pauseBtn = Button(root, text="Pause", command=pauseMusic)

pauseBtn.pack()


volume = Scale(
    root,
    from_=0,
    to=100,
    orient='horizontal',
    variable=volumeVar,
    command=changeVolume
)
volume.pack()

root.mainloop()