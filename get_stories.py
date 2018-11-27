import codecs
import csv
import io
import os
import requests
from tqdm import tqdm

csvfile = codecs.open('data/Successful Conversations - main.csv', 'r')

reader = csv.DictReader(csvfile)
headers = {'Content-Type': 'text/markdown'}
url = "https://website-demo.rasa.com/api/conversations/{sender_id}?api_token=e8c436157a24b007ed5cdc9ba4d062ed66c4f63d"

total = 0
total_yes = 0
total_no = 0

texts_yes = []
texts_no = []

pbar = tqdm(reader)
for row in pbar:
    if row['sender_id'] and row['user goal fullfilled'] and row['user goal supported'] == 'getstarted':
        total += 1
        response = requests.get(url.format(sender_id=row['sender_id']), headers=headers)

        text = response.text.replace('Generated Story',
                                     'Generated Story goal:{}, id:{}'
                                     ''.format(row['user goal supported'],
                                               row['sender_id']))

        if 'es' in row['user goal fullfilled']:
            total_yes += 1
            text_yes = text + '    - success\n'
            texts_yes.append(text_yes)
        elif row['user goal fullfilled'] == 'no':
            total_no += 1
            text_no = text + '    - fail\n'
            texts_no.append(text_no)

print('\n')
print(total)
print(total_yes)
print(total_no)

os.remove("data/success/train_getstarted.md")
with io.open('data/success/train_getstarted.md', 'a', encoding="utf-8") as f:
    for text in texts_yes[:-5]:
        f.write(text + "\n")
    for text in texts_no[:-5]:
        f.write(text + "\n")

os.remove("data/success/test_getstarted.md")
with io.open('data/success/test_getstarted.md', 'a', encoding="utf-8") as f:
    for text in texts_yes[-5:]:
        f.write(text + "\n")
    for text in texts_no[-5:]:
        f.write(text + "\n")
