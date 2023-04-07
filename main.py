import gpt_2_simple as gpt2
import os
import requests

model_name = "124M"
if not os.path.isdir(os.path.join("models", model_name)):
	print(f"Downloading {model_name} model...")
	gpt2.download_gpt2(model_name=model_name)   # model is saved into current directory under /models/124M/


file_name = "alice_and_aren.txt"
if not os.path.isfile(file_name):
	#url = "https://raw.githubusercontent.com/karpathy/char-rnn/master/data/tinyshakespeare/input.txt"
	#data = requests.get(url)

	#with open(file_name, 'w') as f:
	#	 f.write(data.text)


sess = gpt2.start_tf_sess()
gpt2.finetune(sess,
              file_name,
              model_name=model_name,
              steps=10)   # steps is max number of training steps

gpt2.generate_to_file(sess, destination_path='gpt_2_gen_texts.txt')