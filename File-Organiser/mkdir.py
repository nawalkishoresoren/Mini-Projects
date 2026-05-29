from pathlib import Path
from config import*
import shutil

class Directory_API:
    def __init__(self,path):
        self.path = path

    def list_directories(self):
        list_of_directories = [x for x in self.path.iterdir() if x.is_dir()]
        return list_of_directories
        
            
    def make_directories(self):
        existing_directories = {d.name for d in self.list_directories()}
        created = []
        for directory_name in DIRECTORIES:
            if directory_name not in existing_directories:
                target = self.path / directory_name
                target.mkdir(exist_ok=True)
                created.append(directory_name)
        return created

def main():
    path = Path.home()/"Downloads"
    directory = Directory_API(path)
    #List directories
    print("List of Directories = ",directory.list_directories())
    #Make necessary directories
    print("Making necessary Directories",directory.make_directories())


if __name__ == "__main__":
    main()

        
