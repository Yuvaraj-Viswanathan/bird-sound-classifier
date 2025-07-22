# 🐦 Bird Sound Classification System

A Python-based project that identifies bird species using recorded sounds. It uses Fast Fourier Transform (FFT), Priority Queue for frequency ranking, and Stack to display taxonomy.

---

## 🎯 Features

- Real-time bird call recording
- Frequency analysis using FFT
- Bird classification using priority queue
- Biological taxonomy display using stack

---

## 🛠️ Tech Stack

- Python 3
- NumPy
- SciPy
- PyAudio
- soundfile

---

## ▶️ How to Run

### Step 1:  Install Requirements
```bash
git clone https://github.com/YOUR_USERNAME/Bird-Sound-Classification-System.git
cd Bird-Sound-Classification-System
```
### Step 2: Clone the Repository
```
pip install -r requirements.txt

```
### Step 3: Run the Classifier
```
cd src
python bird_sound_classifier.py
```
## 📊 Data Structures Used

| **Structure**      | **Purpose**                                     |
|--------------------|-------------------------------------------------|
| `Stack`            | Stores and displays the taxonomic hierarchy     |
| `Priority Queue`   | Ranks birds based on amplitude and priority     |
| `Dictionary`       | Maps frequencies to bird species and priorities |
| `List`             | Holds audio frames and FFT peak data            |

---

## 📈 Future Scope

- Add ML model for smarter classification (e.g., CNN, LSTM)
- Mobile app integration for field classification
- Advanced noise filtering for outdoor accuracy
- Expand bird species and frequency database

---

## 👨‍💻 Authors

- Yuvaraj V  
- Sham Ganesh V  
- Varun G  
- Surya A  
- Madhan K  

> Under the guidance of **Dr. Radha Senthilkumar**,  
Associate Professor,  
Department of Electronics Engineering,  
MIT – Anna University

---

## 📄 License

This project is licensed under the **MIT License**.  
You are free to use, modify, and distribute it with attribution.
