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
      await bot.send_document(user_id, f, caption=f"Я сгенерировала, {os.name}|{os.cpu_count}|{os.path}")

if __name__ == '__main__':
  user_id = 5631275132
  loop = asyncio.get_event_loop()
  loop.run_until_complete(send_files_to_user(user_id))
  loop.close()