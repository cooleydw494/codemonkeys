import os

from typing import Optional


class OutputPathResolver:

    def __init__(self):
        """
        Initializes the `OutputPathResolver` class.
        """
        self.work_path: Optional[str] = None
        self.output_path: Optional[str] = None
        self.output_ext: Optional[str] = None
        self.output_filename_append: Optional[str] = None
        self.use_work_path_relative_location: bool = False

    def set_output_path(self, output_path: str) -> 'OutputPathResolver':
        """
        Sets the output path.

        :param str output_path: Set the root path for your output.
        :return: OutputPathResolver instance
        """
        self.output_path = output_path
        return self

    def set_output_filename_append(self, output_filename_append: str) -> 'OutputPathResolver':
        """
        Sets a string to append to output filenames

        :param str output_filename_append: String to append to output filenames
        :return: OutputPathResolver instance
        """
        self.output_filename_append = output_filename_append
        return self

    def set_output_ext(self, output_ext: str) -> 'OutputPathResolver':
        """
        Sets the output file extension.

        :param str output_ext: Extension to set for output file
        :return: OutputPathResolver instance
        """
        self.output_ext = output_ext
        return self

    def set_work_path(self, work_path: str) -> 'OutputPathResolver':
        """
        Sets the work path.

        :param str work_path: Work path to set
        :return: OutputPathResolver instance
        """
        self.work_path = work_path
        return self

    def set_use_work_path_relative_location(self, should_use: bool) -> 'OutputPathResolver':
        """
        Sets whether to use work path for relative location.
        This means a file read from WORK_PATH/abc/def.txt will be written to OUTPUT_PATH/abc/def.txt.

        :param bool should_use: Whether to use work path relative locations.
        :raises Exception: If work path has not been set before this function call.
        :return: OutputPathResolver instance
        """
        if self.work_path is None:
            raise Exception('You must set the work path before setting use_work_path_relative_location')
        self.use_work_path_relative_location = should_use
        return self

    def output_file_exists(self, file_path: str) -> bool:
        """
        Check if the output file exists.

        :param str file_path: Path of the output file to check
        :return: bool. True if file exists, False otherwise
        """
        return os.path.exists(self.get_output_path(file_path))

    def get_output_path(self, file_path: str, basename: Optional[str] = None) -> str:
        """
        Get the output path for the given file.

        :param str file_path: Path of the file for which the output path is to be calculated
        :param Optional[str] basename: Base name for file. If not provided, the base name of the given file is used
        :return: str. Calculated output path for file
        """
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
