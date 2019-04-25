import copy, time, random, math
global board

board = list()

class Game(object):
    """A tic-tac-toe game."""

    def __init__(self, grid):
        """Instances differ by their grid marks."""
        self.grid = copy.deepcopy(grid)  # No aliasing!

    def display(self):
        """Print the game board."""
        for row in self.grid:
            for mark in row:
                print mark,
            print
        print

    def moves(self):
        """Return a list of possible moves given the current marks."""
        # YOU FILL THIS IN
        possibleMoves = list()
        count = -1
        for i in range(len(self.grid)):
                for j in range(len(self.grid)):
                    count += 1
                    if (self.grid[i][j] == '-'):
                        possibleMoves.append(count)
        return possibleMoves

    def neighbor(self, move, mark):
        """Return a Game instance like this one but with one move made."""
        # YOU FILL THIS IN
        count = -1
        board.append(move)
        for i in range(len(self.grid)):
            for j in range(len(self.grid)):
                count += 1
                if (count == move):
                    self.grid[i][j] = mark
        return Game(self.grid)

    def utility(self):
        """Return the minimax utility value of this game:
        1 = X win, -1 = O win, 0 = tie, None = not over yet."""
        # YOU FILL THIS IN
        def makeGridArray():
            grids = list()
            diag1 = list()
            diag2 = list()
            horz1 = list()
            horz2 = list()
            horz3 = list()
            count = -1
            for i in range(len(self.grid)):
                row = list()
                for j in range(len(self.grid)):
                    count += 1
                    if (self.grid[i][j] == '-') or(self.grid[i][j] != '-'):
                        value = self.grid[i][j]
                    else:
                        value = count
                    if(count == 0):
                        diag1.append(value)
                        horz1.append(value)
                    elif(count == 1):
                        horz2.append(value)
                    elif(count == 2):
                        horz3.append(value)
                        diag2.append(value)
                    elif(count == 3):
                        horz1.append(value)
                    elif(count == 4):
                        horz2.append(value)
                        diag1.append(value)
                        diag2.append(value)
                    elif(count == 5):
                        horz3.append(value)
                    elif(count == 6):
                        horz1.append(value)
                        diag2.append(value)
                    elif(count == 7):
                        horz2.append(value)
                    elif(count == 8):
                        horz3.append(value)
                        diag1.append(value)
                    else:
                        pass
                    row.append(value)
                grids.append(row)
            grids.append(horz1)
            grids.append(horz2)
            grids.append(horz3)
            grids.append(diag1)
            grids.append(diag2)
            return grids

        currGrid = makeGridArray()
        
        p1 = ['X', 'X', 'X']
        p2 = ['O', 'O', 'O']

        utilityValue = 0
        
        if ((p1 in currGrid) == True):
            utilityValue = 1
        elif ((p2 in currGrid) == True):
            utilityValue = -1
        else:
            for elements in currGrid:
              if (('-' in elements) == True):
                  utilityValue = None

        # Return the utility value of the current game configuration
        return utilityValue

class Agent(object):
    """Knows how to play tic-tac-toe."""

    def __init__(self, mark):
        """Agents use either X or O."""
        self.mark = mark

    def maxvalue(self, game, opponent):
        """Compute the highest utility this game can have."""
        # YOU FILL THIS IN
        
        def getgrids():
            grids = list()
            count = -1
            for i in range(len(game.grid)):
                for j in range(len(game.grid)):
                    count += 1
                    val = 0
                    if(game.grid[i][j] != '-'):
                        if (game.grid[i][j] != 'X'):
                            val = 2
                        else:
                            val = 1.5
                        if (j+1 < 3) and (game.grid[i][j+1] != '-'):
                            if(game.grid[i][j+1] == 'X'):
                                val += 2
                            else:
                                val += 0.75
                        if (j+2 < 3) and (game.grid[i][j+2] != '-'):
                            if(game.grid[i][j+2] == 'X'):
                                val += 1
                            else:
                                val += 0.5
                        if (j-1 >= 0) and (game.grid[i][j-1] != '-'):
                            if(game.grid[i][j-1] == 'X'):
                                val += 2
                            else:
                                val += 0.75
                        if (j-2 >= 0) and (game.grid[i][j-2] != '-'):
                            if(game.grid[i][j-2] == 'X'):
                                val += 1
                            else:
                                val += 0.5
                        if (i+1 < 3) and (game.grid[i+1][j] != '-'):
                            if(game.grid[i+1][j] == 'X'):
                                val += 2
                            else:
                                val += 0.75
                        if (i+2 < 3) and (game.grid[i+2][j] != '-'):
                            if(game.grid[i+2][j] == 'X'):
                                val += 1
                            else:
                                val += 0.5
                        if (i-1 >= 0) and (game.grid[i-1][j] != '-'):
                            if(game.grid[i-1][j] == 'X'):
                                val += 2
                            else:
                                val += 0.75
                        if (i-2 >= 0) and (game.grid[i-2][j] != '-'):
                            if(game.grid[i-2][j] == 'X'):
                                val += 1
                            else:
                                val += 0.5
                    else:
                        pass
                    thisgrid = (count, val)
                    grids.append(thisgrid)
            return grids

        def valueOf(grid):
            getGrids =  getgrids()
            if (grid == 0):
                utility = getGrids[1][1] + getGrids[2][1] + getGrids[3][1] + getGrids[4][1] + getGrids[6][1] + getGrids[8][1]
            elif (grid == 1):
                utility = getGrids[0][1] + getGrids[2][1] + getGrids[4][1] + getGrids[7][1]
            elif (grid == 2):
                utility = getGrids[0][1] + getGrids[1][1] + getGrids[5][1] + getGrids[8][1] + getGrids[4][1] + getGrids[6][1]
            elif (grid == 3):
                utility = getGrids[0][1] + getGrids[6][1] + getGrids[4][1] + getGrids[5][1]
            elif (grid == 4):
                utility = getGrids[0][1] + getGrids[1][1] + getGrids[2][1] + getGrids[3][1] + getGrids[5][1] + getGrids[6][1] + getGrids[7][1] + getGrids[8][1]
            elif (grid == 5):
                utility = getGrids[2][1] + getGrids[8][1] + getGrids[3][1] + getGrids[4][1]
            elif (grid == 6):
                utility = getGrids[0][1] + getGrids[3][1] + getGrids[7][1] + getGrids[8][1] + getGrids[2][1] + getGrids[4][1]
            elif (grid == 7):
                utility = getGrids[1][1] + getGrids[4][1] + getGrids[6][1] + getGrids[8][1]
            elif (grid == 8):
                utility = getGrids[0][1] + getGrids[4][1] + getGrids[2][1] + getGrids[5][1] + getGrids[6][1] + getGrids[7][1]
            else:
                pass
            return utility

            
        movesAndValues = list()
        if (game.utility() != 0):
            highest = 0
            listMoves = game.moves()
            if (len(board) > 0) and (len(listMoves) > 0):
                for move in listMoves:
                    m_value = (move, valueOf(move))
                    movesAndValues.append(m_value)

                for i in range(len(movesAndValues)):
                    move = movesAndValues[0][0]
                    highest = movesAndValues[0][1]
                    if(movesAndValues[i][1] > highest):
                        move = movesAndValues[i][0]
                        highest = movesAndValues[i][1]

            elif (len(board) == 0):
                move = random.randint(0, 8)
                highest = 0

            else:
                pass

            return (highest, move)
                

    def minvalue(self, game, opponent):
        """Compute the lowest utility this game can have."""
        # YOU FILL THIS IN

        # Function to get best move 'X' can make if 'O' makes a move
        def getValueforXOf(move, copyGame):
            init_game = copy.deepcopy(copyGame)
            valueforX = 0
            
            count = -1
            for i in range(len(init_game.grid)):
                for j in range(len(init_game.grid)):
                    count += 1
                    if (count == move):
                        init_game.grid[i][j] = "O"

            game = Game(init_game.grid)
            maxplayer = Agent('X')
            minplayer = Agent('O')
            (valueforX, move) = maxplayer.maxvalue(init_game, minplayer)
            return valueforX

        
        movesAndValues = list()
        if (game.utility() != 0):
            leastLoss = 1234567890
            listMoves = game.moves()
            # Create a Duplicate of current game configuration
            copyGame = copy.deepcopy(game)
            # For each possible moves 'O' can make, get the best next move 'X' can make and choose the minimum
            for move in listMoves:
                m_value = (move, getValueforXOf(move, copyGame))
                movesAndValues.append(m_value)
                game = Game(copyGame.grid)

            # Choose the move that produces least utility for opponent
            for i in range(len(movesAndValues)):
                move = movesAndValues[0][0]
                leastLoss= movesAndValues[0][1]
                if(movesAndValues[i][1] <= leastLoss):
                    move = movesAndValues[i][0]
                    leastLoss = movesAndValues[i][1]
            return (leastLoss, move)
        

def main():
    """Create a game and have two agents play it."""

    game = Game([['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']])
    game.display()

    maxplayer = Agent('X')
    minplayer = Agent('O')

    while True:

        (value, move) = maxplayer.maxvalue(game, minplayer)
        game = game.neighbor(move, maxplayer.mark)
        time.sleep(1)
        game.display()

        if game.utility() is not None:
            break

        (value, move) = minplayer.minvalue(game, maxplayer)
        game = game.neighbor(move, minplayer.mark)
        time.sleep(1)
        game.display()

        if game.utility() is not None:
            break


if __name__ == '__main__':
    main()
