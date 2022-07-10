# ZaidimasV04

Program code divided in separate files for more convenience. Also game history now is stored in MySQL database.

Challenges: For some reason then program reads and displays game history the results comes with "{{" in the beginning and "}}" and in the end of each sentence. Tried creating new list where "{{" and "}}" are deleted, but it seems the problem is somewhere else as in terminal then printing the list there are no "{{" and "}}". Haven't solved this problem yet.

History of previous versions of the game:

#ZaidimasV01

The game based on a party game where people sit in circle, write a word answering some question on a list, fold it (so other people could not see what's written and then pass it to other player. In the end the paper is unfold and the sentence is read loudly. In many cases it's a very fun game. In the program the player answers 3 questions. Then computer generates random missing parts of the sentence and puts a final sentence with incorporated answers of the player.

#ZaidimasV02

Same basic ZaidimasV01, but with added history of previous games.

Challenges: for some reason game sometimes crashed and sometimes worked just fine. It took me some time to find out that the reason for that was Lithuanian letters. And it wasn't easy to find a solution for the problem as it seems not many people are using Lithuanian letters so had to experiment with different codecs till found one which works.

#ZaidimasV03

ZaidimasV02 with added graphical interface made with tkinter. Basically had to rewrite the whole program.
