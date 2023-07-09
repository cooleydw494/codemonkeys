import os


class OutputPathResolver:

    def __init__(self):
        self.output_path: str | None = None
        self.output_ext: str | None = None
        self.output_filename_append: str | None = None

    def set_output_path(self, output_path: str) -> 'OutputPathResolver':
        self.output_path = output_path
        return self

    def set_output_filename_append(self, output_filename_append: str) -> 'OutputPathResolver':
        self.output_filename_append = output_filename_append
        return self

    def set_output_ext(self, output_ext: str) -> 'OutputPathResolver':
        self.output_ext = output_ext
        return self

    def output_file_exists(self, file_path: str) -> bool:
        return os.path.exists(self.get_output_path(file_path))

    def get_output_path(self, file_path: str, basename: str | None = None) -> str:
        the_file_name = os.path.basename(file_path)

        the_file_ext = os.path.splitext(the_file_name)[1]
        basename = basename if basename is not None else os.path.splitext(the_file_name)[0]

        filename_append = self.output_filename_append if self.output_filename_append is not None else ''
        ext = self.output_ext if self.output_ext is not None else the_file_ext

        output_file_name = f"{basename}{filename_append}{ext}"
        output_file_path = os.path.join(self.output_path, output_file_name)
        return output_file_path
