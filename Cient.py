from msilib.schema import ListBox
import socket
from threading import Thread
from tkinter import *
from tkinter import ttk
import ftplib
import os
import time
import ntpath #This is used to extract filename from path

from tkinter import filedialog
from pathlib import Path


from playsound import playsound
import pygame
from pygame import mixer

PORT = 8050
IP_ADDRESS = '127.0.0.1'
SERVER = None
BUFFER_SIZE = 4096

name = None
listbox = None
filePathLabel = None
global song_counter
song_counter = 0

for file in os.listdir("shared_files"):
    filename = os.fsdecode(file)
    listbox.insert(song_counter, filename)
    song_counter = song_counter + 1

def play():
    global song_selected
    song_selected = listbox.get(ANCHOR)
    
    pygame
    mixer.init()
    mixer.music.load("shared_files/" + song_selected)
    mixer.music.play()
    if(song_selected != ""):
        infolabel.configure(text = "Now Playing: " + song_selected)
    else:
        infolabel.configure(text = "")

def stop():
    global song_selected
    pygame
    mixer.init()
    mixer.music.load("shared_files/" + song_selected)
    mixer.music.pause()
    infolabel.configure(text = "")

def musicWindow():
    window = Tk()
    window.title("Music Window")
    window.geometry("300x300")
    window.configure(bg = "LightSkyBlue")
    
    selectlabel = Label(window, text = "Select Song", bg = "LightSkyBlue", font = ("Calibri", 8))
    selectlabel.place(x = 2, y = 1)
    
    listbox = ListBox(window, height = 10, width = 39, activestyle = "dotbox", bg = "LightSkyBlue", borderwitdh = 2, font = ("Calibri", 10))
    listbox.place(x = 10, y = 10)
    
    scrollbar1 = Scrollbar(listbox)
    scrollbar1.place(relheight = 1, relx = 1)
    scrollbar1.config(command = listbox.yview)
    
    playbutton = Button(window, text = "Play", width = 10, bd = 1, bg = "SkyBlue", font = ("Calibri", 10), command = play)
    playbutton.place(x = 30, y = 200)
    
    stop = Button(window, text = "Stop", bd = 1, width = 10, bg = "SkyBlue", font = ("Calibri", 10), command = stop)
    stop.place(x = 200, y = 200)
    
    upload = Button(window, text = "Upload", bd = 1, width = 10, bg = "SkyBlue", font = ("Calibri", 10))
    upload.place(x = 30, y = 250)
    
    download = Button(window, text = "Download", bd = 1, width = 10, bg = "SkyBlue", font = ("Calibri", 10))
    download.place(x = 200, y = 250)
    
    infolabel = Label(window, text = "", fg = "blue", font = ("Calibri", 8))
    infolabel.place(x = 4, y = 280)
    
    window.mainloop()

def setup():
    global SERVER
    global PORT
    global IP_ADDRESS
    
    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.bind((IP_ADDRESS, PORT))
    
    musicWindow()
    
setup()
