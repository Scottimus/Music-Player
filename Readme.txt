
Need to install ffmpeg from this package

If you haven't installed the ffmpeg/ffprobe as @Rotem answered, you can use my ffmpeg-downloader package:

pip install ffmpeg-downloader
ffdl install --add-path
The --add-path option adds the installed FFmpeg folder to the user's system path. Re-open the Python window and both ffmpeg and ffprobe will be available to your program.