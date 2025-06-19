from moviepy.editor import VideoFileClip
import subprocess

video = VideoFileClip("Input_video.mp4")
video.audio.write_audiofile("original_audio.wav")


# for  separating audio into vocals and instrumental, we will use Demucs.
# Demucs is a tool for music source separation.
# It can separate audio into vocals, drums, bass, and other instruments.
def merge_audio_video(audio_path, output_path):
    command = [
        "python3.12", "-m", "demucs",audio_path,
        f"python3.12 -m demucs -n mdx_extra_q -o {output_path} {audio_path}",
        
    ]
    subprocess.run(command)
if __name__ == "__main__":
    audio_path = "original_audio.wav"  # Path to the extracted audio file
    output_path = "seprated"  # Directory where separated audio will be saved

    merge_audio_video(audio_path, output_path)
    print(f"Audio separated successfully into {output_path}")
# To separate the audio into vocals and instrumental, use Demucs comand.
# python3.12 -m demucs path_to_audio.wav
# After running the Demucs command, the audio will be separated into different folders.

# for merging audio back with video, you can use ffmpeg command:
# ffmpeg -i Input_video.mp4 -i separated/htdemucs/original_audio/vocals.wav -c:v copy -map 0:v:0 -map 1:a:0 -shortest clean_output.mp4