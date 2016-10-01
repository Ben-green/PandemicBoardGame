## What is this?

This is a simple project I've started to help me learn how to use vim, python and Github. When it's finished it should let somebody play the Pandemic board game as one or more of the players.

I'm about to start an OU degree in computing and IT and hoping for a career in IT eventually. The role I've got my eye on is one of full stack developer:

>The term full-stack means developers who are comfortable working with
both back-end and front-end technologies. To be more specific, it means
that the developer can work with databases, PHP, HTML, CSS, JavaScript
and everything in between ... --
[Being a Full Stack Developer](https://www.sitepoint.com/full-stack-developer/),
(George Fekete, September 22, 2014)

although I understand this might already be old hat

>It seems as though everyone in tech today is infatuated with the full-stack
developer. Full stack may have been possible in the Web 2.0 era, but a new
generation of startups is emerging, pushing the limits of virtually all
areas of software. --
[The Rise And Fall Of The Full Stack Developer](https://techcrunch.com/2014/11/08/the-rise-and-fall-of-the-full-stack-developer/),
(Peter Yared, November 8, 2014)

So I'm going to try to learn as much code as I can and focus on completing practical fun projects with other people alongside my course. 


## What am I trying to learn?

I'd like to get my head round Python, SQL, and anything else relevant to make this work. I think that probably includes git and how to use the command line in Linux (running Ubuntu at the moment). In the future I'd also like to learn

At least one kind of web server language, probably two (Apache, PHP I think)
At least one version of SQL
Some basic front end website languages (HTML, JavaScript and the like)


## Classes and Defs in PandemicGame.py
### A - Class - startinggame
1- startinglocals - Updates the BoardTBL table with basic game info. A research station is set in Atlanta, and a given number of players are also set there.
2- BoardTBL - Sets up the gameboard from a given .txt file. This has columns which give the name, colour, connections and cubes in a city. It also has columns which are set to 1 from 0 when a player or research station is present.
3- pdTBL - creates and populates the player deck table pdTBL. This has 3 columns for the name, colour and position of the card in the deck.
4- pddTBL - creates the player deck discard pile, which simply contains the name of the card in the discard pile.
5- idTBL - creates the infection deck
6- iddTBL - creates the infection deck discard pile
7- edTBL - shuffles the event cards together in a pile from a given .txt file.
8- cTBL - shuffles the character identity cards together in a pile from a given .txt file.
9- caTBL - gives all players an identity (no need to specify player numbers)
10 - cubesTBL - creates a table with stores the numbers of each time of cube not on the board.
11- shufpd - shuffles the player deck (with event cards) for a given number of players.
12- shufid - shuffles the infection deck.
13- player1TBL - draws a hand for player one for a given number of players.
14- player2TBL - draws a hand for player two for a given number of players.
15- player3TBL - draws a hand for player three for a given number of players.
16- player4TBL - draws a hand for player four for a given number of players.
17- epTBL - shuffles a given number of Epidemic cards into the player deck.
18- gsTBL - creates a game state table with the infection rate, outbreak count, number of players, number of epidemics, active player and actions remaining.
19- sginfect - infects 3 cities with 3 cubes, 3 with 2 and 3 with 1.
20- startnewgame - starts a new game for a given number of players, on a specific board, with a given number of epidemics using given event and character files.

### B - Class - inaturn
1 - getplayer - returns the location of a given player. 
2 - getcityallcubes - returns all the cubes of any colour found in a given city.
3 - infectcities - infects cities at a given rate
4 - move - moves a given player from a given location to a given destination
5 - getxcube - returns the name of all cities with a given colour and given number of cubes in
6 - getoc - returns the current outbreak count 
7 - getir - returns the current infection rate
8 - gethand - returns the contents of a given players hand
9 - getcitycubes - returns the number of cubes of a given colour in a given city
10 - getcubes - returns the number of cubes remaining of a given colour
11 - usecube - reduces the remaining amount of a given colour of cube by 1.
12 - getidd - returns the cards in the infection deck discard pile
13 - getpdd - returns the cards in the player deck pile
14 - discard - for a given player discards a given card from their hand.
15 - pdraw - draws a single card for a given player, checking if it is an epidemic
16 - epidemic - carries out an epidemic on the board
17 - co - checks for unresolved outbreaks
18 - ic - infects a given city with a given colour
19 - action - reduces the current active players action by 1, and if zero moves to the next players turn
20 - rc - removes a cube of a given colour from a given location
21 - getap - returns the current active player

### C - Class - playeraction
1 - trainboat - move a given player from a given location to another adjacent location, for an action.
2 - direct - move a given player to given location dicarding the card of the destination city from their hand.
3 - charter - move a given player to a given location discarding the card of their current location from their hand.
4 - shuttle - move a given player from a given location to a given destination where there is a research station present at each locaton.
5 - treat - remove 1 cube of a given colour from a given city, or all cubes of that colour if a cure has been discovered.
6 - cure - discard 5 given cards of the same colour to discover a cure for a disease.
7 - sk - moves a given card from a given player to another given player when both are in the same city and the city named on the card.
8 - br - a given player builds a research station in a given city discarding that city card if they are in the city on the card
