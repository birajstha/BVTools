import pyaudio
import numpy as np
import wave
import os
import subprocess

def play_and_save_sound(frequency, total_duration, beep_duration, pause_duration, file_name):
    p = pyaudio.PyAudio()

    volume = 0.5  # range [0.0, 1.0]
    fs = 44100  # sampling rate, Hz, must be integer

    # Initialize the stream
    stream = p.open(format=pyaudio.paFloat32,
                    channels=1,
                    rate=fs,
                    output=True)

    # Calculate the number of beeps
    num_beeps = int(total_duration / (beep_duration + pause_duration))

    all_samples = np.array([], dtype=np.float32)

    for _ in range(num_beeps):
        # Generate beep
        beep_samples = (np.sin(2 * np.pi * np.arange(fs * beep_duration) * frequency / fs)).astype(np.float32)
        # Generate pause
        pause_samples = np.zeros(int(fs * pause_duration), dtype=np.float32)
        # Concatenate beep and pause
        all_samples = np.concatenate((all_samples, beep_samples, pause_samples))

    # Write to stream
    stream.write(volume * all_samples)

    # Close the stream
    stream.stop_stream()
    stream.close()
    p.terminate()

    # Save to WAV file temporarily
    wav_file_name = file_name + ".wav"
    with wave.open(wav_file_name, 'wb') as wf:
        wf.setnchannels(1)
        wf.setsampwidth(p.get_sample_size(pyaudio.paFloat32))
        wf.setframerate(fs)
        wf.writeframes((volume * all_samples).tobytes())

    # Convert WAV to MP3
    mp3_file_name = file_name + ".mp3"
    subprocess.call(['ffmpeg', '-i', wav_file_name, mp3_file_name])

    # Remove temporary WAV file
    os.remove(wav_file_name)

# Example usage
play_and_save_sound(1000, 10, 1, 1, "beep_sound")