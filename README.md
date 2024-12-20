# Dynamic Fine-Tuning and Adaptive Reference Selection for StyleTTS2 in Speaker-Specific Voice Synthesis Using Multi-Source Audio Data

This repository accompanies the paper:  
**"Dynamic Fine-Tuning and Adaptive Reference Selection for StyleTTS2 in Speaker-Specific Voice Synthesis Using Multi-Source Audio Data"**  
*Mohammad Zubair Khan, Katz School of Science and Health, Yeshiva University, New York, NY, USA*

**Paper Link:** [[https://github.com/CasterShade/Voice-cloning-TTS](https://github.com/CasterShade/Voice-cloning-TTS/blob/main/Speech_Synthesis_Final_report.pdf)]

## Overview

This project presents a fully automated pipeline and a dynamic fine-tuning methodology for synthesizing high-fidelity, speaker-specific voices using the **StyleTTS2** model. Our approach uses heterogeneous audio sources—**YouTube videos**, **podcast interviews**, and **Zoom-meeting recordings**—to create comprehensive speaker datasets.

Key innovations include:

1. **Automated Multi-Source Data Preparation:**  
   - Collects and preprocesses audio from diverse platforms.
   - Applies speaker diarization, segmentation at natural voice breaks, transcription, and phoneme conversion.
   - Produces training-ready datasets with minimal manual intervention.

2. **Dynamic Fine-Tuning of StyleTTS2:**  
   - Adapts the StyleTTS2 model to replicate each target speaker’s vocal characteristics.
   - Achieves speaker-specific synthesis even from limited, noisy initial data.

3. **Adaptive Reference Selection Using Cosine Similarity:**  
   - Introduces a reference speech selection mechanism.
   - Matches input text with training transcripts to find a contextually relevant reference sample.
   - Ensures synthesized speech closely aligns with the speaker’s style and intended context.

4. **Custom Word-Level Evaluation Metrics:**  
   - Incorporates WhisperX for word-level timestamp alignment.
   - Evaluates synthesized vs. reference audio on a per-word basis, offering finer-grained fidelity and intelligibility assessments.
   - Employs phoneme accuracy, pitch consistency, PESQ, STOI, and composite metrics (CSIG, CBAK, COVL) for a multidimensional performance view.

5. **Student Model Exploration:**  
   - Attempts knowledge distillation into a reduced student model with half the hidden layers.
   - Though unsuccessful, it highlights avenues for future model compression and efficiency research.

## Data Sources & Preprocessing

- **YouTube:** Audio scraping and diarization to isolate target speakers.
- **Podcasts & Zoom Recordings:** Additional data to capture diverse speech conditions and styles.
- **Preprocessing Steps:**
  - Speaker diarization (using `pyannote.audio`).
  - Noise reduction, volume normalization, and trimming.
  - Automated transcription and phoneme alignment.

## Model & Training Details

- **Model:** StyleTTS2 with style diffusion and adversarial training.
- **Fine-Tuning:** 
  - Performed over 50 epochs with a small batch size (2) and learning rate (1e-4).
  - Ensures speaker-specific traits are captured with minimal data.
- **Dynamic Reference Selection:**
  - Uses TF-IDF and cosine similarity to select the most contextually relevant reference audio.
  - Enhances naturalness and maintains speaker style consistency.

## Evaluation

- **Word-Level Analysis:**
  - WhisperX-based alignment to segment and compare synthesized vs. ground truth audio word-by-word.
- **Speech Quality & Intelligibility:**
  - PESQ, STOI for perceptual quality and intelligibility.
  - CSIG, CBAK, COVL for composite measures of signal distortion, background noise, and overall quality.
  - Phoneme-level accuracy assessments to ensure articulation fidelity.
- **Results:**
  - High naturalness, improved phoneme fidelity.
  - Synthesized voices are frequently perceived as indistinguishable from the real speakers.

## Results & Insights

- Achieved realistic voice cloning for various speakers, including those sourced from challenging audio (e.g., Zoom recordings).
- Dynamic reference selection significantly improved style fidelity and naturalness.
- Attempts at reducing model complexity (student model) revealed challenges in maintaining quality, guiding future efficiency strategies.

## Applications & Limitations

- **Applications:**
  - Personalized TTS, virtual assistants, media content creation, and forensic analysis.
- **Limitations:**
  - Dependence on high-quality source data; noisy environments affect outcomes.
  - Computationally intensive reference selection and fine-tuning steps.
  - Future work will focus on optimizing reference selection and investigating advanced model compression techniques.



## Acknowledgements

- This work builds on the advancements in neural TTS, style modeling, and speaker verification techniques.
- We acknowledge the authors of open-source tools and datasets that facilitated data scraping, transcription, alignment, and evaluation.

---

**Disclaimer:**  
This project is intended for research and educational purposes only. The authors and maintainers are not responsible for any misuse of the technology.

