# Python Music Player

A desktop audio player built with Python and Tkinter. It uses pygame for playback and pydub and FFmpeg for audio handling.

![Music Player interface](images/music-player.png)

## Run locally

Install Python with Tkinter support and put FFmpeg and FFprobe on your PATH. From the repository folder, install the Python dependencies and launch the player.

```bash
python -m pip install pygame pydub
python MusicPlayer.py
```

Choose a folder containing `.mp3` or `.flac` files, select a track, and click **Play**. FLAC playback converts the selected track to a temporary WAV file in the working directory.
