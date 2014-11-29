from sys import exit
from random import randint


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
        

# a class that makes various pokemons!
class Pokemon():
	# the first argument __init__ () gets is used to refer to the
	# instance object
	def __init__(self, pokemon_name, trainer_name, level, HP, moves):
        self.pokemon_name = pokemon_name
        self.trainer_name = trainer_name
		self.level = level
		self.HP = HP
        self.moves = moves
        
    def __repr__(self):
      	return self.pokemon_name
        
	# lets player know pokemon stats
	def description(self):
		print "%s's pokemon is a %s that is level %s and has %s HP" % (
		self.trainer_name, self.pokemon_name, self.level, self.HP)
        return self
        
	def Trainer_Challenge(self):
		print "\nTrainer %s challenges you to a batttle." % (self.trainer_name)
		print "%s sends out %s" % (self.trainer_name, self.pokemon_name)
		print " "
        return self
    
   	def update_HP(self, new_HP):
      	self.HP = new_HP
        return self
        
	def attack(self, target):
		damage = randint(1, 25)
        new_HP = target.HP - damage
		target.update_HP(new_HP)
		return self

      
class Battle():
	def __init__(self, pokemon1, pokemon2):
		self.pokemon1 = pokemon1
		self.pokemon2 = pokemon2
        
	def first_strike (self):
		random_int = randint(0, 10)
		if random_int < 5:
			print "%s goes first!" % self.pokemon1
		else:
			print "%s goes first!" % self.pokemon2

      
# set My_Pokemon to an instance of class Pokemon
bulbasaurs_moves = Moves("Bulbasaur", "Razor Blade", "Vine Whip", "Solar Beam", "Scratch")
My_Pokemon =  Pokemon("Bulbasaur", "Ashley", 15, 100, bulbasaurs_moves)
My_Pokemon.description()
print(My_Pokemon)

gyradosz_moves = Moves("Gyarados", "Dragon Rage", "Twister", "Bite", "Hydro Pump")
Trainer_Pokemon = Pokemon("Gyarados", "Esteban", 13, 80, gyradosz_moves)
Trainer_Pokemon.description()

# from My_Pokemon get 
Trainer_Pokemon.Trainer_Challenge()


Pokemon_in_Battle = Battle(My_Pokemon, Trainer_Pokemon)
Pokemon_in_Battle.first_strike()