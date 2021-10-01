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


@cli.command()
@click.argument("cal-type", type=click.Choice(["dark", "bias", "flat"]))
@click.argument("files", nargs=-1)
def cal(cal_type, files):
    try:
        os.makedirs("JPG/{}".format(cal_type))
        os.makedirs("NEF/{}".format(cal_type))
    except FileExistsError:
        print("The subfolders already exist. Proceeding to move files into pre-existing folders.")
    for file in files:
        filename = f"DSC_{file.zfill(4)}"
        shutil.move(f"JPG/{filename}.JPG", f"JPG/{cal_type}/")
        shutil.move(f"NEF/{filename}.NEF", f"NEF/{cal_type}/")

if __name__ == "__main__":
    cli()
