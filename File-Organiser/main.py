from pathlib import Path
from categorise import*
class Organiser:
    def __init__(self,file_type_object:Manage):
        self.file_type_object = file_type_object
    
    def run(self):
        self.file_type_object.manage()
    

if __name__ == "__main__":
    path = Path.home() / "Downloads"
    stroftwares = Softwares(path)
    app = Organiser(stroftwares)
    app.run()

