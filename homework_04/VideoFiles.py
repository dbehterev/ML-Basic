"""Class for work with files"""

import pathlib
from Files import Files


class VideoFiles(Files):
    
    def __init__(self, dir_path, file_name, video_type = 'MPEG'):
        """Initialization attributes of the class"""
        super().__init__(dir_path, file_name)
        self.type = video_type
        
    def save(self, new_name):
        """Save video using new filename"""
        if pathlib.Path(self.full_path).exists():
            try: 
                # TODO: save file
                print('saving///')
            except BaseException as error:
                print('An exception occurred: {}'.format(error))

    def convery(self, new_format):
        """Convert video to another format"""
        if pathlib.Path(self.full_path).exists():
            try: 
                # TODO: convert video
                print('Converting video')
            except BaseException as error:
                print('An exception occurred: {}'.format(error))