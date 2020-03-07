from .BaseReader import BaseReader
import gzip



class MindFileReader(BaseReader):

    supported_formats = ('.mind', '.mind.gz')

    def __init__(self, filepath):
        if not filepath.endswith(self.supported_formats):
            raise NotImplementedError(
                f'Given file format is not supported. The supported formats are {self.supported_formats}')
        self.file = gzip.open(filepath, 'rb') if filepath.endswith(
            'gz') else open(filepath, 'rb')

        user_size = int.from_bytes(self.file.read(4), 'little')
        self.user = self.file.read(user_size)

    def get_user_binary(self):
        return self.user

    def __iter__(self):
        return self

    def __next__(self):
        snapshot_len = self.file.read(4)
        if not snapshot_len:
            raise StopIteration
        snapshot_len = int.from_bytes(snapshot_len, 'little')
        return self.file.read(snapshot_len)
