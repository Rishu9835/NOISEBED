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
denoised_path = "/Users/rishuraj/Desktop/AI_DENOISER/demucs_output/mdx_extra_q/original_audio/vocals.wav"
modulated_path = "modulated.wav"

# Apply modulation
apply_modulation(denoised_path, modulated_path, "female")