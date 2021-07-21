
from numpy import record


def record_audio(file_path, duration):
    """
    Records the audio with given duration. In case of
    a unicode error give the file path as a raw string
    or give it as a linux file path.
    """
    import sounddevice as sd
    from scipy.io.wavfile import write
    
    fs = 44100 # Sample Rate
    seconds = duration # Duration of Recording
    
    myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
    sd.wait()
    write(file_path, fs, myrecording) # Save as WAV file

def start_recording():
    user_input = input("Press enter to start recording your audio.")

    if user_input == "":
        print("Recording...")
        record_audio("C:/Users/deniz/OneDrive/Documents/Deniz the Laps/Wewalk/Sound Analysis WeWalk/output.wav", 5)
        print("Recording finished.")
    else:
        print("Input detected, please only press enter as input.")
        start_recording()

start_recording()
