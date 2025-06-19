# for voice modulation and merging with video 
# should be used after de noising the audio
from pydub import AudioSegment
import librosa
import soundfile as sf
import os

def apply_modulation(input_audio, output_audio, modulation_type):
    y, sr = librosa.load(input_audio)

    if modulation_type == "robot":
        # Simple "robot" effect: pitch + tremolo simulation
        y = y * 0.5 + librosa.effects.harmonic(y)
    elif modulation_type == "deep":
        y = librosa.effects.pitch_shift(y=y, sr=sr, n_steps=-5)
    elif modulation_type == "funny":
        y = librosa.effects.pitch_shift(y=y, sr=sr, n_steps=5)
    elif modulation_type == "female":
        y = librosa.effects.pitch_shift(y=y, sr=sr, n_steps=3)
    elif modulation_type == "male":
        y = librosa.effects.pitch_shift(y=y, sr=sr, n_steps=-3)
    else:
        pass  # No modulation

    sf.write(output_audio, y, sr)

# paths
denoised_path = "/Users/rishuraj/Desktop/AI_DENOISER/separated/htdemucs/original_audio/vocals.wav"
modulated_path = "modulated.wav"

# Apply modulation
apply_modulation(denoised_path, modulated_path, "female")

import subprocess

def merge_audio_video(video_input, audio_input, output_path):
    command = [
        "ffmpeg", "-y",
        "-i", video_input,
        "-i", audio_input,
        "-c:v", "copy",
        "-map", "0:v:0",
        "-map", "1:a:0",
        "-shortest",
        output_path
    ]
    subprocess.run(command)

if __name__ == "__main__":
    video_input = "input_video.mp4"  # Path to the input video file
    audio_input = "modulated.wav"  # Path to the modulated audio file
    output_path = "output_video.mp4"  # Path for the output video with audio

    merge_audio_video(video_input, audio_input, output_path)
    print(f"Video and audio merged successfully into {output_path}")