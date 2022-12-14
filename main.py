from tkinter import *
import os
from mutagen.mp3 import MP3
import pygame
from tkinter import filedialog

root = Tk()

root.title("Psycho Music Player")
root.geometry("300x300")
listDir = os.listdir()

musics = []

for item in listDir:
	if ".mp3" in item or ".MP3" in item:
		print(item)
		musics.append(item)

print(musics)
soundObj = None
currentMusicIndex = 0
selectedFolder = "D:/Coding/Python/Music Player GUI"
volumeVar = DoubleVar()
volumeVar.set(100.0)


def updateMusicPlaylist():
	newMusic = os.listdir(selectedFolder)
	print(newMusic[0])
	global musics
	musics = []
	for music in newMusic:
		if ".mp3" in music or ".MP3" in music:
			musics.append(music)	
	print(musics[0])
	initialMusic()

def selectFolder():
	global selectedFolder
	selectedFolder = filedialog.askdirectory()
	print(selectedFolder)
	updateMusicPlaylist()

def pauseMusic():
	pygame.mixer.music.pause()
	pauseBtn.config(text="Resume", command=resumeMusic)

def resumeMusic():
	pygame.mixer.music.unpause()
	pauseBtn.config(text="Pause", command=pauseMusic)

def initialMusic():
	print("Initialization Done!")
	global soundObj
	global musicName
	global currentMusicIndex
	pygame.init()
	if selectedFolder:	
		soundObj =  pygame.mixer.music.load(f"{selectedFolder}/{musics[currentMusicIndex]}")
	else:
		soundObj =  pygame.mixer.music.load(f"{musics[currentMusicIndex]}")
	
	musicName.config(text=musics[currentMusicIndex])



def playMusic():
	pygame.mixer.music.play()

def previousTrack():
	global currentMusicIndex
	if currentMusicIndex == 0:
		currentMusicIndex = len(musics) - 1
	else:
		currentMusicIndex -= 1
	initialMusic()
	playMusic()
	musicName.config(text=musics[currentMusicIndex])


def nextTrack():
	global currentMusicIndex
	if (len(musics)-1) == currentMusicIndex:
		currentMusicIndex = 0
	else:
		currentMusicIndex += 1
	initialMusic()
	playMusic()
	musicName.config(text=musics[currentMusicIndex])

def changeVolume(event):
	pygame.mixer.music.set_volume(volume.get()/100)


title = Label(root, text="Music Player", font=("Calibri", 20, "bold"))
title.pack()

musicName = Label(root, text=musics[currentMusicIndex])
musicName.pack()


playBtn = Button(root, text="Play", command=playMusic)
playBtn.pack()


pauseBtn = Button(root, text="Pause", command=pauseMusic)

pauseBtn.pack()


prevTrackBtn = Button(root, text="Previous Track", command=previousTrack)
prevTrackBtn.pack()


nextTrackBtn = Button(root, text="Next Track", command=nextTrack)
nextTrackBtn.pack()

volume = Scale(
    root,
    from_=0,
    to=100,
    orient='horizontal',
    variable=volumeVar,
    command=changeVolume
)
volume.pack()


mainMenu = Menu()

fileMenu = Menu(mainMenu, tearoff=0)
fileMenu.add_command(label="Open a Folder", command=selectFolder)

mainMenu.add_cascade(label="File", menu=fileMenu)
root.config(menu=mainMenu)

initialMusic()
root.mainloop()