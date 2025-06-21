class file:       
    def __enter__(self):
        self.file = open("mcu.txt", "w")
        return self.file

    def __exit__(self, *args):
        self.file.close()

with file() as f:
    f.write("file handed safely")