##Simple Music Game##
 
import random
import time
from colorama import Fore
x = 0
 
print("""
  _____                      _____                      
 /  ___|                    |  __ \                     
 \ `--.  ___  _ __   __ _   | |  \/ __ _ _ __ ___   ___ 
  `--. \/ _ \| '_ \ / _` |  | | __ / _` | '_ ` _ \ / _ \
 /\__/ / (_) | | | | (_| |  | |_\ \ (_| | | | | | |  __/
 \____/ \___/|_| |_|\__, |  \____/\__,_|_| |_| |_|\___|
                     __/ |                            
                    |___/                              """)
 
#Ask's for the username and password
Auth = str(input("What is your username and password?"))
 
#if the user puts PUT YOUR PASSWORD HERE as the username and password it will grant them access to the game
if Auth == "PUT YOUR PASSWORD HERE":
    print(Fore.GREEN + 'Access Granted')
    print('\033[39m')
 
#If the username isnt PUT YOUR PASSWORD HERE it will close the program
elif Auth != "PUT YOUR PASSWORD HERE":
    print(Fore.RED + "Password or Username Is Wrong")
    print("Program will close now")
    exit()
 
#Creating a score 
score = 0
 
#Reading song names and artist from the file
read = open("skunk.txt", "r")
skunk = read.readlines()
songlist = []
 
#Removing the 'new line' code
for i in range(len(skunk)):
    songlist.append(skunk[i].strip('\n'))
  
while x == 0:
    #Randomly choosing a song and artist from the list
    choice = random.choice(songlist)
    artist, song = choice.split('-')
 
    #Splitting the song into the first letters of each word
    skunk = song.split()
    letters = [word[0] for word in skunk]
 
    #Loop for guessing the answer in red using colorama package
    for x in range(0,2):
        print(artist, "".join(letters))
        guess = str(input("Guess the song!"))
        print('\033[37m')
        if guess == song:
            if x == 0:
                score = score + 3
                break
            if x == 1:
                score = score + 1
                break
 
    #This will print the score in blue
    print(Fore.BLUE + "Your score is", score)
    print("Get ready for the next question!")
    print('\033[37m')
    time.sleep(2)
 
leaderboard = open("leaderboard.txt", "r+")
leaderboard.write(Auth + '-' + '{}'.format(score))
leaderboard.close()
leaderboard = open("leaderboard.txt", "r+")
leaderboardlisting = leaderboard.readlines()
print(leaderboardlisting)
leaderboard.close()
exit()
## end of quiz ##
