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
    video_input = input("Enter the path to the video file: ")  # Path to the input video file
    audio_input = input("Enter audio path :")  # Path to the modulated audio file
    output_path = "output_video.mp4"  # Path for the output video with audio

    merge_audio_video(video_input, audio_input, output_path)
    print(f"Video and audio merged successfully into {output_path}")