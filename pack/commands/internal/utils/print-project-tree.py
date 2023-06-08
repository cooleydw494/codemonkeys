from pack.modules.internal.theme.theme_functions import print_tree


def print_project_tree():
    print_tree(
        start_dir='..',
        exclude_dirs=['venv'],
        exclude_file_starts=['.', '_'],
        title="Directory Tree",
        show_exts=True
    )


if __name__ == '__main__':
    print_project_tree()

