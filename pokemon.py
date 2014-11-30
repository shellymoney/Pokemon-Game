from sys import exit
from random import randint

class Moves():
    def __init__(self, move1, move2, move3, move4):
        self.move1 = move1
        self.move2 = move2
        self.move3 = move3
        self.move4 = move4
    
    def __repr__(self):
#       moves_list = "1. %s\n 2. %s\n " % ()
#       moves_list = [self.move1, self.move2, self.move3, self.move4]
        printable_moves = ""
#       for item, move in enumerate(moves_list, start=1):
#               printable_moves += "%d. %s\n" % (item, move)
        printable_moves += "\t1. %s\n" % self.move1
        printable_moves += "\t2. %s\n" % self.move2
        printable_moves += "\t3. %s\n" % self.move3
        printable_moves += "\t4. %s\n" % self.move4
        return printable_moves

# a class that makes various pokemons!
class Pokemon():
    # the first argument __init__() gets is used to refer to the
    # instance object
    def __init__(self, pokemon_name, trainer_name, level, HP, poke_moves):
        self.pokemon_name = pokemon_name
        self.trainer_name = trainer_name
        self.level = level
        self.HP = HP
        self.poke_moves = poke_moves
#         print(self.poke_moves)
        
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
        print "%s's new HP is %d" % (target, target.HP) # target.HP = new_HP
        return self

      
bulbasaurs_moves = Moves("Razor Leaf", "Vine Whip", "Solar Beam", "Scratch")
My_Pokemon =  Pokemon("Bulbasaur", "Ashley", 15, 100, bulbasaurs_moves)
My_Pokemon.description()

# print(My_Pokemon) prints 'Bulbasaur'
gyradosz_moves = Moves("Dragon Rage", "Twister", "Bite", "Hydro Pump")
Trainer_Pokemon = Pokemon("Gyarados", "Esteban", 15, 100, gyradosz_moves)
Trainer_Pokemon.description()

class Battle():
    def __init__(self, pokemon1, pokemon2):
        self.pokemon1 = pokemon1
        self.pokemon2 = pokemon2
        
    def first_strike (self):
        random_int = randint(0, 10)
        if random_int < 5:
            print "\n%s goes first!" % self.pokemon1
            return self.pokemon1
        else:
            print "\n%s goes first!" % self.pokemon2
            return self.pokemon2
            
    def Pokemon_Battle(self, next_pokemon):
            if next_pokemon == My_Pokemon:
                print "What move would you like to use?\n"
                print(self.pokemon1.poke_moves)
#               print bulbasaurs_moves.move_set()
                choice = int(raw_input("> "))
                if choice == 1:
                    print "%s used %s" % (self.pokemon1, self.pokemon1.poke_moves.move1)
                    self.pokemon1.attack(self.pokemon2)
                elif choice == 2:
                    print "%s used %s" % (self.pokemon1, self.pokemon1.poke_moves.move2)
                    self.pokemon1.attack(self.pokemon2)
                elif choice == 3:
                    print "%s used %s" % (self.pokemon1, self.pokemon1.poke_moves.move3)
                    self.pokemon1.attack(self.pokemon2)
                elif choice == 4:
                    print "%s used %s" % (self.pokemon1, self.pokemon1.poke_moves.move4)
                    self.pokemon1.attack(self.pokemon2)
            else:
                random_int = randint(1, 20)
                if random_int <= 5:
                    print "%s uses %s" % (self.pokemon2, self.pokemon2.poke_moves.move1)
                    self.pokemon2.attack(self.pokemon1)
                if ((random_int >=6) & (random_int <= 10)):
                    print "%s uses %s" % (self.pokemon2, self.pokemon2.poke_moves.move2)
                    self.pokemon2.attack(self.pokemon1)
                if ((random_int >=11) & (random_int <= 15)):
                    print "%s uses %s" % (self.pokemon2, self.pokemon2.poke_moves.move3)
                    self.pokemon2.attack(self.pokemon1)
                if ((random_int >=16) & (random_int <= 20)):
                    print "%s uses %s" % (self.pokemon2, self.pokemon2.poke_moves.move4)
                    self.pokemon2.attack(self.pokemon1)
      

Trainer_Pokemon.Trainer_Challenge()
My_Pokemon.Trainer_Challenge()

# will take the first arguments from My_Pokemon and Trainer_Pokemon
Pokemon_in_Battle = Battle(My_Pokemon, Trainer_Pokemon)
Next_Pokemon = Pokemon_in_Battle.first_strike()
Pokemon_Battle(Next_Pokemon)
