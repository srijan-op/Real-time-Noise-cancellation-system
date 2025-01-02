import pyaudio
import wave
import numpy as np
import scipy.signal as signal
from noisereduce import reduce_noise

# Define constants
CHUNK = 1024  # Audio chunk size
FORMAT = pyaudio.paInt16  # Format of audio input
CHANNELS = 1  # Mono audio
RATE = 16000  # Sampling rate
OUTPUT_FILE = "processed_audio.wav"

# Capture live audio stream from microphone
def record_audio(callback, duration=10):
    """
    Record audio from the microphone in real-time and process it using the provided callback function.

    :param callback: A function to process each chunk of audio.
    :param duration: Duration in seconds for recording.
    """
    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE,
                    input=True, frames_per_buffer=CHUNK)

    print("Recording...")
    frames = []

    for _ in range(0, int(RATE / CHUNK * duration)):
        data = stream.read(CHUNK)
        processed_data = callback(data)
        frames.append(processed_data)

    print("Recording finished.")
    stream.stop_stream()
    stream.close()
    p.terminate()

    return frames, p

# Noise Reduction Functions
def reduce_noise_single_speaker(audio_data, rate):

    # Convert audio data to numpy array
    audio_array = np.frombuffer(audio_data, dtype=np.int16)

    # Apply noise reduction
    reduced_noise = reduce_noise(y=audio_array, sr=rate)

    # Convert back to bytes
    return reduced_noise.astype(np.int16).tobytes()

def reduce_noise_multiple_speakers(audio_data, rate):

    audio_array = np.frombuffer(audio_data, dtype=np.int16)

    # Use a band-pass filter to preserve voice frequencies (e.g., 300Hz to 3400Hz)
    sos = signal.butter(10, [300, 3400], btype='bandpass', fs=rate, output='sos')
    filtered_audio = signal.sosfilt(sos, audio_array)

    # Apply noise reduction
    reduced_noise = reduce_noise(y=filtered_audio, sr=rate)

    return reduced_noise.astype(np.int16).tobytes()

# Save processed audio to a .wav file
def save_audio(frames, p, file_name=OUTPUT_FILE):

    wf = wave.open(file_name, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()
    print(f"Processed audio saved as {file_name}")

# Main execution
if __name__ == "__main__":
    # Choose scenario
    scenario = input("Choose scenario (1: Single Speaker, 2: Multiple Speakers): ")

    if scenario == "1":
        process_callback = lambda data: reduce_noise_single_speaker(data, RATE)
    elif scenario == "2":
        process_callback = lambda data: reduce_noise_multiple_speakers(data, RATE)
    else:
        print("Invalid choice. Defaulting to Single Speaker.")
        process_callback = lambda data: reduce_noise_single_speaker(data, RATE)

    # Record, process, and save audio
    audio_frames, py_audio_instance = record_audio(callback=process_callback, duration=10)
    save_audio(audio_frames, py_audio_instance)
