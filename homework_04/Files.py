"""Class for work with files"""

import pathlib


class Files:
        
    def __init__(self, dir_path, file_name, file_type = 'file'):
        """Initialization attributes of the class"""
        self.dir_path   = dir_path
        self.file_name  = file_name
        self.full_path  = pathlib.Path(dir_path).joinpath(file_name)
        self.type       = file_type
        
    def delete(self):
        """Deleting existing file"""
        try:
            if pathlib.Path(self.full_path).is_file():
                pathlib.Path(self.full_path).unlink()
        except BaseException as error:
            print('An exception occurred: {}'.format(error))
        
    def create(self):
        """Create a new file"""
        try:
            if not pathlib.Path(self.full_path).exists():
                pathlib.Path(self.full_path).touch()
        except BaseException as error:
            print('An exception occurred: {}'.format(error))
            
    def rename(self, new_name_path):
        """Rename file"""
        try:
            if pathlib.Path(self.full_path).is_file():
                pathlib.Path(self.full_path).rename(new_name_path)
        except BaseException as error:
            print('An exception occurred: {}'.format(error))
            
    def owner(self):
        """Return owner of the file"""
        if pathlib.Path(self.full_path).is_file():
            return pathlib.Path(self.full_path).owner
        return ''
