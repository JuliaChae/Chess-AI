# Chess-AI

Chess-AI is a chess player algorithm that is able to play against human players or other chess playing algorithms. This project contains programs to: 
* Determine if a piece is under threat and analyze all possible moves to make on the board 
* Select the optimal move based on the possible moves generated for the board 
* Display the current state of board and output list of captured pieces
* Continously ask opposing player for their moves and update board accordingly 

## Move Generation Algorithm
Chess-AI determines the next move to make through the use of a game tree and alpha beta search. At every turn, a game tree is generated to scope all possible moves by both sides in the next n turns of the game. This tree is then searched through a minimax search algorithm to maximize the outcome of the computer's move and to minimize the opponent's move. This algorithm is paired with alpha beta pruning to optimize the number of depths that can be searched down the game tree. The evaluation of all possible moves is custom-weighed for each piece, with different scores based on where the piece is located on the board. The move that maximizes the evaluation score for the computer is selected at the end of the searches. 
