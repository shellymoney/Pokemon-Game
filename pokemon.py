from sys import exit
from random import randint
# a class that makes various pokemon!
class Pokemon():
	# the first argument __init__ () gets is used to refer to the
	# instance object
	def __init__(self, trainer_name, pokemon_name, level, base_hp):
		self.trainer_name = trainer_name
		self.pokemon_name = pokemon_name
		self.level = level
		self.base_hp = base_hp
	# lets player know pokemon stats
	def description(self):
		print "%s's pokemon is a %s that is level %s and has %s HP" % (
		self.trainer_name, self.pokemon_name, self.level, self.base_hp)
	def Trainer_Challenge(self):
		print "\nTrainer %s challenges you to a batttle." % (self.trainer_name)
		print "%s sends out %s" % (self.trainer_name, self.pokemon_name)
		print " "
# set My_Pokemon to an instance of class Pokemon
My_Pokemon =  Pokemon("Ashley", "Bulbasaur", "15", 100)
My_Pokemon.description()
Trainer_Pokemon = Pokemon("Esteban", "Gyarados", "13", 80)
Trainer_Pokemon.description()
# from My_Pokemon get 
Trainer_Pokemon.Trainer_Challenge()
class Moves():
	def __init__(self, poke_name, move1, move2, move3, move4):
		self.poke_name = poke_name
		self.move1 = move1
		self.move2 = move2
		self.move3 = move3
		self.move4 = move4
	def move_set(self):
		print "%s's moves: " % self.poke_name
		print "1. %s " % self.move1
		print "2. %s" % self.move2
		print "3. %s" % self.move3
		print "4. %s\n" % self.move4
	def random_move(self):
		random_int = randint(1, 20)
		if random_int <= 5:
			print "%s uses %s" % (self.poke_name, self.move1)
		if (random_int >=6 || random_int <= 10):
			print "%s uses %s" % (self.poke_name, self.move2)
		if (random_int >=11 || random_int <= 15):
			print "%s uses %s" % (self.poke_name, self.move3)
		if (random_int >=16 || random_int <= 20):
			print "%s uses %s" % (self.poke_name, self.move4)
Bulbasaur = Moves("Bulbasaur", "Razor Blade", "Vine Whip", "Solar Beam", "Scratch")
Bulbasaur.move_set()
Gyarados = Moves("Gyarados", "Dragon Rage", "Twister", "Bite", "Hydro Pump")
Gyarados.move_set()
class Battle():
	def __init__(self, pokemon1, pokemon2):
		self.pokemon1 = pokemon1
		self.pokemon2 = pokemon2
	def first_strike (self):
		random_int = randint(0, 10)
		if random_int < 5:
			print "%s goes first!" % self.pokemon1
		else:
			print "%s goes first" % self.pokemon2
Pokemon_in_Battle = Battle("Bulbasaur", "Gyarados")
Pokemon_in_Battle.first_strike()