# import and acknowledge random, os, time, colorama data libraries
import random
import os as screen
import time as delay
import colorama
from colorama import Fore
# mandatory colorama acknowledgement
colorama

# set constants
LOGGED_IN = False

# main function
def menu():
  global LOGGED_IN
  screen.system("clear")
  print(Fore.WHITE + "\033[1mROULETTE LEGENDS\033[0m")
  print()
  if LOGGED_IN == True:
    print(f"Logged in as {usernameForMenu}")
    print()
    # menu GUI display
  else:
    pass
  print("1. Play Roulette")
  print("2. Create Account")
  print("3. Login")
  print("4. Check Balance")
  print("5. Store")
  print("6. Exit")
  print()
  menuInput = str(input("> "))
  if menuInput == str("1"):
    roulette()
  elif menuInput == str("2"):
    newAccount()
  elif menuInput == str("3"):
    login()
  elif menuInput == str("4"):
    checkBalance()
  elif menuInput == str("5"):
    store()
  elif menuInput == str("6"):
    print()
    print("Thank's for playing!")
    delay.sleep(3)
    screen.system("clear")
    
# account creation subroutine
def newAccount():
  global username
  screen.system("clear")
  print("\033[1mCREATE NEW ACCOUNT\033[0m")
  print()

  # write new end user data to file accounts.txt
  # note that a file is created named f"{username}.txt" - this file stores the user's in game currency values
  f = open("accounts.txt", "a")
  username = str(input("Username > "))
  userCredentials = {username: {"userID": "", "passhash": "", "coins": ""}}
  userCredentials[username]["passhash"] = str(input("Password > "))
  userCredentials[username]["userID"] = str(username)
  userCredentials[username]["coins"] = str("10000")
  f.write(str(userCredentials))
  f.write("\n")
  f.close()
  c = open(f"{username}.txt", "a+")
  c.write("1000")
  c.close()
  cash = open(f"{username}.cash", "a+")
  cash.write("0")
  cash.close()
  print()
  print("Account successfully created!")
  delay.sleep(1.5)
  menu()
  
# exsisting user login subroutine
def login():
  global LOGGED_IN
  global usernameForMenu
  screen.system("clear")
  print("\033[1mLOGIN\033[0m")
  print()
  # simple text parsing login system to identify if a given username and password are in accounts.txt
  with open("accounts.txt") as f:
    usernameInput = input("Username > ")
    passwordInput = input("Password > ")
    print()
    if usernameInput and passwordInput in f.read():
      print("Login Successful")
      usernameForMenu = str(usernameInput)
      LOGGED_IN = True
      delay.sleep(1.5)
      menu()
    else:
      print("Login Failed")
      delay.sleep(1.5)
      menu()
      
 # roulette game *menu* subroutine
def roulette():
  try:
    global won
    global betAmount
    global usernameForMenu
    won = int()
    # roulette menu
    screen.system("clear")
    f = open(f"{usernameForMenu}.txt", "r")
    balance = int(f.read())
    print("\033[1mPLACE A BET\033[0m")
    print()
    print(f"BALANCE: {balance} COINS")
    print()
    print("1. Red (2:1)")
    print("2. Black (2:1)")
    print("3. Even (2:1)")
    print("4. Odd (2:1)")
    print("5. Pick a dozen (3:1)")
    print("6. Pick a number (36:1)")
    print("7. Zero (36:1)")
    print("8. Menu")
    print()
    rouletteInput = str(input("> "))
  
    # analyze end user roulette menu input
    
    if rouletteInput == str("1"):
      screen.system("clear")
      print(Fore.RED + "\033[1mRED\033[0m")
      print()
      betAmountRaw = int(input("Bet amount > "))
      betAmount = round(betAmountRaw, 0)
      if betAmount > balance:
        print("You can't bet more coins than you have!")
        delay.sleep(2)
        roulette()
      else:
        pass
      winnings = betAmount * 2
      spin()
      print()
      if color == str("red"):
        print(f"You win {winnings} coins!")
        won = winnings

        f = open(f"{usernameForMenu}.txt", "r")
        coins = int(f.read())
        f.close()
        c = open(f"{usernameForMenu}.txt", "w")
        betCoins = coins - betAmount
        coinsNew = str(betCoins + won)
        c.write(coinsNew)
        c.close()
        
      else:
        print(f"You lose {betAmount} coins")
        print(f"You could have won {winnings} coins!")
        won = 0
        f = open(f"{usernameForMenu}.txt", "r")
        coins = int(f.read())
        f.close()
        c = open(f"{usernameForMenu}.txt", "w")
        betCoins = coins - betAmount
        coinsNew = str(betCoins + won)
        c.write(coinsNew)
        c.close()
      delay.sleep(3)
      roulette()
      
    elif rouletteInput == str("2"):
      screen.system("clear")
      print(Fore.YELLOW + "\033[1mBLACK\033[0m")
      print()
      betAmountRaw = int(input("Bet amount > "))
      betAmount = round(betAmountRaw, 0)
      if betAmount > balance:
        print("You can't bet more coins than you have!")
        delay.sleep(2)
        roulette()
      else:
        pass
      winnings = betAmount * 2
      spin()
      print()
      if color == str("black"):
        print(f"You win {winnings} coins!")
        won = winnings
        f = open(f"{usernameForMenu}.txt", "r")
        coins = int(f.read())
        f.close()
        c = open(f"{usernameForMenu}.txt", "w")
        betCoins = coins - betAmount
        coinsNew = str(betCoins + won)
        c.write(coinsNew)
        c.close()
      else:
        print(f"You lose {betAmount} coins")
        print(f"You could have won {winnings} coins!")
        won = 0
        f = open(f"{usernameForMenu}.txt", "r")
        coins = int(f.read())
        f.close()
        c = open(f"{usernameForMenu}.txt", "w")
        betCoins = coins - betAmount
        coinsNew = str(betCoins + won)
        c.write(coinsNew)
        c.close()
      delay.sleep(3)
      roulette()
      
    elif rouletteInput == str("3"):
      screen.system("clear")
      print("\033[1mEVEN\033[0m")
      print()
      betAmountRaw = int(input("Bet amount > "))
      betAmount = round(betAmountRaw, 0)
      if betAmount > balance:
        print("You can't bet more coins than you have!")
        delay.sleep(2)
        roulette()
      else:
        pass
      winnings = betAmount * 2
      spin()
      print()
      if even == str("even"):
        print(f"You win {winnings} coins!")
        won = winnings
        f = open(f"{usernameForMenu}.txt", "r")
        coins = int(f.read())
        f.close()
        c = open(f"{usernameForMenu}.txt", "w")
        betCoins = coins - betAmount
        coinsNew = str(betCoins + won)
        c.write(coinsNew)
        c.close()
      else:
        print(f"You lose {betAmount} coins")
        print(f"You could have won {winnings} coins!")
        won = 0
        f = open(f"{usernameForMenu}.txt", "r")
        coins = int(f.read())
        f.close()
        c = open(f"{usernameForMenu}.txt", "w")
        betCoins = coins - betAmount
        coinsNew = str(betCoins + won)
        c.write(coinsNew)
        c.close()
      delay.sleep(3)
      roulette()
      
    elif rouletteInput == str("4"):
      screen.system("clear")
      print("\033[1mODD\033[0m")
      print()
      betAmountRaw = int(input("Bet amount > "))
      betAmount = round(betAmountRaw, 0)
      if betAmount > balance:
        print("You can't bet more coins than you have!")
        delay.sleep(2)
        roulette()
      else:
        pass
      winnings = betAmount * 2
      spin()
      print()
      if even == str("odd"):
        print(f"You win {winnings} coins!")
        won = winnings
        f = open(f"{usernameForMenu}.txt", "r")
        coins = int(f.read())
        f.close()
        c = open(f"{usernameForMenu}.txt", "w")
        betCoins = coins - betAmount
        coinsNew = str(betCoins + won)
        c.write(coinsNew)
        c.close()
      else:
        print(f"You lose {betAmount} coins")
        print(f"You could have won {winnings} coins!")
        won = 0
        f = open(f"{usernameForMenu}.txt", "r")
        coins = int(f.read())
        f.close()
        c = open(f"{usernameForMenu}.txt", "w")
        betCoins = coins - betAmount
        coinsNew = str(betCoins + won)
        c.write(coinsNew)
        c.close()
      delay.sleep(3)
      roulette()
      
    elif rouletteInput == str("5"):
      screen.system("clear")
      print("\033[1mPICK A DOZEN\033[0m")
      print()
      print("1. 1-12")
      print("2. 13-24")
      print("3. 25-36")
      print()
      dozenInput = str(input("> "))
      
      if dozenInput == str("1"):
        screen.system("clear")
        print("\033[1mFIRST DOZEN\033[0m")
        print()
        betAmountRaw = int(input("Bet amount > "))
        betAmount = round(betAmountRaw, 0)
        if betAmount > balance:
          print("You can't bet more coins than you have!")
          delay.sleep(2)
          roulette()
        else:
          pass
        winnings = betAmount * 3
        spin()
        print()
        if dozen == str("1-12"):
          print(f"You win {winnings} coins!")
          won = winnings
          f = open(f"{usernameForMenu}.txt", "r")
          coins = int(f.read())
          f.close()
          c = open(f"{usernameForMenu}.txt", "w")
          betCoins = coins - betAmount
          coinsNew = str(betCoins + won)
          c.write(coinsNew)
          c.close()
        else:
          print(f"You lose {betAmount} coins")
          print(f"You could have won {winnings} coins!")
          won = 0
          f = open(f"{usernameForMenu}.txt", "r")
          coins = int(f.read())
          f.close()
          c = open(f"{usernameForMenu}.txt", "w")
          betCoins = coins - betAmount
          coinsNew = str(betCoins + won)
          c.write(coinsNew)
          c.close()
        delay.sleep(3)
        roulette()
          
      elif dozenInput == str("2"):
        screen.system("clear")
        print("\033[1mSECOND DOZEN\033[0m")
        print()
        betAmountRaw = int(input("Bet amount > "))
        betAmount = round(betAmountRaw, 0)
        if betAmount > balance:
          print("You can't bet more coins than you have!")
          delay.sleep(2)
          roulette()
        else:
          pass
        winnings = betAmount * 3
        spin()
        print()
        if dozen == str("13-24"):
          print(f"You win {winnings} coins!")
          won = winnings
          f = open(f"{usernameForMenu}.txt", "r")
          coins = int(f.read())
          f.close()
          c = open(f"{usernameForMenu}.txt", "w")
          betCoins = coins - betAmount
          coinsNew = str(betCoins + won)
          c.write(coinsNew)
          c.close()
        else:
          print(f"You lose {betAmount} coins")
          print(f"You could have won {winnings} coins!")
          won = 0
          f = open(f"{usernameForMenu}.txt", "r")
          coins = int(f.read())
          f.close()
          c = open(f"{usernameForMenu}.txt", "w")
          betCoins = coins - betAmount
          coinsNew = str(betCoins + won)
          c.write(coinsNew)
          c.close()
        delay.sleep(3)
        roulette()
          
      elif dozenInput == str("3"):
        screen.system("clear")
        print("\033[1mTHIRD DOZEN\033[0m")
        print()
        betAmountRaw = int(input("Bet amount > "))
        betAmount = round(betAmountRaw, 0)
        if betAmount > balance:
          print("You can't bet more coins than you have!")
          delay.sleep(2)
          roulette()
        else:
          pass
        winnings = betAmount * 3
        spin()
        print()
        if dozen == str("25-36"):
          print(f"You win {winnings} coins!")
          won = winnings
          f = open(f"{usernameForMenu}.txt", "r")
          coins = int(f.read())
          f.close()
          c = open(f"{usernameForMenu}.txt", "w")
          betCoins = coins - betAmount
          coinsNew = str(betCoins + won)
          c.write(coinsNew)
          c.close()
        else:
          print(f"You lose {betAmount} coins")
          print(f"You could have won {winnings} coins!")
          won = 0
          f = open(f"{usernameForMenu}.txt", "r")
          coins = int(f.read())
          f.close()
          c = open(f"{usernameForMenu}.txt", "w")
          betCoins = coins - betAmount
          coinsNew = str(betCoins + won)
          c.write(coinsNew)
          c.close()
        delay.sleep(3)
        roulette()
      else:
        pass
      
    elif rouletteInput == str("6"):
      screen.system("clear")
      print(Fore.BLUE + "\033[1mPICK A NUMBER\033[0m")
      print()
      numberInput = str(input("What number > "))
      print()
      betAmountRaw = int(input("Bet amount > "))
      betAmount = round(betAmountRaw, 0)
      if betAmount > balance:
        print("You can't bet more coins than you have!")
        delay.sleep(2)
        roulette()
      else:
        pass
      winnings = betAmount * 36
      spin()
      print()
      if number == numberInput:
        print(Fore.RED + "\033[1mMASSIVE WIN!\033[0m")
        print(f"You win {winnings} coins!")
        won = winnings
        f = open(f"{usernameForMenu}.txt", "r")
        coins = int(f.read())
        f.close()
        c = open(f"{usernameForMenu}.txt", "w")
        betCoins = coins - betAmount
        coinsNew = str(betCoins + won)
        c.write(coinsNew)
        c.close()
      else:
        print(f"You lose {betAmount} coins")
        print(f"You could have won {winnings} coins!")
        won = 0
        f = open(f"{usernameForMenu}.txt", "r")
        coins = int(f.read())
        f.close()
        c = open(f"{usernameForMenu}.txt", "w")
        betCoins = coins - betAmount
        coinsNew = str(betCoins + won)
        c.write(coinsNew)
        c.close()
      delay.sleep(3)
      roulette()
        
    elif rouletteInput == str("7"):
      screen.system("clear")
      print(Fore.GREEN + "\033[1mZERO\033[0m")
      print()
      betAmountRaw = int(input("Bet amount > "))
      betAmount = round(betAmountRaw, 0)
      if betAmount > balance:
        print("You can't bet more coins than you have!")
        delay.sleep(2)
        roulette()
      else:
        pass
      winnings = betAmount * 36
      spin()
      print()
      if number == 0:
        print("\033[1mMASSIVE WIN!\033[0m")
        print(f"You win {winnings} coins!")
        won = winnings
        f = open(f"{usernameForMenu}.txt", "r")
        coins = int(f.read())
        f.close()
        c = open(f"{usernameForMenu}.txt", "w")
        betCoins = coins - betAmount
        coinsNew = str(betCoins + won)
        c.write(coinsNew)
        c.close()
      else:
        print(f"You lose {betAmount} coins")
        print(f"You could have won {winnings} coins!")
        won = 0
        f = open(f"{usernameForMenu}.txt", "r")
        coins = int(f.read())
        f.close()
        c = open(f"{usernameForMenu}.txt", "w")
        betCoins = coins - betAmount
        coinsNew = str(betCoins + won)
        c.write(coinsNew)
        c.close()
      delay.sleep(3)
      roulette()
      
    elif rouletteInput == str("8"):
      menu()
      
   # developer mode option for devs to see traceback and .err variables for debugging
  except Exception as err:
    print("ERROR: You either:")
    print()
    var1 = str("n")
    while var1 == str("n"):
      print("1. Tried to bet more than you had in coins balance")
      print("2. Tried to play roulette without logging in")
      print()
      print("3. Developer Mode")
      z = str(input("> "))
      if z == str("1") or z == str("2"):
        var1 = str("y")
        menu()
      elif z == str("3"):
        screen.system("clear")
        print("\033[1mDEVELOPER MODE\033[0m")
        print()
        password = str(input("Encoding Hash > "))
        if password == str("0"):
          screen.system("clear")
          print(f"Error encountered from user {usernameForMenu}.")
          print()
          print(err)
          print()
          menuBoolean = str(input("Menu? "))
          if menuBoolean == str("y") or menuBoolean == str("Y") or menuBoolean == str("yes"):
            menu()
          else:
            menu()
        else:
          screen.system("clear")
          print("Incorrect password.")
          print()
          print("Returning to main menu...")
          delay.sleep(2)
          menu()
      else:
        print("Invalid response.")
        delay.sleep(2)
        screen.system("clear")
        
# this is the actual game engine for random number generation
# spin() also includes the function that determines whether a number is black or red (line 593 >>)
def spin():
  global usernameForMenu
  global betAmount
  global even
  global number
  global color
  global dozen
  print()
  print("Spinning...")
  # number generation and analysis
  number = random.randint(0,36)
  group = int()
  if number != 0:
    if number <= 10:
      group = 1
    elif number >= 19 and number <= 28:
      group = 1
    else:
      group = 2
  elif number == 0:
    group = 3
  else:
    pass

  even = str()
  if (number % 2) == 0:
    even = ("even")
  else:
    even = ("odd")

  color = str()
  if group == 1:
    if (number % 2) == 0:
      color = str("red")
    else:
      color = str("black")
  elif group == 2:
    if (number % 2) == 0:
      color = str("black")
    else:
      color = str("red")
  elif group == 3:
    color = str("green")

  dozen = str()
  if number != 0:
    if number >= 1 and number <= 12:
      dozen = str("1-12")
    elif number >= 13 and number <= 24:
      dozen = str("13-24")
    elif number >= 25 and number <= 36:
      dozen = str("25-36")
    else:  
      pass
  elif number == 0:
    dozen = str("0")
  else:
    pass

  # print number to end user
  delay.sleep(3)
  if color == str("black"):
    print()
    print(Fore.YELLOW + f"\033[1m{number}\033[0m")
  elif color == str("red"):
    print()
    print(Fore.RED + f"\033[1m{number}\033[0m")
  elif color == str("green"):
    print()
    print(Fore.GREEN + f"\033[1m{number}\033[0m")
  delay.sleep(1)
  
# function to check the balance of *any user* (not just the active signed in user) without an end user password available
def checkBalance():
  screen.system("clear")
  print("\033[1mCHECK BALANCE\033[0m")
  print()
  username1 = input("Username > ")
  try:
  # this code reads from a file and gives the end user an error message if the username that they enter is not present
  # this is because of consistent crashing when the user enters a username that does not exist (traceback >> file)
    f = open(f"{username1}.txt", "r")
    screen.system("clear")
    print("\033[1mCURRENT BALANCE\033[0m")
    print()
    coins = str(f.read())
    f.close()
    cashFile = open(f"{username1}.cash", "r")
    cash = str(cashFile.read())
    print(Fore.YELLOW + f"{coins} Coins")
    print(Fore.GREEN + f"{cash} Cash")
  except:
    print()
    print("That username does not exist!")
    print()
    print("Returning to main menu...")
  delay.sleep(3)
  menu()
    # store I might add in the future
def store():
  print("Store coming soon! Check back later!")
  delay.sleep(3)
  menu()
  
menu()
