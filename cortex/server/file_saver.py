

class BinaryFileSaver:
    def __init__(self,dir):
        self.dir = dir
    
    def save_file(self, filename, content):
        full_path = f'{self.dir}/{filename}'
        with open(full_path, 'wb') as f:
            f.write(content)
        return full_path