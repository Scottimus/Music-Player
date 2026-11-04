# Python Music Player

A desktop audio player built with Python, Tkinter, and pygame. It plays local MP3 and FLAC files directly through SDL_mixer.

![Music Player interface](images/music-player.png)

## Run locally

Install Python with Tkinter support. From the repository folder, install the dependency and launch the player.

```bash
python -m pip install -r requirements.txt
python MusicPlayer.py
```

Choose a folder containing `.mp3` or `.flac` files, select a track, and click **Play**. **Pause** toggles pause/resume. Previous and next wrap through the playlist and safely handle an empty list. Playback errors appear in a dialog.

Run the navigation and paused-stop regression checks with `python -m unittest discover -s tests -v`.
