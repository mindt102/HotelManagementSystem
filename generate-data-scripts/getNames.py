import re
import requests
import json
import threading
from tqdm import trange

threads = []

def requestNames():
    names = ""
    for _ in trange(150):
        res = requests.get("https://api.namefake.com/us")
        resDict = json.loads(res.text)
        names += resDict["name"] + "\n"
    with open("names.txt", "a") as f:
        f.write(names)

for _ in range(8):
    thread = threading.Thread(target=requestNames)
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()