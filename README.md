# Wordle-Seeker-by-Voltaic
Projects made by Logan Maupin aka Voltaic


This is a program made by Logan Maupin aka Voltaic (on github & socials). I'm a computer science student at the University of Arizona Online. My goal with this project is to make word games like Lingo and Wordle a bit easier by suggesting all possible words the target word may be. 

Some sources of error in this code: 
This code uses a dictionary text file that I acquired through a different github repository -- link here ---> https://github.com/dwyl/english-words/ <---- and it's dictionary may not perfectly match up with dictionaries used in other online word games / apps like Wordle, Lingo, 5 letter hangman games, and so on. So there may be  rare but possible instances where the target word you are meant to find may not even appear in the program's suggestions or alternatively the program might suggest a word that the other game / app might say isn't a real word. Keep that in mind when using it. (Also it seems like Wordle has a much smaller dictionary and prioritizes words that are more common than otherwise, so also keep that in mind when playing). 

###############################################################

ABOUT THE GAME:
Wordle is a 5 letter game in which the goal is to guess five-letter words until you guess the right
word. But the game will tell you if some letters are in the word in general, or if not. If they are
in the word, the game will tell you if any of the letters in the word you guessed are in the same place
as the target word.

##################################################################

HOW TO USE THIS CODE: 

First make sure your device has some way to run python. I would recommend watching a tutorial on run a python script. This varies based on operating system so best just to look up a tutorial of how to run python on your OS, it's pretty easy to do all things considered. Once python is installed just execute the program in your command line and it should start up. 

You will also need the dictionary word list txt file I have provided otherwise the code will not work. So just download that dictionary txt file and put it in the same directory as the python script.

###############################################################

HOW THIS SCRIPT WORKS: 

When you run this script, it will ask if you know any letters positions in the target word. If so, we need to know
what letters and where at. If not, then we need to know if you know any letters in the word and any letters not in the
word.
If you do know any letters positions, as you type them, the script will filter words out of the original list if they
don't contain that letter at that position.
if you know any good letters (letters we know are in the target word), then the script will check to make sure that ALL
of your good letters are in each word or else it will remove them from the list.
if you know any bad letters, (letters we know that aren't in the word), then the script will check to make sure that ANY
of the bad letters are not in any words in the list or else it will remove them from the list.
Finally, it will print the results to you as well as how many results are in your query.

#################################################################

From my own statistical info gathering, Arise and Until are the best starting words because they use
the top 9 most used letters in the alphabet for five-letter words.

##################################################################

If you can think of any ways to improve this code, feel free to modify it or reach out to me with suggestions. I am only a beginner programmer right now so any suggestions are appreciated. Thanks and have fun! 

