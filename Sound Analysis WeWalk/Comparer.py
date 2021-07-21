
from PitchDetector import pitch_detector 
from PyaudioRecorder import record_audio 

src = "C:/Users/deniz/OneDrive/Documents/Deniz the Laps/Wewalk/Sound Analysis WeWalk/output.wav"
src2 = "C:/Users/deniz/OneDrive/Documents/Deniz the Laps/Wewalk/Sound Analysis WeWalk/output2.wav"
record_audio(src, 4)
record_audio(src2, 4)
pitch = pitch_detector(src)
pitch2 = pitch_detector(src2)

if pitch > pitch2:
    print("First sound is louder.")
else:
    print("Second sound is louder.")


