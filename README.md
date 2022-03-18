# cse210-06
Memory Game: With this repository, you could have the opportunity to participate in the Memory game project. This project is our final project for the course.

So, you want to excerice your mind? Play Memory game and you might have fun, playing our game. 

# Rulers:
- There will be just one player.
- The game should be played just with a mouse.
- There will be many hiden card on the screen.
- The player should touch every hiden pair of cards.
- The ame ends when all the pairs are matched.


Getting Started Make sure you have Python 3.8.0 or newer installed and running on your machine. Open a terminal and browse to the project's root folder. Start the program by running the following command:
```
py main.py
``` 
You can also run the program from an IDE like Visual Studio Code. Start your IDE and open the project folder. Select the main module inside the dice folder and click the "run" button.

# Getting Started
Make sure you have Python 3.8.0 or newer and Raylib Python CFFI 3.7 and Pygame installed and running on your machine. You can install Raylib and Pygame Python by opening a terminal and running the following command:

```
python3 -m pip install raylib

```
After you installed these libraries, you can run without problem this programa.

# Project Structure

The project files and folders are organized as follows:

```
root                        (project root folder)
+-- cse-210-06              
  +-- Game        
    +--- memory_game	    (project main folder)		    
        +--- casting        (ALL THE ACTORS IN OUR GAME AND OPERATIONS)
	  +-- actor.py        (Parent class to create objects)
	  +-- cast.py         (All types of operations applied to our actors) 
	  +-- card.py         (This will be the main actor of the game) 
	  +-- timer.py        (lets control the time during the game) 
    	+--- directing      (THE MAIN CLASS TO DIRECT THE GAME)
  	  +---- director.py   (This class will direct all the actors)
   	+--- scripting      (TRACKING ACTIONS )
	  +-- action.py     		(overridden by derived classes)
	  +-- control_actors_action.py  ()
	  +-- draw_cards_action.py      (Draws all the actors)
	  +-- reveal_cards_action.py    (Makes visible all cards when the game stars)
	  +-- remove cards_action.py    (Makes invisible when players pair two cards)
	  +-- add_cards_action.py       (**The paired card are put above the screen)
	  +-- script.py                 (Keep track of a collection of actions)
  	+--- services        (ALL SERVICES TO PLAY WITH THE GAME )
	  +---- video_services.py       (Lets to draw graphic on the screem)
 	+--- shared          (CONTROL POSITION AND COLOR IN THE GAME)
	  +---- color.py        (Control color of every character on the sreem)
	  +---- point.py        (Control position X's and Y's on the sreen)
      +-- __main__.py        (THE MAIN CLASS)
      +-- constants.py       (CONSTANTS TO BE USED IN THE GAME)
      +-- soundtrack.mp3     (Background music)
    +-- README.md            (General info)
```

# Required Technologies
* Python 3.9.0
* Raylib Python 3.7

# Authors

```
* Melanie Cristeche (cri21012@byui.edu)
* Carter Raymond (ray21006@byui.edu)
* Leonard Salazar (sal21034@byui.edu)
```