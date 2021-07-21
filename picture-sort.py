import os
import shutil
from tqdm import tqdm
import click
from click_default_group import DefaultGroup


@click.group(cls=DefaultGroup, default="picture-sort", default_if_no_args=True)
def cli():
    pass


@cli.command()
def picture_sort():
    try:
        os.makedirs("JPG")
        os.makedirs("NEF")
    except FileExistsError:
        print("The subfolders already exist. Proceeding to move files into pre-existing folders.")
    files = os.listdir()
    for file in tqdm(files):
        if file.endswith(".NEF"):
            shutil.move(file, "NEF/")
        elif file.endswith(".JPG"):
            shutil.move(file, "JPG/")


@cli.command()
@click.argument("files", nargs=-1)
def rem(files):
    for file in files:
        filename = f"DSC_{file.zfill(4)}"
        os.remove(f"JPG/{filename}.JPG")
        os.remove(f"NEF/{filename}.NEF")


if __name__ == "__main__":
    cli()
