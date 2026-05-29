from pathlib import Path
from config import*
import shutil

from abc import ABC,abstractmethod

p = Path.home()/"Downloads"

class Manage(ABC):
    def __init__(self,path):
        self.path = path
    
    @abstractmethod
    def manage(self):
        pass

class Image(Manage):
    def __init__(self,path):
        super().__init__(path)

    def manage(self):
        files = [x for x in self.path.iterdir() if x.is_file()]
        for file in files:
            if file.suffix.lower() in IMAGE:
                target = self.path/"Images"/file.name
                file.rename(target)

class Document(Manage):
    def __init__(self,path):
        super().__init__(path)

    def manage(self):
        files = [x for x in self.path.iterdir() if x.is_file()]
        for file in files:
            if file.suffix.lower() in DOCUMENTS:
                target = self.path/"Documents"/file.name
                file.rename(target)
                print("Inserting Documents in Documents folder")

class Songs(Manage):
    def __init__(self,path):
        super().__init__(path)

    def manage(self):
        files = [x for x in self.path.iterdir() if x.is_file()]
        for file in files:
            if file.suffix.lower() in SONGS:
                target = self.path/"Songs"/file.name
                file.rename(target)

class Softwares(Manage):
    def __init__(self,path):
        super().__init__(path)

    def manage(self):
        files = [x for x in self.path.iterdir() if x.is_file()]
        for file in files:
            if file.suffix.lower() in SOFTWARES:
                target = self.path/"Softwares"/file.name
                file.rename(target)

class Games(Manage):
    def __init__(self,path):
        super().__init__(path)

    def manage(self):
        files = [x for x in self.path.iterdir() if x.is_file()]
        for file in files:
            if file.suffix.lower() in GAMES:
                target = self.path/"Games"/file.name
                file.rename(target)
if __name__ == "__main__":
    image = Image()
    image.manage()
