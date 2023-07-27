import os

from typing import Optional


class OutputPathResolver:

    def __init__(self):
        self.work_path: Optional[str] = None
        self.output_path: Optional[str] = None
        self.output_ext: Optional[str] = None
        self.output_filename_append: Optional[str] = None
        self.use_work_path_relative_location: bool = False

    def set_output_path(self, output_path: str) -> 'OutputPathResolver':
        self.output_path = output_path
        return self

    def set_output_filename_append(self, output_filename_append: str) -> 'OutputPathResolver':
        self.output_filename_append = output_filename_append
        return self

    def set_output_ext(self, output_ext: str) -> 'OutputPathResolver':
        self.output_ext = output_ext
        return self

    def set_work_path(self, work_path: str) -> 'OutputPathResolver':
        self.work_path = work_path
        return self

    def set_use_work_path_relative_location(self, should_use: bool) -> 'OutputPathResolver':
        if self.work_path is None:
            raise Exception('You must set the work path before setting use_work_path_relative_location')
        self.use_work_path_relative_location = should_use
        return self

    def output_file_exists(self, file_path: str) -> bool:
        return os.path.exists(self.get_output_path(file_path))

    def get_output_path(self, file_path: str, basename: Optional[str] = None) -> str:
        the_file_name = os.path.basename(file_path)

        the_file_ext = os.path.splitext(the_file_name)[1]
        basename = basename if basename is not None else os.path.splitext(the_file_name)[0]

        filename_append = self.output_filename_append if self.output_filename_append is not None else ''
        ext = self.output_ext if self.output_ext is not None else the_file_ext
        output_file_name = f"{basename}{filename_append}{ext}"

        if self.use_work_path_relative_location:
            relative_path = os.path.relpath(file_path, self.work_path)
            output_file_path = os.path.join(self.output_path, relative_path).replace(the_file_name, output_file_name)
        else:
            output_file_path = os.path.join(self.output_path, output_file_name)

        return output_file_path
