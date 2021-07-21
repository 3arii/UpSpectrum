def record_audio(file_src, duration):
    """
    Returns an encoded WAV file. In case of an unicode
    error give file_src as a linux type path file.
    add 1 to the duration as it does - 1 for some reason.
    """
    import pyaudio
    import wave

    chunk = 1024 # Record in chunks of 1024 Samples
    sample_format = pyaudio.paInt16 # 16 bits per sample
    channels = 2
    fs = 44100 # This will recod at 44100 samples per second
    seconds = duration
    filesrc = file_src

    p = pyaudio.PyAudio()

    print("Recording...")

    stream = p.open(format=sample_format,
                    channels=channels,
                    rate=fs,
                    frames_per_buffer=chunk,
                    input=True)

    frames = []

    # Storing data in chunks for 3 secs
    for i in range(0, int(fs / chunk * seconds)):
        data = stream.read(chunk)
        frames.append(data)

    # Stops and closes the Stream
    stream.stop_stream
    stream.close()

    print("Finished Recording.")

    # Save the file as a WAV file.
    wf = wave.open(filesrc, "wb")
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(sample_format))
    wf.setframerate(fs)
    wf.writeframes(b"".join(frames))
    wf.close()


# C:/Users/deniz/OneDrive/Documents/Deniz the Laps/Wewalk/Sound Analysis WeWalk/output.wav
