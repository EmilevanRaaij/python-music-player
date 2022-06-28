import tkinter
from tkinter import ttk
from ttkthemes import ThemedTk
from mutagen.mp3 import MP3
import os
from time import sleep
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame

root = ThemedTk(theme="equilux")
root.title("Music Player")
root.config(bg= "#464646")
pygame.init()

os.chdir("C:\\Users\\emile\\Desktop\\python programs\\music_player\\songs")

in_main = True
Playing = False

fromm = 0

def check_event():
    for event in pygame.event.get():
        if event.type == MUSIC_END:
            nextsong()

    root.after(102, check_event)

MUSIC_END = pygame.USEREVENT+1
pygame.mixer.music.set_endevent(MUSIC_END)

songlist = []

playlists = []

p0 = []
p1 = []
p2 = []
p3 = []
p4 = []
p5 = []
p6 = []
p7 = []
p8 = []
p9 = []
p10 = []
p11 = []
p12 = []

current_song = ""
current_song_idx = 0

lval = 0

clicking = False

def pbarrelease(event):
    global clicking
    global fromm
    pygame.mixer.music.rewind()
    pygame.mixer.music.set_pos(w_pbar.get())
    fromm = w_pbar.get()
    clicking = False

def pbarclick(event):
    global clicking
    clicking = True

w_pbar = ttk.Scale(root, from_= 0, to= 100, length= 300)

songlabeltext = tkinter.StringVar()
songlabeltext.set("")

def play():
    global w_pbar
    global current_song
    global fromm
    global songlabeltext
    global Playing
    pygame.mixer.music.play()
    songlabeltext.set(os.path.splitext(current_song)[0])
    audio = MP3(current_song)
    fromm = 0
    w_pbar.config(to= int(audio.info.length))
    w_pbar.set(0)
    updatepbar()
    Playing = True

def updatepbar():
    global w_pbar
    global Playing
    global clicking
    global fromm
    if Playing == True and clicking == False:
        w_pbar.set(((pygame.mixer.music.get_pos()) / 1000) + fromm)
    root.after(100, updatepbar)

def songlistclick(event):
    global current_song
    global Playing
    global current_song_idx
    clicked_song = songlist[int(str(w_songlist.curselection()).strip("(,)"))]
    clicked_song_idx = int(str(w_songlist.curselection()).strip("(,)"))
    if clicked_song == current_song:
        if Playing == False:
            play()
            Playing = True
        else:
            pass
    else:
        current_song = clicked_song
        current_song_idx = clicked_song_idx
        pygame.mixer.music.load(current_song)
        play()
        Playing = True

def playlistlistclick(event):
    global songlist
    global w_songlist
    global in_main
    clicked_list = playlists[int((str(w_playlistlist.curselection()).strip("(,)")))]
    if clicked_list == playlists[0]:
        songlist = p0
    elif clicked_list == playlists[1]:
        songlist = p1
    elif clicked_list == playlists[2]:
        songlist = p2
    elif clicked_list == playlists[3]:
        songlist = p3
    elif clicked_list == playlists[4]:
        songlist = p4
    elif clicked_list == playlists[5]:
        songlist = p5
    elif clicked_list == playlists[6]:
        songlist = p6
    elif clicked_list == playlists[7]:
        songlist = p7
    elif clicked_list == playlists[8]:
        songlist = p8
    elif clicked_list == playlists[9]:
        songlist = p9
    elif clicked_list == playlists[10]:
        songlist = p10
    elif clicked_list == playlists[11]:
        songlist = p11
    elif clicked_list == playlists[12]:
        songlist = p12
    w_songlist.delete(0, "end")
    for song in songlist:
        w_songlist.insert("end", song)
    in_main = False

def loadlist():
    global songlist
    global in_main
    songlist = []
    for song in os.listdir():
        ext = os.path.splitext(song)[1]
        if ext == ".mp3":
            songlist.append(song)
    updatelistwidget()
    in_main = True

def gohome():
    w_songlist.delete(0, "end")
    w_playlistlist.delete(0, "end")
    loadlist()

def startstop():
    global Playing
    if Playing == True:
        pygame.mixer.music.pause()
        Playing = False
    else:
        try:
            pygame.mixer.music.unpause()
            Playing = True
        except:
            pass

def prevsong():
    global current_song_idx
    global current_song
    global Playing
    try:
        pygame.mixer.music.load(songlist[current_song_idx -1])
        current_song = songlist[current_song_idx -1]
        current_song_idx = current_song_idx -1
        play()
        Playing = True
    except:
        pass
        
def nextsong():
    global current_song_idx
    global current_song
    global Playing
    try:
        pygame.mixer.music.load(songlist[current_song_idx + 1])
        current_song = songlist[current_song_idx + 1]
        current_song_idx = current_song_idx + 1
        play()
    except:
        pygame.mixer.music.load(songlist[0])
        current_song = songlist[0]
        current_song_idx = 0
        play()
    playing = True

def edit():
    global in_main
    global playlists
    global w_songstoadd
    

    if in_main == True:
        newp = tkinter.Toplevel()
        newp.config(bg= "#464646")
        w_newname = ttk.Entry(newp)
        def createpl():
            playlists.append(w_newname.get())
            updatelistwidget()
            save()
            newp.destroy()
        w_createButton = ttk.Button(newp, text= "Create!", command= createpl)

        w_newname.grid(row= 0, column= 0, padx= 3, pady= 3)
        w_createButton.grid(row= 0, column= 1, padx= 3, pady= 3)
    if in_main == False:
        addp = tkinter.Toplevel()
        addp.config(bg= "#464646")
        w_songstoadd = tkinter.Listbox(addp)
        songstoadd = []
        for song in os.listdir():
            songstoadd.append(song)
        w_songstoadd.delete(0, "end")
        for song in songstoadd:
            w_songstoadd.insert("end", song)

        def addtopl():
            global p0
            global p1
            global p2
            global p3
            global p4
            global p5
            global p6
            global p7
            global p8
            global p9
            global p10
            global p11
            global p12

            sta = songstoadd[int((str(w_songstoadd.curselection()).strip("(,)")))]

            if songlist == p0:
                p0.append(sta)
            elif songlist == p1:
                p1.append(sta)
            elif songlist == p2:
                p2.append(sta)
            elif songlist == p3:
                p3.append(sta)
            elif songlist == p4:
                p4.append(sta)
            elif songlist == p5:
                p5.append(sta)
            elif songlist == p6:
                p6.append(sta)
            elif songlist == p7:
                p7.append(sta)
            elif songlist == p8:
                p8.append(sta)
            elif songlist == p9:
                p9.append(sta)
            elif songlist == p10:
                p10.append(sta)
            elif songlist == p11:
                p11.append(sta)
            elif songlist == p12:
                p12.append(sta)
            updatelistwidget()
            save()

        w_addsongbutton = ttk.Button(addp, text= "Add song", command= addtopl)
        w_songstoadd.grid(row= 0, column= 0, padx= 3, pady= 3)
        w_addsongbutton.grid(row= 1, column= 0, padx= 3, pady= 3)

w_songlist = tkinter.Listbox(root, width= 50)
w_songlabel = ttk.Label(root, textvariable= songlabeltext)
w_homebutton = ttk.Button(root, text= "Home", command= gohome)
w_previousbutton = ttk.Button(root, text= "<<", command= prevsong)
w_playbutton = ttk.Button(root, text= "Play/Pause", command= startstop)
w_nextbutton = ttk.Button(root, text= ">>", command= nextsong)
w_editbutton = ttk.Button(root, text= "Edit", command= edit)
w_playlistlist = tkinter.Listbox(root, height= 14)

def updatelistwidget():
    w_playlistlist.delete(0, "end")
    w_songlist.delete(0, "end")
    for song in songlist:
        w_songlist.insert("end", os.path.splitext(song)[0])
    for pl in playlists:
        w_playlistlist.insert("end", pl)

w_songlist.grid(row= 0, column= 2, columnspan= 5, padx= 5, pady= 3)
w_songlabel.grid(row= 1, column= 2, columnspan= 5, pady= 3)
w_pbar.grid(row= 3, column= 2, columnspan= 5)
w_homebutton.grid(row= 4, column= 2, pady= 3)
w_previousbutton.grid(row= 4, column= 3, pady= 3)
w_playbutton.grid(row= 4, column= 4, pady= 3)
w_nextbutton.grid(row= 4, column= 5, pady= 3)
w_editbutton.grid(row= 4, column= 6, pady= 3)
w_playlistlist.grid(row= 0, column= 0, rowspan= 5, padx= 5, pady= 3)

def startup():
    current_song = songlist[0]
    pygame.mixer.music.load(current_song)
    play()
    sleep(0.001)
    startstop()

def save():
    global p0
    global p1
    global p2
    global p3
    global p4
    global p5
    global p6
    global p7
    global p8
    global p9
    global p10
    global p11
    global p12
    global playlists
    os.chdir("C:\\Users\\emile\\Desktop\\python programs\\music_player\\saves")

    with open("spl.txt", "w", encoding="utf-8") as file:
        for f in playlists:
            file.write(f + "\n")
    with open("pl0.txt", "w", encoding="utf-8") as file:
        for f in p0:
            file.write(f + "\n")
    with open("pl1.txt", "w", encoding="utf-8") as file:
        for f in p1:
            file.write(f + "\n")
    with open("pl2.txt", "w", encoding="utf-8") as file:
        for f in p2:
            file.write(f + "\n")
    with open("pl3.txt", "w", encoding="utf-8") as file:
        for f in p3:
            file.write(f + "\n")
    with open("pl4.txt", "w", encoding="utf-8") as file:
        for f in p4:
            file.write(f + "\n")
    with open("pl5.txt", "w", encoding="utf-8") as file:
        for f in p5:
            file.write(f + "\n")
    with open("pl6.txt", "w", encoding="utf-8") as file:
        for f in p6:
            file.write(f + "\n")
    with open("pl7.txt", "w", encoding="utf-8") as file:
        for f in p7:
            file.write(f + "\n")
    with open("pl8.txt", "w", encoding="utf-8") as file:
        for f in p8:
            file.write(f + "\n")
    with open("pl9.txt", "w", encoding="utf-8") as file:
        for f in p9:
            file.write(f + "\n")
    with open("pl10.txt", "w", encoding="utf-8") as file:
        for f in p10:
            file.write(f + "\n")
    with open("pl11.txt", "w", encoding="utf-8") as file:
        for f in p11:
            file.write(f + "\n")
    with open("pl12.txt", "w", encoding="utf-8") as file:
        for f in p12:
            file.write(f + "\n")
    
    os.chdir("C:\\Users\\emile\\Desktop\\python programs\\music_player\\songs")

def openn():
    global p0
    global p1
    global p2
    global p3
    global p4
    global p5
    global p6
    global p7
    global p8
    global p9
    global p10
    global p11
    global p12
    global playlists
    os.chdir("C:\\Users\\emile\\Desktop\\python programs\\music_player\\saves")

    try:
        with open("spl.txt", "r", encoding="utf-8") as file:
            for f in file:
                playlists.append(f.strip())
        with open("pl0.txt", "r", encoding="utf-8") as file:
            for f in file:
                p0.append(f.strip())
        with open("pl1.txt", "r", encoding="utf-8") as file:
            for f in file:
                p1.append(f.strip())
        with open("pl2.txt", "r", encoding="utf-8") as file:
            for f in file:
                p2.append(f.strip())
        with open("pl3.txt", "r", encoding="utf-8") as file:
            for f in file:
                p3.append(f.strip())
        with open("pl4.txt", "r", encoding="utf-8") as file:
            for f in file:
                p4.append(f.strip())
        with open("pl5.txt", "r", encoding="utf-8") as file:
            for f in file:
                p5.append(f.strip())
        with open("pl6.txt", "r", encoding="utf-8") as file:
            for f in file:
                p6.append(f.strip())
        with open("pl7.txt", "r", encoding="utf-8") as file:
            for f in file:
                p7.append(f.strip())
        with open("pl8.txt", "r", encoding="utf-8") as file:
            for f in file:
                p8.append(f.strip())
        with open("pl9.txt", "r", encoding="utf-8") as file:
            for f in file:
                p9.append(f.strip())
        with open("pl10.txt", "r", encoding="utf-8") as file:
            for f in file:
                p10.append(f.strip())
        with open("pl11.txt", "r", encoding="utf-8") as file:
            for f in file:
                p11.append(f.strip())
        with open("pl12.txt", "r", encoding="utf-8") as file:
            for f in file:
                p12.append(f.strip())
    except:
        pass

    os.chdir("C:\\Users\\emile\\Desktop\\python programs\\music_player\\songs")


openn()
loadlist()
updatepbar()

w_songlist.bind("<<ListboxSelect>>", songlistclick)
w_playlistlist.bind("<<ListboxSelect>>", playlistlistclick)
w_pbar.bind("<Button-1>", pbarclick)
w_pbar.bind("<ButtonRelease-1>", pbarrelease)

check_event()
root.mainloop()