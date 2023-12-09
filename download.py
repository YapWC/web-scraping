from abc import ABC


class Data(ABC):
    def __init__(self, data, file_name) -> None:
       self.data = data
       self.file_name = file_name
    
    def download(self):
       raise NotImplementedError("Subclass must implement abstract method")

class BinaryData(Data):
    def __init__(self, data, file_name) -> None:
        super().__init__(data, file_name)

    def download(self, to_folder="./"):
        with open(to_folder+self.file_name, "wb") as f:
            f.write(self.data)
        f.close()

class TextData(Data):
    def __init__(self, data, file_name) -> None:
        super().__init__(data, file_name)
    
    def download(self, to_folder="./"):
        with open(to_folder+self.file_name, "w") as f:
            f.write(self.data)
        f.close()
