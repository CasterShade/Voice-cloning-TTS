# Dynamic Fine-Tuning and Adaptive Reference Selection for StyleTTS2 in Speaker-Specific Voice Synthesis Using YouTube Data

This repository accompanies the paper:  
**"Dynamic Fine-Tuning and Adaptive Reference Selection for StyleTTS2 in Speaker-Specific Voice Synthesis Using YouTube Data"**  
*Mohammad Zubair Khan, Katz School of Science and Health, Yeshiva University, New York, NY, USA*

**Paper Link:** [https://github.com/CasterShade/Voice-cloning-TTS](https://github.com/CasterShade/Voice-cloning-TTS)

## Overview

This project presents a fully automated, data-to-training pipeline and a dynamic fine-tuning methodology for synthesizing high-fidelity, speaker-specific voices using the StyleTTS2 model. Leveraging heterogeneous audio sources—YouTube videos, podcasts, and Zoom meeting recordings—the system automates every step, from raw audio collection and segmentation to text and phoneme transcription, creating speaker-tailored datasets for training.

After fine-tuning StyleTTS2 to replicate specific speakers’ vocal styles, the project introduces a **dynamic reference selection** mechanism based on cosine similarity between input text and training transcripts. This ensures that the synthesized audio style adapts to the most contextually relevant reference speech. Additionally, a custom evaluation framework is proposed, comparing synthesized and reference audio at the word level for more accurate fidelity and intelligibility assessments.

The work also explores knowledge distillation by creating a smaller “student” model with half the number of hidden layers. While this did not yield performance improvements, it highlights future directions for model compression in high-fidelity TTS systems.

## Key Contributions

1. **Automated Multi-Source Data Pipeline:**  
   - **Data Scraping & Processing:** Collects speech data from YouTube, podcasts, and Zoom meetings.  
   - **Speaker Diarization & Segmentation:** Isolates the target speaker’s audio, splits it into sentence-level chunks.  
   - **Transcription & Phoneme Conversion:** Dynamically generates transcripts and phoneme alignments without manual intervention.

2. **Dynamic Fine-Tuning with StyleTTS2:**  
   - Adapts StyleTTS2 for speaker-specific characteristics.
   - Achieves high-fidelity synthesis even from limited, noisy data sources.

3. **Adaptive Reference Selection via Cosine Similarity:**  
   - Chooses contextually relevant reference samples by comparing input text embeddings with training transcripts.
   - Enhances style fidelity, ensuring the synthesized speech closely matches the speaker’s authentic tone and mannerisms.

4. **Custom Word-Level Evaluation Metrics:**  
   - Incorporates WhisperX-based word-level segmentation and phoneme alignment.
   - Evaluates synthesized vs. ground truth audio at word granularity, yielding deeper insights than standard utterance-level metrics.
   - Measures naturalness, intelligibility, and speaker identity retention using PESQ, STOI, CBAK, CSIG, COVL, and composite quality metrics.

5. **Student Model Exploration (Knowledge Distillation):**  
   - Attempts to compress StyleTTS2 into a student model with half as many hidden layers.
   - Although this did not improve performance, it provides groundwork for future efficiency-focused research.

## Data Sources & Preprocessing

- **YouTube:** Top search results for target speakers like Elon Musk or Donald Trump are downloaded and processed.
- **Podcasts & Zoom Recordings:** Additional audio sources enrich the dataset’s diversity.
- **Preprocessing Steps:**
  - Speaker diarization using `pyannote.audio` to isolate target voices.
  - Noise reduction, volume normalization, and segment trimming.
  - Automatic transcription and phoneme extraction for training readiness.

## Model & Training

- **Model:** StyleTTS2, an expressive neural TTS model with style diffusion.
- **Fine-Tuning Setup:**
  - Limited data environments handled gracefully.
  - A batch size of 2 and a learning rate of 1e-4 for stable adaptation.
  - 50 epochs of training with custom loss terms emphasizing speaker consistency.

- **Reference Selection:**
  - TF-IDF vectorization of training transcripts.
  - Cosine similarity to select a contextually relevant reference sample for each new input.
  - Maintains style consistency and improves perceived naturalness.

## Evaluation

- **Word-Level Comparison:**
  - Uses WhisperX to align synthesized and ground truth audio at the word level.
  - Compares corresponding words to assess phoneme accuracy, timing, and pitch stability.

- **Speech Quality Metrics:**
  - **PESQ & STOI:** Evaluate perceived quality and intelligibility.
  - **CSIG, CBAK, COVL:** Composite measures for signal fidelity, background distortion, and overall quality.
  - **Phoneme Accuracy:** Ensures precision in speaker’s articulation.
  - Results show high speaker identity retention and naturalness, with many listeners unable to distinguish synthesized voices from real speech.

## Results & Findings

- Achieves realistic voice cloning for various speakers, including high-profile figures.
- Dynamic reference selection significantly enhances voice style consistency.
- Custom word-level metrics offer a fine-grained, more accurate assessment of model performance than aggregate-level metrics.
- Student model compression attempts indicate that more sophisticated methods are needed for effective model size reductions.

## Limitations & Future Work

- **Data Dependence:** Quality is influenced by source recordings (YouTube/Zoom may have noise or variable quality).
- **Computational Costs:** Dynamic reference selection and fine-tuning are resource-intensive.
- **Future Directions:**
  - More efficient model compression techniques.
  - Faster inference strategies for real-time TTS.
  - More diverse datasets to improve generalization.


## Acknowledgements

- This work builds upon recent advancements in TTS, style transfer, and speaker verification research.
- Special thanks to the authors and maintainers of open-source libraries like `pyannote.audio`, `yt-dlp`, `librosa`, `phonemizer`, `pysepm`, and `WhisperX`.

---

**Disclaimer:**  
This project is for research and educational purposes only. The maintainers are not responsible for any misuse of the synthesized voices or the underlying technology.
