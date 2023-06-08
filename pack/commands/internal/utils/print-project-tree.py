import argparse

from definitions import ROOT_PATH
from pack.modules.internal.theme.theme_functions import print_tree


def main():
    print_tree(
        start_dir=ROOT_PATH,
        exclude_dirs=['venv'],
        exclude_file_starts=['.', '_'],
        title="Directory Tree",
        show_exts=True
    )
