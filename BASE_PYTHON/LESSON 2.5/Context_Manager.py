    import random
import datetime

class filecreator:
	def __init__(self, path):
		self.path = path
		self.create_time = datetime.datetime.now()
		print('время запусука', self.create_time)

	def __enter__(self):
	    self.file = open(self.path,"w", encoding="utf-8")
	    return self.file

	def __exit__(self, exc_type, exc_val, exc_tb):
		self.file.close()
		self.end_time = datetime.datetime.now()
		print('время окончания',self.end_time)
		print("время работы", self.end_time - self.create_time)

if __name__ == "__main__":
	with filecreator("random.txt") as file:
		for i in range(1000000):
			towrite = str(random.randint(1,100))
			file.write(f'{towrite}\n')
