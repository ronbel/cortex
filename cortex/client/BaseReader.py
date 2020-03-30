from abc import ABC, abstractmethod


class BaseReader(ABC):

    def __init__(self, filepath):
        self.filepath = filepath

    @abstractmethod
    def get_user_binary(self):
        pass
    
    @abstractmethod
    def __iter__(self):
        pass

    @abstractmethod    
    def __next__(self):
        pass
