#pip install styletts2

from styletts2 import tts
import nltk
nltk.download('punkt_tab')


path_to_model = '/home/youshan/Downloads/Zubair StyleTTS2 Models and code/trump_styletts2.pth'

# No paths provided means default checkpoints/configs will be downloaded/cached.
my_tts = tts.StyleTTS2()


# Specific paths to a checkpoint and config can also be provided.
other_tts = tts.StyleTTS2(model_checkpoint_path=path_to_model, config_path='/home/youshan/Downloads/Zubair StyleTTS2 Models and code/config_ft.yml')

# Specify target voice to clone. When no target voice is provided, a default voice will be used.
other_tts.inference("Hello there, I am now a python package.", target_voice_path="/home/youshan/Downloads/Zubair StyleTTS2 Models and code/Dataset/trump/1.wav", output_wav_file="/home/youshan/Downloads/Zubair StyleTTS2 Models and code/output/another_test.wav")

#other_tts.inference("Hello there, I am now a python package.", output_wav_file="another_test.wav")

# Optionally create/write an output WAV file.
# out = my_tts.inference("Hello there, I am now a python package.", output_wav_file="test.wav")

