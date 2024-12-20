
# Voice Cloning Knowledge Distillation

This repository is a work in progress, the models are big in size so difficulty in uploading, all samples are yet to be added.

This repository contains a research project focusing on **voice cloning** using **knowledge distillation techniques**. The main goal is to distill knowledge from a large teacher model (a high-quality, resource-intensive voice cloning system) into a smaller, more efficient student model without significantly compromising audio quality and speaker similarity.

By using knowledge distillation, we aim to reduce the computational footprint, memory usage, and inference latency of state-of-the-art voice cloning models, making them more accessible and deployable on edge devices or less powerful hardware setups.

## Key Features

- **Knowledge Distillation Pipeline:**  
  Leverages a high-fidelity teacher TTS (Text-to-Speech) model to train a smaller student model. The student model learns to replicate the teacher’s acoustic output and voice characteristics.
  
- **Multi-Speaker Voice Cloning:**  
  Works with multiple target speakers, allowing the student model to generalize and clone various voices.
  
- **Lightweight & Efficient:**  
  Optimized for lower computational cost while preserving voice quality and naturalness.

- **Famous Speaker Samples:**  
  Includes demonstration samples for notable voices such as:
  - Donald Trump
  - Elon Musk
  - Jensen Huang
  - Barack Obama

  These samples showcase the model’s ability to capture distinctive speaking styles, intonations, and vocal timbre.

## Getting Started

### Prerequisites

- **Python 3.7+**
- **PyTorch 1.10+** (GPU recommended for training)
- **Audio Processing Libraries:**  
  Such as `librosa`, `soundfile`
- **Model Dependencies:**  
  Requirements might differ based on the teacher and student architectures chosen. Install dependencies via:
  ```bash
  pip install -r requirements.txt
  ```

### Project Structure

```
.
├─ data/
│  ├─ teacher_audio/          # Original high-quality samples (for reference)
│  ├─ student_output/         # Output from the student model during training
│  └─ text_prompts.txt        # Sample texts used to generate audio
│
├─ models/
│  ├─ teacher_model/          # Pre-trained teacher model weights
│  ├─ student_model/          # Distilled student model weights (to be generated)
│
├─ scripts/
│  ├─ Voice_Clonning.ipynb   # Script for running the vice cloning pipeline and training, Script to run inference with the model, Tools to evaluate speaker similarity, quality, etc.
│  ├─ synthesize.py           # Script to run inference with the model, Tools to evaluate speaker similarity, quality, etc.
│  └─ styletts2_inference.py  # Script to run inference with the model
│
└─ samples/
   ├─ trump_samples/
   ├─ elon_musk_sample.wav
   ├─ jensen_huang_sample.wav
   ├─ obama_sample.wav
   └─ README.md (short description of each sample)
```

## Generated Audio Samples

In the [`samples/` directory](samples/), you will find example audio clips generated by the student model for well-known voices. These samples demonstrate how closely the student model can mimic the teacher’s output and speaker characteristics after distillation:

- [Trump Sample](samples/trump_samples/)
- [Elon Musk Sample](samples/elon_musk_sample.wav)
- [Jensen Huang Sample](samples/jensen_huang_sample.wav)
- [Obama Sample](samples/obama_sample.wav)

Listen to these samples to get a sense of the quality and capabilities of the distilled model.

## Limitations & Ethical Considerations

- **Voice Cloning Misuse:**  
  The ability to clone voices raises ethical and privacy concerns. Use responsibly, only for legally and ethically permissible scenarios.
  
- **Impersonation Risks:**  
  Generated voices can be misused for impersonation or misinformation. Consider watermarking or implementing authentication measures if deploying publicly.

- **Data & Licensing:**  
  Ensure that you have proper rights and licenses for any training data used, especially if dealing with proprietary speech datasets.

## Contributing

Contributions are welcome! Feel free to:

- Open issues for bugs, questions, or requests.
- Submit pull requests with improvements, new features, or documentation enhancements.

## Acknowledgements

- Inspiration from research on TTS, knowledge distillation, and neural vocoding.
- References to publicly available voice recordings and state-of-the-art speech synthesis models.

---

**Disclaimer:**  
This project is for research and educational purposes only. The maintainers are not responsible for any misuse of the generated voices.
```
