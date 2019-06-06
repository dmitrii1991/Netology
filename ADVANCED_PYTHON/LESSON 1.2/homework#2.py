import hashlib, os, json

class Hashlib_code:
    def __init__(self, path):
        self.path = path
        self.file = open(r'{}'.format(path), "r", encoding='utf-8')
        self.line = self.file.readline()

    def __iter__(self):
        return self

    def __next__(self):
        hesh = hashlib.md5(bytes(self.line, encoding = 'utf-8')).hexdigest()
        self.line = self.file.readline()
        if self.line == self.file.readline():
            raise StopIteration
        else:
            self.line = self.file.readline()
            return hesh
