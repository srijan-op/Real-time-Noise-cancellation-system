# Real-Time Noise Cancellation System

This project is a Python-based real-time noise cancellation system designed to process live audio input from a microphone. It features two distinct modes:

1. **Single Speaker Scenario**: Focuses on isolating and enhancing a single primary speaker’s voice while minimizing background noise and interference.
2. **Multiple Speaker Scenario**: Preserves multiple speakers’ voices while filtering out environmental noise such as white noise, workplace sounds, or vehicle noise.

## Features
- Real-time audio processing with minimal latency.
- Processes audio for both single speaker and multiple speaker scenarios.
- Saves processed audio to a `.wav` file.

---

## Requirements

### Prerequisites
To run this project, you need:

1. **Python 3.x** installed on your system. Download it from [here](https://www.python.org/downloads/).
2. Install the required Python libraries by running:
   ```bash
   pip install -r requirements.txt
   ```

---

## How to Run the Project

1. Clone or download the repository containing the project files.
2. Open a terminal and navigate to the directory containing the files.
3. Run the script:
   ```bash
   python noise_cancellation.py
   ```
4. Select a processing scenario when prompted:
   - Enter `1` for **Single Speaker Scenario**.
   - Enter `2` for **Multiple Speaker Scenario**.
5. Speak into the microphone while the program processes the audio in real-time.
6. The processed audio will be saved as `processed_audio.wav` in the project directory.

### Example Run
```plaintext
$ python noise_cancellation.py
Choose scenario (1: Single Speaker, 2: Multiple Speakers): 1
Recording...
Recording finished.
Processed audio saved as processed_audio.wav
```

---

## Project Structure
- **`noise_cancellation.py`**: Main script implementing the noise cancellation system.
- **`requirements.txt`**: File listing the Python dependencies required for the project.

---


