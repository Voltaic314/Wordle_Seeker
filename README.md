# Wordle-Seeker-by-Voltaic
Projects made by Logan Maupin aka Voltaic


This is a program made by Logan Maupin aka Voltaic (on github & socials). I'm a computer science student at the University of Arizona Online. My goal with this project is to make word games like Lingo and Wordle a bit easier by suggesting all possible words the target word may be. 

Some sources of error in this code: 
This code uses a dictionary text file that I acquired through a different github repository -- link here ---> https://github.com/dwyl/english-words/ <---- and it's dictionary may not perfectly match up with dictionaries used in other online word games / apps like Wordle, Lingo, 5 letter hangman games, and so on. So there may be  rare but possible instances where the target word you are meant to find may not even appear in the program's suggestions or alternatively the program might suggest a word that the other game / app might say isn't a real word. Keep that in mind when using it. (Also it seems like Wordle has a much smaller dictionary and prioritizes words that are more common than otherwise, so also keep that in mind when playing). 

##################################################################

HOW TO USE THIS CODE: 

First make sure your device has some way to run python. I would recommend watching a tutorial on run a python script. This varies based on operating system so best just to look up a tutorial of how to run python on your OS, it's pretty easy to do all things considered. Once python is installed just execute the program in your command line and it should start up. 

You will also need the dictionary file I have provided otherwise the code will not work. So just download that dictionary txt file and put it in the same directory as the python script. (Wordleseeker.py file)

##################################################################

When the program starts it will ask you to input "letters you know", this is a comma separated list so you have to separate each letter or combo of letters with a comma. The way this works is if you only know specific single letters but don't know the combination or order they go in, just type each letter between each comma. For example, if wordle's target word is ghost, but I only know there is an H, O, and S in the word, I would just type "h, o, s" (it is not case sensitive).

However if you know that some letters go together, for example let's say the target word is GHOST but yet I only know that there's a G somewhere and I know "OS" are in the word, I could type "G, OS", then enter enter enter. Then it should provide me with a list of all words that contain the letter "G" and "OS" 

One final note: unfortunately this code doesn't handle duplicate letters well. So let's say for example the target word is Trees. You know there is an "RE" and you know there's also another "E" somewhere in the word. If you try to type in "RE, E" it will basically ignore the second E because it's already looking for an E in the word with the RE part. Unfortunate oversight of how the code works, if any of you know a clean solution to this please feel free to propose contributions! 

But yeah so the code doesn't distinguish between single and duplicate letters unless you specifically type "EE" but in this case the word could be "There" and you would miss out on that suggestion. 

Also, if you enter 5 letters or less and it tells you to input letters again for the first time, it means your search did not come up with any results. So therefore you'll need to try to search again with different letters. (or it may just mean that the combination of letters you entered does equal a word but it's not in the dictionary file - this is rare. More likely you may have entered more than 5 characters).  Note that the code may also tell you to try again if you create a paradox. Such that you for example type "G" as a good letter, but then also put "G" as a bad letter, you have created a logical paradox. This isn't shrodinger's cat, the program will not get all philosophical on you, it will just tell you to try again because such a word that both contains and doesn't contain said letter at the same time does not exist (LOL). Similarly if you enter more than 5 characters in the good letter section, the program will also tell you to try again, this is by design because obviously there are no 6-letter words in a 5 letter game. *DUH* LOL.

Remember, on the section of inputting bad letters, do not leave it blank, if you don't know any bad letters (which is mathematically very unlikely), just hit space and then enter, don't just hit enter otherwise you will get 0 results and have to start over. Sorry. Another oversight in the code's design. Again, feel free to propose contributions. 

##################################################################

If you can think of any ways to improve this code, feel free to modify it or reach out to me with suggestions. I am only a beginner programmer right now so any suggestions are appreciated. Thanks and have fun! 
