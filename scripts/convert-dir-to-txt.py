import os


def main():
    source_dir = './VirtueMaster'
    output_dir = './VirtueMasterTxt'
    file_types = ('.txt', '.md', '.svg', '.js', '.ts', '.json', '.sql')
    readme_file = None

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for root, dirs, files in os.walk(source_dir):
        for file in files:
            if file.endswith(file_types) and file != 'README.md':
                input_file_path = os.path.join(root, file)
                relative_path = os.path.relpath(input_file_path, source_dir)
                new_root = root.replace(source_dir, output_dir)
                output_file_path = os.path.join(new_root,
                                                f'{os.path.splitext(file)[0]}.{os.path.splitext(file)[1][1:]}.txt')

                if not os.path.exists(new_root):
                    os.makedirs(new_root)

                with open(input_file_path, 'r') as infile, open(output_file_path, 'w') as outfile:
                    outfile.write(
                        f'This is a txt representation of the VirtueMaster file located at {relative_path}\n\n')
                    outfile.write(infile.read())

            elif file == 'README.md':
                readme_input_file_path = os.path.join(root, file)
                readme_relative_path = os.path.relpath(readme_input_file_path, source_dir)

    if readme_file:
        readme_new_root = readme_input_file_path.replace(source_dir, output_dir)
        readme_output_file_path = os.path.join(os.path.dirname(readme_new_root),
                                               f'{os.path.splitext("README.md")[0]}.{os.path.splitext("README.md")[1][1:]}.txt')
        with open(readme_input_file_path, 'r') as infile, open(readme_output_file_path, 'w') as outfile:
            outfile.write(
                f'This is a txt representation of the VirtueMaster file located at {readme_relative_path}\n\n')
            outfile.write(infile.read())


if __name__ == '__main__':
    main()
