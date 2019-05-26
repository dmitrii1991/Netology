eggs = 0
all_milk = 0
all_wool =0
weight_all = 0
weightest = ""
max_weight = 0

class Goose:
  satiety = "голоден"
  bollocks = 2
  voice = "Крякря"

  def __init__ (self, name, weight):
    self.name = name
    self.weight = weight
  def eat(self):
    self.satiety = "Сыт"
  def egg (self):
    global eggs
    eggs += self.bollocks
    self.bollocks = 0
  def voices (self):
    print(self.name, " says ", self.voice)

class Cow:
  satiety = "Жгучий голод"
  milk = 30
  voice = "МУМУ"

  def __init__ (self, name, weight):
    self.name = name
    self.weight = weight
  def eat(self):
    self.satiety = "пузя полно"
  def get_milk (self):
    global all_milk
    all_milk += self.milk
    self.milk = 0
  def voices (self):
    print(self.name, " says ", self.voice)
class Sheep:
  satiety = "Пустое брюхо"
  wool = 25
  voice = "БЕБЕ"

  def __init__ (self, name, weight):
    self.name = name
    self.weight = weight
  def eat(self):
    self.satiety = "Обездвижен от сытости"
  def get_wool (self):
    global all_wool
    all_wool += self.wool
    self.wool = 0
  def voice (self):
    print(self.name, " says ", self.voice)


class Chicken:
  satiety = "Голодно"
  bollocks = 10
  voice = "Кoko"

  def __init__ (self, name, weight):
    self.name = name
    self.weight = weight
  def eat(self):
   self.satiety = "Сытость"
  def egg (self):
    global eggs
    eggs += self.bollocks
    self.bollocks = 0
  def voice(self):
    print(self.name, " says ", self.voice)

class Goat:
  satiety = 'Голодная смерть близка!'
  milk = 150
  voice = "МУМУ"

  def __init__(self, name, weight):
    self.name = name
    self.weight = weight
  def eat(self):
    self.satiety = 'Смерть от обжорства близка!'
  def get_milk (self):
    global all_milk
    all_milk += self.milk
    self.milk = 0
  def voice (self):
    print(self.name, " says ", self.voice)

class Duck:
  satiety = "голод"
  bollocks = 6
  voice = "Крякря"

  def __init__ (self, name, weight):
    self.name = name
    self.weight = weight
  def eat(self):
    self.satiety = "Сытость"
  def egg (self):
    global eggs
    eggs += self.bollocks
    self.bollocks = 0
  def voice (self):
    print(self.name, " says ", self.voice)


grey = Goose('Серый', 2)
white = Goose('Белый', 3)

man = Cow('Манька', 300)

bar = Sheep('Барашек', 125)
kud = Sheep('Кудрявый',145)

koko = Chicken('КОКО', 1)
kyr = Chicken('кукареку', 2)

roga = Goat('Рога', 65)
kop = Goat('Копыта', 55)

kry = Duck('Кряква', 1)

animals = [grey, white, man,bar, kud, koko, kyr, roga, kop, kry]

for animal in animals:
  weight_all += animal.weight
  if max_weight < animal.weight:
    weightest = animal.name
    max_weight = animal.weight


print('общая масса ', weight_all)
print('тяжеловес ', weightest, 'весом',  max_weight)
