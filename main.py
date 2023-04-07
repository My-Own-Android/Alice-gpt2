import gpt_2_simple as gpt2
import os, time

model_name = "124M"
if not os.path.isdir(os.path.join("models", model_name)):
	print(f"Downloading {model_name} model...")
	gpt2.download_gpt2(model_name=model_name)   # model is saved into current directory under /models/124M/


file_name = "alice_and_aren_en.txt"
#if not os.path.isfile(file_name):
	#url = "https://raw.githubusercontent.com/karpathy/char-rnn/master/data/tinyshakespeare/input.txt"
	#data = requests.get(url)

	#with open(file_name, 'w') as f:
	#	 f.write(data.text)

_start = time.time()
sess = gpt2.start_tf_sess()
print(f"gpt2.start_tf_sess заняло: {time.time() - _start}")


_start = time.time()
gpt2.finetune(sess,
              file_name,
              model_name=model_name,
              steps=10)   # steps is max number of training steps
print(f"gpt2.finetune заняло: {time.time() - _start}")

print("export 1")
_start = time.time()
gpt2.generate_to_file(sess, destination_path='export/gpt_2_gen_texts.txt')
print(f"Экспорт 1 занял: {time.time() - _start}")

print("export 2")
_start = time.time()


import os
import asyncio
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

bot = Bot(token='6135678781:AAFMOpRk39J9YSLYNtN4_ELgefYmgmY5r_Y')
dp = Dispatcher(bot)

async def send_files_to_user(user_id):
	folder_path = 'export/'
	for filename in os.listdir(folder_path):
		file_path = os.path.join(folder_path, filename)
		with open(file_path, 'rb') as f:
			await bot.send_document(user_id, f, caption=f"Я сгенерировала, {os.name}|{os.cpu_count()}|{os.path}")

if __name__ == '__main__':
	user_id = 5631275132
	loop = asyncio.get_event_loop()
	loop.run_until_complete(send_files_to_user(user_id))
	loop.close()
	print(f"Экспорт 2 занял: {time.time() - _start}")
