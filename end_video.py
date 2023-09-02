from pydub import AudioSegment
from moviepy.editor import VideoFileClip
import os

def stitch_video(input_video_file, output_video_file, audio_file):
    video_clip = VideoFileClip(input_video_file)
    audio_clip = AudioSegment.from_wav(audio_file)
    
    if len(video_clip) > len(audio_clip):
        audio_clip = audio_clip + audio_clip[-(len(video_clip)-len(audio_clip)):]
    
    video_clip = video_clip.set_audio(audio_clip)
    video_clip.write_videofile(output_video_file, codec='libx264', audio_codec='aac')

if __name__ == "__main__":
    input_video_file = "input_video.mp4"  # Replace with your input video file
    output_video_file = "output_video.mp4"  # Replace with your desired output video file
    audio_file = "output_audio.wav"  # Replace with your audio file

    stitch_video(input_video_file, output_video_file, audio_file)
