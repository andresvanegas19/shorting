# script to download a youtube video and get the text from it
from pytube import YouTube
import urllib.request

def download_vide():
    """
    Download a video from youtube and keep in a buffer
    """
    import youtube_dl
    import os
    import subprocess
    import speech_recognition as sr
    from pydub import AudioSegment

    # Download YouTube video
    url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'wav',
            'preferredquality': '192'
        }]
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url, download=True)
        filename = ydl.prepare_filename(info_dict)
        video_id = info_dict.get("id", None)

    # Convert audio to text
    sound = AudioSegment.from_wav(filename)
    sound.export(f"{video_id}.flac", format="flac")

    r = sr.Recognizer()
    with sr.AudioFile(f"{video_id}.flac") as source:
        audio = r.record(source)
    text = r.recognize_google(audio)

    print(text)

    # Clean up
    os.remove(filename)
    os.remove(f"{video_id}.flac")
        

if __name__ == "__main__":
    download_vide()
