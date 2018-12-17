import codecs
import csv
import io
import os
import requests
from tqdm import tqdm


csvfile = codecs.open("data/Intents_ Actions >> User Goal - Sheet1.csv", 'r')
reader = csv.DictReader(csvfile)
pbar = tqdm(reader)
topic_dict = {}
for row in pbar:
    if row['User goal'] and row['type'] == 'action':
        topic_dict[row['Intent/Action Name'][2:]] = row['User goal']
        if row['if_success']:
            topic_dict[row['Intent/Action Name'][2:]] += '_' + row['if_success']

# for topic in set(topic_dict.values()):
#     print('- '+topic)
# exit()

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
    if row['sender_id'] and len(row['sender_id']) > 20 and row['reason for failure'] != 'NLU':  # and row['user goal fullfilled'] and row['user goal supported'] == 'getstarted':
        total += 1
        response = requests.get(url.format(sender_id=row['sender_id']), headers=headers)

        text = response.text.replace('Generated Story',
                                     'Generated Story goal:{}, id:{}'
                                     ''.format(row['user goal (if supported)'],
                                               row['sender_id'])
                                     )#.replace('rewind', 'event_rewind'
                                              # ).replace('restart', 'event_restart')

        for action, topic in topic_dict.items():
            text = text.replace(action + '\n', topic + '\n')

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
print(total_yes)
print(total_no)

os.remove("data/success/train_no_NLU.md")
with io.open('data/success/train_no_NLU.md', 'a', encoding="utf-8") as f:
    for text in texts_yes[-600:-100]:
        f.write(text + "\n")
    for text in texts_no[:-15]:
        f.write(text + "\n")

os.remove("data/success/test_no_NLU.md")
with io.open('data/success/test_no_NLU.md', 'a', encoding="utf-8") as f:
    for text in texts_yes[-100:]:
        f.write(text + "\n")
    for text in texts_no[-15:]:
        f.write(text + "\n")
