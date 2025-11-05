"""Class for work with pictures"""

import pathlib
from Files import Files
from PIL import Image


class PictureFile(Files):
        
    def __init__(self, dir_path, file_name, picture_type = ''):
        """Initialization attributes of the class"""
        super().__init__(dir_path, file_name)
        self.type = self.get_picture_info().get('format')
        
    def new(self, width, height, color):
        """Generate a new picture"""
        img = Image.new(mode = "RGBA", size = (width, height), color = color)
        img.show()
        
    def open(self):
        """Open picture"""
        if pathlib.Path(self.full_path).exists():
            img = Image.open(self.full_path)
            #print(dir(img))
            return img
        else:
            print('File doesn\'t exist')
            
    def get_picture_info(self):
        """Get picture info"""
        if pathlib.Path(self.full_path).exists():
            try: 
                img = self.open()
                # print (dir(img))
                return {
                    'width': img.width,
                    'height': img.height,
                    'format': img.format
                }
            except BaseException as error:
                print('An exception occurred: {}'.format(error))
        return {}
    
    def save(self, new_name):
        """Save picture using new filename"""
        if pathlib.Path(self.full_path).exists():
            try: 
                img = self.open()
                img = img.save(new_name)
            except BaseException as error:
                print('An exception occurred: {}'.format(error))

    def resize(self, width, height):
        """Resize picture"""
        if pathlib.Path(self.full_path).exists():
            try: 
                img = self.open()
                img = img.resize(width, height)
                img.save(self.full_path)
            except BaseException as error:
                print('An exception occurred: {}'.format(error))
        
jpeg_file = PictureFile('c:\\Education\\Python\\Learning\\tmp\\', 'bing.jpg', 'JPG')
#jpeg_file.create()
#print(jpeg_file.owner())
#print(jpeg_file.picture_type)
#jpeg_file.new()
#jpeg_file.open()
#info = jpeg_file.get_picture_info()
#print(info.get('format'))
#print(jpeg_file.type)