import os

from codemonkeys.types import OStr


class OutputPathResolver:

    _output_path: OStr = None
    _output_ext: OStr = None
    _output_filename_append: OStr = None
    _relative_path_root: OStr = None

    def output_path(self, output_path: str) -> 'OutputPathResolver':
        """
        Sets the output path.

        :param str output_path: Set the root path for your output.
        :return: OutputPathResolver instance
        """
        self._output_path = output_path
        return self

    def output_filename_append(self, output_filename_append: OStr = None) -> 'OutputPathResolver':
        """
        Sets a string to append to output filenames

        :param str output_filename_append: String to append to output filenames
        :return: OutputPathResolver instance
        """
        self._output_filename_append = output_filename_append
        return self

    def output_ext(self, output_ext: str) -> 'OutputPathResolver':
        """
        Sets the output file extension.

        :param str output_ext: Extension to set for output file
        :return: OutputPathResolver instance
        """
        self._output_ext = output_ext
        return self

    def relative_from_root(self, relative_path_root: OStr = None) -> 'OutputPathResolver':
        """
        Set a root path (must be part of all original filepaths, usually the WORK_PATH)
        This means a file read from relative_root_path/abc/def.txt will be written to OUTPUT_PATH/abc/def.txt.

        :param relative_path_root: Root path to use for relative path
        :return: OutputPathResolver instance
        """
        self._relative_path_root = relative_path_root
        return self

    def output_file_exists(self, file_path: str) -> bool:
        """
        Check if the output file exists.

        :param str file_path: Path of the output file to check
        :return: bool. True if file exists, False otherwise
        """
        return os.path.exists(self.get_output_path(file_path))

    def get_output_path(self, file_path: str, override_file_name: OStr = None) -> str:
        """
        Get the output path for the given file.

        :param str file_path: Path of the file for which the output path is to be calculated
        :param OStr override_file_name: Optionally override the file basename, otherwise it will be calculated from file_path
        :return: str. Calculated output path for file
        """
        original_file_name = os.path.basename(file_path)
        file_name = override_file_name or original_file_name
        without_ext = os.path.splitext(file_name)[0]
        ext = self._output_ext or os.path.splitext(file_name)[1]

        output_file_name = f"{without_ext}{self._output_filename_append or ''}{ext}"

        output_file_path = self._output_path
        if self._relative_path_root:
            relative_path = os.path.relpath(file_path, self._relative_path_root).replace(original_file_name, '')
            output_file_path = os.path.join(self._output_path, relative_path)

        return os.path.join(output_file_path, output_file_name)
