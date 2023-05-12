import os
import pygame
from tkinter import Tk, Label, Button, Listbox, filedialog
from pydub import AudioSegment
from pydub.utils import mediainfo

class MusicPlayer:
    def __init__(self, master):
        self.master = master
        master.title("Music Player")

        self.playlist = Listbox(master, width=50)
        self.playlist.pack(padx=10, pady=10)

        self.load_button = Button(master, text="Load", command=self.load_music)
        self.load_button.pack()

        self.play_button = Button(master, text="Play", command=self.play_music)
        self.play_button.pack()

        self.pause_button = Button(master, text="Pause", command=self.pause_music)
        self.pause_button.pack()

        self.stop_button = Button(master, text="Stop", command=self.stop_music)
        self.stop_button.pack()

        self.next_button = Button(master, text="Next", command=self.next_track)
        self.next_button.pack()

        self.previous_button = Button(master, text="Previous", command=self.previous_track)
        self.previous_button.pack()

        self.current_track_label = Label(master, text="Current Track: ")
        self.current_track_label.pack()

        self.current_track_info = Label(master, text="")
        self.current_track_info.pack()

        self.music_directory = None
        self.music_files = []

        self.current_track = None

        pygame.mixer.init()

    def load_music(self):
        directory = filedialog.askdirectory()
        if directory:
            self.music_directory = directory
            self.music_files = [
                f for f in os.listdir(self.music_directory) if f.endswith((".mp3", ".flac"))
            ]
            self.playlist.delete(0, "end")
            for file in self.music_files:
                self.playlist.insert("end", file)

    def play_music(self):
        selected_track = self.playlist.get("active")
        if selected_track:
            track_path = os.path.join(self.music_directory, selected_track)
            if track_path.endswith(".flac"):
                audio = AudioSegment.from_file(track_path, format="flac", ffmpeg="C:\Program Files (x86)\ffmpeg\ffmpeg-6.0-essentials_build\bin")
                audio.export("temp.wav", format="wav")
                track_path = "temp.wav"

            pygame.mixer.music.load(track_path)
            pygame.mixer.music.play()
            self.current_track = selected_track
            self.current_track_info.config(text=self.current_track)

    def pause_music(self):
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.pause()

    def stop_music(self):
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.stop()
            self.current_track_info.config(text="")

    def next_track(self):
        current_index = self.music_files.index(self.current_track)
        next_index = (current_index + 1) % len(self.music_files)
        self.playlist.selection_clear(0, "end")
        self.playlist.selection_set(next_index)
        self.playlist.activate(next_index)
        self.playlist.see(next_index)
        self.play_music()

    def previous_track(self):
        current_index = self.music_files.index(self.current_track)
        previous_index = (current_index - 1) % len(self.music_files)
        self.playlist.selection_clear(0, "end")
        self.playlist.selection_set(previous_index)
        self.playlist.activate(previous_index)
       
if __name__ == "__main__":
    root = Tk()
    music_player = MusicPlayer(root)
    root.mainloop()
