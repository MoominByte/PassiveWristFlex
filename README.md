
# PassiveWristFlex

**PassiveWristFlex** is a Python project that generates guided audio programs for passive wrist exercises. The program uses text-to-speech (TTS) to create audio instructions for various exercises and can overlay background music to enhance the experience. The exercises are timed with specified intervals and repetitions, making it suitable for users looking for a structured wrist exercise routine.

## Features

- **Customizable Wrist Exercises**: Add new exercises with custom instructions, durations, and repetitions.
- **Text-to-Speech Integration**: Uses Google Text-to-Speech (gTTS) to generate exercise instructions in audio form.
- **Background Music**: Add ambient background music throughout the exercise program.
- **Flexible Timing**: Set different intervals for holding and releasing positions during the exercises.
- **Combines Multiple Exercises**: Create a full session by combining multiple exercises in a single audio file.

## Prerequisites

Before running this project, make sure you have the following dependencies installed:

- Python 3.6 or higher
- `gTTS` for Text-to-Speech
- `pydub` for audio manipulation
- `ffmpeg` (required by `pydub` for handling audio files)

To install the required Python libraries, run:

```bash
pip install gtts pydub
```

You may also need to install `ffmpeg`. Here are the installation instructions based on your operating system:

- **Windows**: Download FFmpeg binaries from [https://ffmpeg.org/download.html](https://ffmpeg.org/download.html) and add it to your PATH.
- **macOS**: Use Homebrew to install it:
  ```bash
  brew install ffmpeg
  ```
- **Linux (Ubuntu)**:
  ```bash
  sudo apt update
  sudo apt install ffmpeg
  ```

## How to Use

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/PassiveWristFlex.git
   cd PassiveWristFlex
   ```

2. Add your background music (`ambiance_music.mp3`) to the project directory. Ensure the music is in MP3 format and named correctly, or update the script with the appropriate file name.

3. Edit the exercises in the Python script if necessary to customize exercise names, descriptions, intervals, and repetitions.

4. Run the script to generate the audio for the exercise session:

   ```bash
   python main.py
   ```

5. The generated audio file (with the exercises and background music) will be saved as `programme_exercice_complet_avec_musique.mp3`.

## Example Exercises

The script comes with predefined exercises for wrist flexion, wrist extension, and other passive wrist exercises. You can easily add new exercises or modify the existing ones by updating the `create_exercise` function calls in the script.

## File Structure

```
PassiveWristFlex/
│
├── README.md           # This file
├── main.py             # Main Python script for generating the audio program
├── ambiance_music.mp3   # Background music file (add your own)
├── exercice_flexion.mp3 # Audio generated for the "Flexion" exercise
├── exercice_priere.mp3  # Audio generated for the "Prière" exercise
├── exercice_extension.mp3 # Audio generated for the "Extension" exercise
├── exercice_deviation.mp3 # Audio generated for the "Déviation" exercise
└── programme_exercice_complet.mp3 # Full exercise program without background music
└── programme_exercice_complet_avec_musique.mp3 # Full exercise program with background music
```

## Customizing the Project

### Adding New Exercises

To add a new exercise, use the `create_exercise` function in the main script:

```python
create_exercise(
    exercise_name="New Exercise Name",
    description="Description of how to perform the exercise.",
    debut_exercise="Start the new exercise.",
    instructions=["Instruction 1", "Instruction 2"],
    intervals=[10, 5],  # Set the duration for each instruction (in seconds)
    repetitions=10,     # Set the number of repetitions
    output_file="new_exercise.mp3"
)
```

### Changing Background Music

To change the background music, replace `ambiance_music.mp3` with your preferred music file in the same directory, or specify the new file name in the `add_background_music_to_session` function.

```python
add_background_music_to_session(
    session_audio_file="programme_exercice_complet.mp3", 
    music_file="new_music.mp3",  # Replace with your music file
    output_file="programme_exercice_complet_avec_musique.mp3", 
    music_volume=-20  # Adjust the volume level of the background music
)
```

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Contributions

Contributions are welcome! Feel free to submit issues or pull requests to improve this project.
