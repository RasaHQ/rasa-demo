import codecs
import csv
import io
import os
import requests
import random
from tqdm import tqdm


csvfile = codecs.open("data/Intents_ Actions >> User Goal - Sheet1.csv", 'r')
reader = csv.DictReader(csvfile)
pbar = tqdm(reader)
topic_dict = {}
for row in pbar:
    if row['User goal'] and row['type'] in {'action', 'form'}:
        topic_dict[row['Intent/Action Name'][2:]] = row['User goal']
        if row['if_success']:
            topic_dict[row['Intent/Action Name'][2:]] += '_' + row['if_success']

for topic in set(topic_dict.values()):
    print('- '+topic)
print('\n')
exit()
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
    if row['sender_id'] and len(row['sender_id']) > 20 and row['reason for failure'] != 'NLU' and row['user goal fullfilled'] and row['user goal fullfilled'] != 'neutral' and '11.2018' not in row['date']: #row['user goal fullfilled']: # and row['user goal supported'] == 'getstarted':
        total += 1
        response = requests.get(url.format(sender_id=row['sender_id']), headers=headers)
        if response.status_code == 200:
            text = response.text.replace('Generated Story',
                                         'Generated Story goal:{}, id:{}, {}'
                                         ''.format(row['user goal (if supported)'],
                                                   row['sender_id'],
                                                   row['date'])
                                         )#.replace('- rewind', '- event_rewind'
                                                   #)#.replace('- restart', '- event_restart')

            parts = text.split('\n')

            continue_flag = False
            if not parts[1].startswith('* get_started_step'):
                continue_flag = True
            for part in parts[2:]:
                if part.startswith('* get_started_step'):
                    continue_flag = True
            if continue_flag:
                continue

            for action, topic in topic_dict.items():
                text = text.replace(action + '\n', '{}: {}'.format(topic, action) + '\n')

            texts_yes.append(text)
            # if 'es' in row['user goal fullfilled']:
            #     total_yes += 1
            #     text_yes = text + '    - success\n'
            #     texts_yes.append(text_yes)
            # elif row['user goal fullfilled'] == 'no':
            #     total_no += 1
            #     text_no = text + '    - fail\n'
            #     texts_no.append(text_no)

print('\n')
print(total)
print(len(texts_yes))
print(len(texts_no))

random.shuffle(texts_yes)

os.remove("data/success/train_for_success.md")
with io.open('data/success/train_for_success.md', 'a', encoding="utf-8") as f:
    for text in texts_yes[:-20]:#[-250:-50]:
        f.write(text + "\n")
    for text in texts_no[:-15]:
        f.write(text + "\n")

os.remove("data/success/test_for_success.md")
with io.open('data/success/test_for_success.md', 'a', encoding="utf-8") as f:
    for text in texts_yes[-20:]:
        f.write(text + "\n")
    for text in texts_no[-15:]:
        f.write(text + "\n")


def label_file(path, output_path, topic_dict):
    with io.open(path, "r", encoding="utf-8") as file:
        text = file.read()

        for action, topic in topic_dict.items():
            text = text.replace(action + '\n',
                                '{}: {}'.format(topic, action) + '\n')

        with io.open(output_path, "w", encoding="utf-8") as f:
            f.write(text)
