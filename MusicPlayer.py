import os
import pygame
from tkinter import Tk, Label, Button, Listbox, filedialog, messagebox

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
        self.paused = False

        pygame.mixer.init()

    def load_music(self):
        directory = filedialog.askdirectory()
        if directory:
            self.stop_music()
            self.current_track = None
            self.music_directory = directory
            self.music_files = sorted(
                f for f in os.listdir(self.music_directory)
                if f.lower().endswith((".mp3", ".flac"))
                and os.path.isfile(os.path.join(directory, f))
            )
            self.playlist.delete(0, "end")
            for file in self.music_files:
                self.playlist.insert("end", file)

    def play_music(self):
        selected_track = self.playlist.get("active")
        if selected_track:
            track_path = os.path.join(self.music_directory, selected_track)
            try:
                pygame.mixer.music.load(track_path)
                pygame.mixer.music.play()
            except (pygame.error, OSError) as error:
                messagebox.showerror("Playback error", str(error))
                return
            self.current_track = selected_track
            self.paused = False
            self.current_track_info.config(text=self.current_track)

    def pause_music(self):
        if self.paused:
            pygame.mixer.music.unpause()
            self.paused = False
        elif pygame.mixer.music.get_busy():
            pygame.mixer.music.pause()
            self.paused = True

    def stop_music(self):
        pygame.mixer.music.stop()
        self.paused = False
        self.current_track_info.config(text="")

    def next_track(self):
        self.step_track(1)

    def previous_track(self):
        self.step_track(-1)

    def step_track(self, direction):
        if not self.music_files:
            return
        if self.current_track in self.music_files:
            index = (self.music_files.index(self.current_track) + direction) % len(self.music_files)
        else:
            index = 0 if direction > 0 else len(self.music_files) - 1
        self.playlist.selection_clear(0, "end")
        self.playlist.selection_set(index)
        self.playlist.activate(index)
        self.playlist.see(index)
        self.play_music()
       
if __name__ == "__main__":
    root = Tk()
    music_player = MusicPlayer(root)
    root.mainloop()
