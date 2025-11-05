import pathlib
from PIL import Image


class Files:
    """Class for work with mediafiles"""
    
    def __init__(self, dir_path, file_name):
        self.dir_path   = dir_path
        self.file_name  = file_name
        self.full_path  = pathlib.Path(dir_path).joinpath(file_name)
        self.type       = "file"
        
    def delete(self):
        """Deleting existing file"""
        try:
            if pathlib.Path(self.full_path).is_file():
                pathlib.Path(self.full_path).unlink()
        except BaseException as error:
            print('An exception occurred: {}'.format(error))
        
    def create(self):
        """Creates a new file"""
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


class PictureFile(Files):
    def __init__(self, dir_path, file_name, picture_type = ''):
        super(PictureFile, self).__init__(dir_path, file_name)
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
