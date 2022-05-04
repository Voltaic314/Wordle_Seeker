# Wordle-Seeker-by-Voltaic
Projects made by Logan Maupin aka Voltaic


This is a program made by Logan Maupin aka Voltaic (on github & socials). I'm a computer science student at the University of Arizona Online. My goal with this project is to make word games like Lingo and Wordle a bit easier by suggesting all possible words the target word may be. 

Some sources of error in this code: 
This code uses a dictionary text file that I acquired through a different github repository -- link here ---> https://github.com/dwyl/english-words/ <---- and it's dictionary may not perfectly match up with dictionaries used in other online word games / apps like Wordle, Lingo, 5 letter hangman games, and so on. So there may be rare but possible instances where the target word you are meant to find may not even appear in the program's suggestions or alternatively the program might suggest a word that the other game / app might say isn't a real word. Keep that in mind when using it. (Also it seems like Wordle has a much smaller dictionary and priorities words that are more common than otherwise, so also keep that in mind when playing). 

##################################################################

HOW TO USE THIS CODE: 

First make sure your device has some way to run python. I would recommend watching a tutorial on run a python script. This varies based on operating system so best just to look up a tutorial of how to run python on your OS, it's pretty easy to do all things considered. Once python is installed just execute the program in your command line and it should start up. 

You will also need the dictionary file I have provided otherwise the code will not work. So just download that dictionary txt file and put it in the same directory as the python script. (Wordleseeker.py file)

When the program starts it will ask you to input a "letter you know" and it will ask this up to 5 times. The way this works is if you only know specific single letters but don't know the combination or order they go in, just type each letter in each line. leaving lines blank for the letters you don't know. For example, if wordle's target word is ghost, but I only know there is an H, O, and S in the word, I would just type H in the first line, O in the second line, and S in the third. It does not matter which order you type the lines for single lines. 

However if you know that some letters go together, for example let's say the target word is GHOST but yet I only know that there's a G somewhere and I know "OS" are in the word, I could type G in the first input line, hit enter, then type OS in the second line, then enter enter enter. Then it should provide me with a list of all words that contain the letter G and "OS" 

One final note: unfortunately this code doesn't handle duplicate letters whille. So let's say for example the target word is Trees. You know there is an "RE" and you know there's also another "E" somewhere in the word. If you try to type in RE in the first line and E in the second line, it will basically ignore the second line because it's already looking for an E in the word. The code doesn't distinguish between single and duplicate letters unless you specifically type "EE" but in this case the word could be "There" and you would miss out on that suggestion. 

Also, if you enter 5 letters or less and it tells you to input letters again for the first time, it means your search did not come up with any results. so therefore you'll need to try to search again with different letters. (or it may just mean that the combination of letters you entered does equal a word but it's not in the dictionary file - this is rare. More likely you may have entered more than 5 characters). 

#######################################################################

If you can think of any ways to improve this code, feel free to modify it or reach out to me with suggestions. I am only a beginner programmer right now so any suggestions are appreciated. Thanks and have fun! 
