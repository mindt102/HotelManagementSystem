import os

FILEPATH = os.path.dirname(__file__)
DATAPATH = os.path.join(FILEPATH, "../sample-data/")

if __name__ == "__main__":
    with open(DATAPATH + "names.txt", "r") as f:
        print(f.readline())