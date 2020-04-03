import requests
from bs4 import BeautifulSoup
import os
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('idx', type=str)
parser.add_argument('--contest',type=str)


contest = '1332'


args = parser.parse_args()
if args.contest:
    contest = args.contest
idx = args.idx
problem = "https://codeforces.com/contest/" + contest +"/problem/" + idx

response = requests.get(problem)

# if response.status_code == 200:
#     with open('problem.txt', 'w') as f:
#         f.write(response.text)

soup = BeautifulSoup(response.text, 'html.parser')
inp = soup.findAll("div", {"class": "input"})
try:
    os.mkdir('testcases')
except FileExistsError:
    # directory already exists
    pass

os.chdir('testcases')
# [os.remove(i) for i in os.listdir()]

try:
    os.mkdir('inp')
    os.mkdir('op')
except FileExistsError:
    pass

os.chdir('inp')
[os.remove(i) for i in os.listdir()]
for en, i in enumerate(inp):
    with open(str(en) + '.txt', 'w') as f:
        ip = i.find("pre").text.lstrip()
        f.write(ip)

os.chdir('../op')
[os.remove(i) for i in os.listdir()]
op = soup.findAll('div', {'class': 'output'})

for en, i in enumerate(op):
    with open(str(en) + '.txt', 'w') as f:
        p = i.find("pre").text.lstrip()
        f.write(p)
        # f.write('\n')

