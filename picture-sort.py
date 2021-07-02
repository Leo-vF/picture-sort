import os
import shutil
from tqdm import tqdm


def picture_sort():
    os.makedirs("JPG")
    os.makedirs("NEF")
    files = os.listdir()
    for file in tqdm(files):
        if file.endswith(".NEF"):
            shutil.move(file, "NEF/")
        elif file.endswith(".JPG"):
            shutil.move(file, "JPG/")


if __name__ == "__main__":
    picture_sort()
