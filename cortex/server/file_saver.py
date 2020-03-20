import os

class BinaryFileSaver:
    def __init__(self,dir):
        self.dir = dir
        
    
    def save_file(self, filename, content):
        full_path = f'{self.dir}/{filename}'
        os.makedirs(os.path.dirname(full_path), exist_ok=True)
        with open(full_path, 'wb') as f:
            f.write(content)
        return full_path