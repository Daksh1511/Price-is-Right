import time # using time module to reduce the pace of game by adding sleep function
import game # Module Made specially for this game


'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
'''Aryan's Part'''
formed_list_dict= list(game.Dictionary())
dict_item_value = formed_list_dict[1]
random_list_Items = formed_list_dict[0]

list_for_game_1 = random_list_Items[0:5]
list_for_game_2 = random_list_Items[5:10]
list_for_game_3 = random_list_Items[10:15]
#End of making list of keys in dictionary and selecting 15 random value from that list

'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''




# Start of Games Program

'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
'''Aryan's Part'''
# Game Number 1

# Main game compare orignal value with value we get by adding random error and assign points according to points system 
def Game_1(Point,k):
  
  Score = Point
  new_dict = {}
  for x in list_for_game_1:
    Price = dict_item_value[x]
    Updated_price = game.high_low_value(Price)
    new_dict.update({x:Updated_price})
    print(new_dict)
    Guessed_high_low = game.input_high_low()
    print(Guessed_high_low)
    
    
    if (Updated_price < Price and Guessed_high_low == "LOWER") or (Updated_price > Price and Guessed_high_low == "HIGHER"):
      
      print("Congragulation You guessed correctly")
      
      Score = game.Points_system(Score,k)
      k = k+1
      print('Your Current Score is : ',Score)
    
    else:
      
      k = 0 
      print("Sorry You didn't guessed correctly. The Price of ", x, 'is', Price)   
      print('Your Current Score is : ',Score)
    

    new_dict = {}
    time.sleep(1)

  return Score,k
# Return score and multiplicating factor
# End of Game 1 program
'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''


'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
'''Daksh's Part'''
# Game Number 2


# Compare input with correct option and assign points according to points system 
def Game_2(Point,k):
  Score = Point
  for x in list_for_game_2:
    Price = dict_item_value[x]
    print('Your item whose price you have to Guess is :', x )
    MCQ_option = game.option_maker(Price)
    print(MCQ_option)
    Guessed_option = game.Guess_option()

    if MCQ_option[Guessed_option] == Price:
      print("Congragulation You guessed correctly")
      
      Score = game.Points_system(Score,k)
      k = k+1
      print('Your Current Score is : ',Score)

      
    else:
      k = 0 
      print("Sorry You didn't guessed correctly. The Price of ", x, 'is', Price)   
      print('Your Current Score is : ',Score)

    time.sleep(1)
      
  return Score,k
# Return score and multiplicating factor
# End of Game 2 program
'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''


'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
'''Daksh's Part'''
# Game Number 3

# Main game were input should be betwwen orignal price ± error and assign points according to points system 
def Game_3(Point,k):
  
  Score = Point
  for x in list_for_game_3:
    Price = dict_item_value[x]
    highest_value = Price + game.limit(Price)
    lowest_value = Price - game.limit(Price)
    
    print('Your item whose price you have to Guess is :', x )
    price_guessed = game.Guess()

    if (price_guessed <= highest_value) and (price_guessed >= lowest_value) :
      print("Congragulation You guessed correctly")
      Score = game.Points_system(Score,k)
      k = k+1
      print('Your Current Score is : ',Score)

    else:
      k = 0 
      print("Sorry You didn't guessed correctly. The Price of ", x, 'is', Price)
      print('Your Current Score is : ',Score)
    
    time.sleep(1)

  return Score
# Return only score
# End of Game 3 program
# End of Games Program
'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''


'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
'''This Part is done with cumulative effort.'''
# Start of Game 
def Game():
    # Start of Game 1
    print("Get ready for the first game Higher or Lower")
    Path1 = game.path_game()
    if Path1 == 1:  # This if else block help to get rules or play the game
      fo = open("Game1_Rules.txt",mode="r")
      fo
      print(fo.read())
      fo.close()
      time.sleep(3)
      Game_1_result = Game_1(0,0)
      list_result_game1 = game.list_maker(Game_1_result)
      Game_1_score = list_result_game1[0]
      Game_1_multipication_factor = list_result_game1[1]
      game_score = list_result_game1[0]
      
    elif Path1 == 2:
      Game_1_result = Game_1(0,0)
      list_result_game1 = game.list_maker(Game_1_result)
      Game_1_score = list_result_game1[0]
      Game_1_multipication_factor = list_result_game1[1]
      game_score = list_result_game1[0]
    # End of Game 1

    # Start of Game 2
    if game_score >= 3000:  # This if else block help to know that if a player passed 1 level
        time.sleep(2)
        print("Congragulation You succed first level")
        print("Get ready for the second game Guess the Price from the given option")
        Path2 = game.path_game()
        if Path2 == 1:   # This if else block help to get rules or play the game
          fo = open("Game2_Rules.txt",mode="r")
          fo
          print(fo.read())
          fo.close()
          time.sleep(3)
          Game_2_result = Game_2(Game_1_score,Game_1_multipication_factor)
          list_result_game2 = game.list_maker(Game_2_result)
          Game_2_score = list_result_game2[0]
          Game_2_multipication_factor = list_result_game2[1]
          game_score = Game_2_score - game_score
        elif Path2 == 2:
          Game_2_result = Game_2(Game_1_score,Game_1_multipication_factor)
          list_result_game2 = game.list_maker(Game_2_result)
          Game_2_score = list_result_game2[0]
          Game_2_multipication_factor = list_result_game2[1]
          game_score = Game_2_score - game_score
        # End of Game 2

        # Start of Game 3
        if game_score >= 3000:  # This if else block help to know that if a player passed 2 level
            time.sleep(2)
            print("Congragulation You succed second level")
            print("Get ready for the third game Guess the price of object with limited error")
            Path3 = game.path_game()
            if Path3 == 1:
              fo = open("Game3_Rules.txt",mode="r")
              fo
              print(fo.read())
              fo.close()
              time.sleep(3)
              Game_3_result = Game_3(Game_2_score,Game_2_multipication_factor)
              game_score = Game_3_result - Game_2_score
            elif Path3 == 2:
              Game_3_result = Game_3(Game_2_score,Game_2_multipication_factor)
              game_score = Game_3_result - Game_2_score
            if game_score >= 3000:  # This if else block help to know that if a player passed 2 level
              print("Congralution you passed all the level ")
              return Game_3_result
            elif game_score < 3000:  # This if else block help to know that if a player passed 2 level
              print("Sorry you didn't pass the Third level, Better luck next time")
              return Game_3_result
            
        else:
            print("Sorry you didn't pass the Second level, Better luck next time")
            return Game_2_score
    else:
      print("Sorry you didn't pass the first level, Better luck next time")
      return Game_1_score
'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''

# End of Game 3
# End of Game 


'''This Part is done with cumulative effort.'''
'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
# This is main Game function combining all code in one function
def Begin():
  fo = open("Rules_Game.txt",mode="r")
  fo
  print(fo.read())
  fo.close()
  Path = game.path()
  if Path == 1:   # This if else block help to know about Point system or play the game
    fo = open("Points_System.txt",mode="r")
    fo
    print(fo.read())
    fo.close()
    time.sleep(3)
    Points = Game()
    
    Username = game.name_checker()
    # Starting of storing data
    game.add_entry_to_leaderboard(Username,Points)
    game.making_leaderboard()
    time.sleep(1)
    game.printer()
    print("Thanks for playing the game ,hope you enjoyed it.")

  elif Path == 2:  # This if else block help to know about Point system or play the game
    Points = Game()
    Username = game.name_checker()
    # Starting of storing data
    game.add_entry_to_leaderboard(Username,Points)
    game.making_leaderboard()
    time.sleep(1)
    game.printer()
    print("Thanks for playing the game ,hope you enjoyed it.")
# End of the code 
'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''


#This function will execute all the code
Begin()
