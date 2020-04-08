from abc import ABC, abstractmethod


class BaseReader(ABC):
    """
    An abstract base class for all the reader classes. Custom readers must extend this class.
    Supported formats must be specified as class variable
    """

    supported_formats = ()

    def __init__(self, filepath):
        """
        Initializes a reader instance that reads from the given file

        :param filepath: The path to the file being read
        """
        self.filepath = filepath

    @abstractmethod
    def get_user_binary(self):
        """
        A method to get the user binary encoded according to cortex.proto

        :return: (string) A binary serialized user info string
        """
        pass
    
    @abstractmethod
    def __iter__(self):
        """
        The class must be an iterable that iterates over the snapshots from the file being read
        """
        pass

    @abstractmethod    
    def __next__(self):
        """
        Gets the next snapshot binary in the file according to cortex.proto

        :return: (string) A binary serialized snapshot string
        """
        pass
