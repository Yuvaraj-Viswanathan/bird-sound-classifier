import numpy as np
import scipy.fftpack
import soundfile as sf
import pyaudio
import wave
import heapq

# Stack for taxonomy
class Stack:
    def _init_(self):
        self.stack = []

    def push(self, taxonomy):
        self.stack.append(taxonomy)

    def pop(self):
        return self.stack.pop() if self.stack else None

    def display(self):
        print("\nTaxonomy Hierarchy:")
        # Printing each taxonomy level in the required format
        taxonomy_levels = [
            "Kingdom", "Phylum", "Class", "Order", "Family", "Genus", "Species"
        ]
        for level, taxonomy in zip(taxonomy_levels, self.stack):
            print(f"{level}: {taxonomy}")

# Bird frequency definitions (Hz) with priority order
BIRDS = {
    "Eagle":   {"frequency_range": (3000, 3400), "priority": 1},
    "Parrot":  {"frequency_range": (1700, 1800), "priority": 2},
    "Peacock": {"frequency_range": (1000, 1700), "priority": 3},
    "Sparrow": {"frequency_range": (3500, 5000), "priority": 4},
    "Crow":    {"frequency_range": (1800, 2900), "priority": 5}
}

# Record audio
def record_audio(filename="recorded_audio.wav", duration=7, samplerate=22000):
    print("Recording audio...")
    audio = pyaudio.PyAudio()
    stream = audio.open(format=pyaudio.paInt16, channels=1, rate=samplerate,
                        input=True, frames_per_buffer=1024)

    frames = []
    for _ in range(int(samplerate / 1024 * duration)):
        data = stream.read(1024)
        frames.append(data)

    stream.stop_stream()
    stream.close()
    audio.terminate()

    with wave.open(filename, 'wb') as wf:
        wf.setnchannels(1)
        wf.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
        wf.setframerate(samplerate)
        wf.writeframes(b''.join(frames))

    print(f"Audio saved as {filename}")

# Extract top frequency peaks using priority queue
def extract_top_frequencies(audio_file, num_peaks=20):
    print("Extracting multiple peaks...")
    data, samplerate = sf.read(audio_file)

    # Convert stereo to mono
    if len(data.shape) > 1:
        data = np.mean(data, axis=1)

    # Apply window
    data *= np.hamming(len(data))

    # FFT
    fft_values = np.abs(scipy.fftpack.fft(data))[:len(data)//2]
    freqs = np.fft.fftfreq(len(data), d=1/samplerate)[:len(data)//2]

    # Priority queue: max heap by amplitude
    priority_queue = [(-amp, freq) for amp, freq in zip(fft_values, freqs)]
    heapq.heapify(priority_queue)

    top_frequencies = []
    seen = set()

    while priority_queue and len(top_frequencies) < num_peaks:
        neg_amp, freq = heapq.heappop(priority_queue)
        if freq > 0 and freq not in seen:
            seen.add(freq)
            top_frequencies.append((abs(freq), -neg_amp))

    return top_frequencies

# Classify by frequency based on priority order
def classify_bird(frequency):
    for bird, features in BIRDS.items():
        f_min, f_max = features["frequency_range"]
        if f_min <= frequency <= f_max:
            return bird
    return None

# Store taxonomy in structured format
def store_taxonomy(bird, stack):
    if bird == "Sparrow":
        stack.push("Animalia")  # Kingdom
        stack.push("Chordata")  # Phylum
        stack.push("Aves")  # Class
        stack.push("Passeriformes")  # Order
        stack.push("Passeridae")  # Family
        stack.push("Passer")  # Genus
        stack.push("Sparrow")  # Species
    elif bird == "Crow":
        stack.push("Animalia")
        stack.push("Chordata")
        stack.push("Aves")
        stack.push("Passeriformes")
        stack.push("Corvidae")
        stack.push("Corvus")
        stack.push("Crow")
    elif bird == "Parrot":
        stack.push("Animalia")
        stack.push("Chordata")
        stack.push("Aves")
        stack.push("Psittaciformes")
        stack.push("Psittacidae")
        stack.push("Psittacus")
        stack.push("Parrot")
    elif bird == "Peacock":
        stack.push("Animalia")
        stack.push("Chordata")
        stack.push("Aves")
        stack.push("Galliformes")
        stack.push("Phasianidae")
        stack.push("Pavo")
        stack.push("Peacock")
    elif bird == "Eagle":
        stack.push("Animalia")
        stack.push("Chordata")
        stack.push("Aves")
        stack.push("Accipitriformes")
        stack.push("Accipitridae")
        stack.push("Aquila")
        stack.push("Eagle")

# Main
def main():
    audio_file = "recorded_audio.wav"
    record_audio(audio_file)

    top_freqs = extract_top_frequencies(audio_file, num_peaks=20)
    taxonomy_stack = Stack()

    # Priority queue for bird detection based on frequency and priority
    priority_queue = []

    for freq, amp in top_freqs:
        bird = classify_bird(freq)
        if bird:
            print(f"Detected Bird: {bird} | Frequency: {freq:.2f} Hz | Amplitude: {amp:.2f}")
            # Push bird to the queue with its priority
            heapq.heappush(priority_queue, (BIRDS[bird]["priority"], bird, freq, amp))

    if priority_queue:
        # Select the most dominant bird (highest priority)
        _, dominant_bird, dominant_freq, dominant_amp = heapq.heappop(priority_queue)
        print(f"Most dominant bird detected: {dominant_bird} | Frequency: {dominant_freq:.2f} Hz | Amplitude: {dominant_amp:.2f}")
        store_taxonomy(dominant_bird, taxonomy_stack)
        taxonomy_stack.display()
    else:
        print("❌ No known bird detected in top frequencies.")

if _name_ == "_main_":
    main()

Ithu code uh