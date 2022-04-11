'''
This is module for all the function used in the game
'''

import random  # using random module too randomise the selection of items from sepcifice list and used to creat option value by randomizing error

items_opener = open("item_values.txt",mode="r")
leaderboard_opener_reader = open("leaderboard.txt",mode="r")
leaderboard_opener_editor = open("leaderboard.txt",mode="a")
finalleaderboard_opener_editor = open("finalleaderboard.txt",mode="w")
finalleaderboard_opener_reader = open("finalleaderboard.txt",mode="r")

'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
'''Aryan's Part'''
#Start of making dictionary using file handling
def Dictionary():
    items_opener = open("item_values.txt",mode="r")
    items_opener
    list_1 = []
    list_2 = []
    for lines in items_opener.readlines():    
        list_1.append(lines)

    for x in list_1:
        updated_list_1 = x.replace("\n","")
        list_2.append(updated_list_1)

    name_of_item = ''
    price_of_item = ''
    dict_item_value = {}

    for x in list_2:
        string = x
        name_of_item = ''
        price_of_item = ''
        cout = 0
        for y in string:
            if y == ':':
                cout += 1
            if cout == 0:
                name_of_item += y
            elif cout == 1:
                if y == ':':
                    pass
                else:
                    price_of_item += y
        dict_item_value[name_of_item] = int(price_of_item)

    items_opener.close()
    list_of_Items = []
    for x in dict_item_value.keys():
        list_of_Items.insert(1,x)
    random_list_Items = random.choices(list_of_Items,k=15)

    return random_list_Items,dict_item_value
#End of making dictionary
'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''


'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
'''Daksh's Part'''
# Points system
def Points_system(score,k):
  
  if k == 0:
    score = score + 1000
  else:
    score = score + 1000*(k+1)
    
  return score

# Converting data we get from each game to list 
def list_maker(tuple_1):
    list_formed = list(tuple_1)
    return list_formed


'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''


'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
'''Aryan's Part'''
# Game 1 imp function

# Function form value using random error with the help of random module 
def high_low_value(num):
  list_error = [-0.1,0.1,0.2,-0.2,0.05,-0.05,0.15,-0.15]
  random_error = random.choice(list_error)
  value = num + (num*random_error)
  return value

# To get input for high or low and then checking wheter user enter correct input if not it ask again till it get desired input 
def input_high_low():
  global checked
  high_low = {
      "H":"HIGHER",
      "L":"LOWER"
  }
  list_3 = ['H','L'] 
  Guess_high_low = str(input("Enter what do you think price shown should be higher or lower with respect to original price (Type 'H' or 'L'):")).upper()
  
  if Guess_high_low not in list_3:
    print("Please Type either 'H' or 'L'")
    input_high_low()
  else:
    checked = high_low[Guess_high_low]
  
  return checked

'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''


'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
'''Daksh's Part'''
# Game 2 imp function
# Option Maker
def option_maker(num):
  Option = {
      "A":0,
      "B":0,
      "C":0,
      "D":0
  }
  List_option = ["A","B","C","D"]
  random_option = random.choice(List_option) #select random option fro A,B,C or D and assign correct value to it
  
  Option[random_option] = num
  List_option.remove(random_option)
  list_error = [-0.1,0.1,0.2,-0.2,0.05,-0.05,0.15,-0.15]

  for x in List_option:
    random_error = random.choice(list_error)
    Option[x] = num + num*(random_error)
    # Assign value to other option by adding it with error

  return Option
# To get input for option and then checking wheter user enter correct input if not it ask again till it get desired input 

def Guess_option():
  guessed_option = str(input('Enter option You want to enter, Type either A,B,C or D:')).upper()
  if guessed_option not in ['A','B','C','D']:
    return Guess_option()
  else:
    return guessed_option

'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''


'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
'''Daksh's Part'''
# Game 3 imp function

# Take input for the game # using error Handling
def Guess():
  global y
  Guess_price = input("What should be price of this item:")
  try:
    y = int(Guess_price)
  except Exception as e:
    print(e,"You didn't entered integer, Please enter integer")
    Guess()
  finally:
    return y

# Find error
def limit(num):
  error = (num*0.1)
  return error

'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''


'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
'''Daksh's Part'''

# Start of Leadeboard
# Start of Name Checker
# This function will check is entered userename is present in the leader board if not it will return name or else it will ask to enter different name
def name_checker():
    Name = input("Enter Username:")
    list_name = []
    list_leaderboard = []
    leaderboard_opener_reader = open("leaderboard.txt",mode="r")
    leaderboard_opener_reader
    for line in leaderboard_opener_reader.readlines():
        list_leaderboard.append(line)
    
    for x in list_leaderboard:
        string = x
        cout = 0
        name_of_individual = ''
        for y in string:
            if y == '=':
                cout = 1
            if y == '\n':
              pass
            if cout == 0:
                name_of_individual += y
            elif cout == 1:
                pass
        list_name.append(name_of_individual)
    
    
    leaderboard_opener_reader.close()
    if Name not in list_name:
        return Name
        
    else:
        print("This username is already taken,Please enter different username.")
        return name_checker()
# End of Name Checker

#adding info to leaderboard and printing leader board
# This function will add username and score of that person in leaderboard
def add_entry_to_leaderboard(name,score):
  leaderboard_opener_editor = open("leaderboard.txt",mode="a")
  leaderboard_opener_editor
  text_to_display = name + '=' + str(score) + '\n'
  leaderboard_opener_editor.write(text_to_display)
  leaderboard_opener_editor.close()

# This function will help leaderboard to be sorted and reprint it in descending order of the score
def making_leaderboard():
    final_list=[]
    leaderboard_opener_reader = open("leaderboard.txt",mode="r")
    leaderboard_opener_reader
    for x in leaderboard_opener_reader.readlines():
      if x == '\n':
        pass
      else:
        tuple_name_score = ('','')
        tupled_list = list(tuple_name_score) 
        list_name_score = x.split('=')
        name = list_name_score[0]
        temp_score = list_name_score[1]
        score = int(temp_score[:-1])
        tupled_list[0] = name
        tupled_list[1] = score
        tuple_name_score = tuple(tupled_list)
        final_list.append(tuple_name_score)
        tuple_name_score = ('','')
        tupled_list = list(tuple_name_score) 
    score = lambda final_list: final_list[1]
    final_list.sort(key=score, reverse=True)
    

    leaderboard_opener_reader.close()
    finalleaderboard_opener_editor = open("finalleaderboard.txt", mode="w")
    finalleaderboard_opener_editor
    i = 1
    First_line = 'Leaderboard is as follow: ' + '\n'

    finalleaderboard_opener_editor.write(First_line)
    for x in final_list:
        new_list= list(x)
        What_to_type = str(i) + '. ' + new_list[0] + '=' + str(new_list[1]) + '\n'
        
        finalleaderboard_opener_editor.write(What_to_type)
        i += 1
    finalleaderboard_opener_editor.close()


# This function will help to type leaderboard
def printer():
    finalleaderboard_opener_reader = open("finalleaderboard.txt", mode="r")
    print(finalleaderboard_opener_reader.read())
    finalleaderboard_opener_reader.close()


'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''


'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
'''Aryan's Part'''

# This function will help to guess the path if user want to know the rule or directly play the game
def path_game():
  x = input("(press '1' to get info about rules of this game), (press '2' to start the Game) : ")
  if x == '1':
    return 1
  elif x == '2':
    return 2
  else:
    print("Type either 1 or 2")
    return path_game()
'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''


'''Aryan's Part'''
'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
# This function will help to guess the path if user want to know the Points System or directly play the game
def path():
  x = input("(press '1' to get info about points system), (press '2' to start the Game) : ")
  if x == '1':
    return 1
  elif x == '2':
    return 2
  else:
    print("Type either 1 or 2")
    return path()
'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''


