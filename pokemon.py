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
    # the first argument __init__() gets is used to refer to the
    # instance object
    def __init__(self, pokemon_name, trainer_name, level, HP, moves):
        self.pokemon_name = pokemon_name
        self.trainer_name = trainer_name
        self.level = level
        self.HP = HP
        self.moves = moves
        
    # returns a printable representation of the object
    def __repr__(self):
        return self.pokemon_name
        
    # lets player know pokemon stats
    def description(self):
        print "%s's pokemon is a %s that is level %s and has %s HP" % (
        self.trainer_name, self.pokemon_name, self.level, self.HP)
        return self
        
    def Trainer_Challenge(self):
        # print "\nTrainer %s challenges you to a batttle." % (self.trainer_name)
        print "%s sends out %s" % (self.trainer_name, self.pokemon_name)
        return self
    
    def update_HP(self, new_HP):
        self.HP = new_HP
        return self
        
    def attack(self, target):
        damage = randint(1, 25)
        new_HP = target.HP - damage
        target.update_HP(new_HP)
        return self

      
bulbasaurs_moves = Moves("Bulbasaur", "Razor Leaf", "Vine Whip", "Solar Beam", "Scratch")
My_Pokemon =  Pokemon("Bulbasaur", "Ashley", 15, 100, bulbasaurs_moves)
My_Pokemon.description()

# print(My_Pokemon) prints 'Bulbasaur'
gyradosz_moves = Moves("Gyarados", "Dragon Rage", "Twister", "Bite", "Hydro Pump")
Trainer_Pokemon = Pokemon("Gyarados", "Esteban", 13, 80, gyradosz_moves)
Trainer_Pokemon.description()

class Battle():
    def __init__(self, pokemon1, pokemon2):
        self.pokemon1 = pokemon1
        self.pokemon2 = pokemon2
        
    def first_strike (self):
        random_int = randint(0, 10)
        if random_int < 5:
            print "%s goes first!" % self.pokemon1
            if self.pokemon1 == My_Pokemon:
                print "What move would you like to use?"
                print bulbasaurs_moves.move_set()
                choice = int(raw_input("> "))
                if choice == 1:
                    print "Bulbasaur used Razor Leaf"
                elif choice == 2:
                    print "Bulbasaur used Vine Whip"
                elif choice == 3:
                    print "Bulbasaur used Solar Beam"
                elif choice == 4:
                    print "Bulbasaur used Scratch"
        else:
            random_int = randint(1, 20)
            if random_int <= 5:
                print "%s uses %s" % (self.pokemon2.Moves.move1)
            if ((random_int >=6) & (random_int <= 10)):
                print "%s uses %s" % (self.pokemon2.Moves.move2)
            if ((random_int >=11) & (random_int <= 15)):
                print "%s uses %s" % (self.pokemon2.Moves.move3)
            if ((random_int >=16) & (random_int <= 20)):
                print "%s uses %s" % (self.pokemon2.Moves.move4)
      

# from My_Pokemon get 
Trainer_Pokemon.Trainer_Challenge()
My_Pokemon.Trainer_Challenge()

# will take the first arguments from My_Pokemon and Trainer_Pokemon
Pokemon_in_Battle = Battle(My_Pokemon, Trainer_Pokemon)
Pokemon_in_Battle.first_strike()






