import config
import utils

# Module
import requests
import random
import time

key = random.choice(config.ZENZARR)
chances = 3

d = requests.get(utils.word_url(key))
d = d.json()['result']

while chances > 0:
  utils.clear()

  right_answer = d.get('jawaban')
  print(f'Kata: {d.get("soal")} Tipe: {d.get("tipe")}')

  tebakan = input('Susun kata berikut: ').upper()
  if right_answer == tebakan:
    print(f'Betul! Katanya adalah {right_answer}')
    break
  else:
    print('Maaf masih salah!')

  time.sleep(1)
  chances -= 1