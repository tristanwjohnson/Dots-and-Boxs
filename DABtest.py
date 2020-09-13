class Board:   
    '''
	object to store information about the dots and boxes board
	TBD: hold useful information for an AI to play 
    '''                    
    def __init__(self,x,y):		
        ''' creates a 2d array to represent the dots
		each element is a line(even rows are horizontal odd rows are verticle) '''
        self.barArr = []
        self.boxArr = []
        self.width = x
        self.height = y
        row = []
        for i in range(self.height):
            row.append(0)

        for j in range((2*self.width)+1):
            if j%2 == 0:
                self.barArr.append(row.copy())
            else:
                self.barArr.append(row+[0])

        for k in range(self.width):
            self.boxArr.append(row.copy())

    def __repr__(self):
        ''' use to return useful information when working with AI '''
        return "w: "+str(self.width)+" h: "+str(self.height)

    def __str__(self):
        ''' fills boardstr with a string verison of bar arr '''
        boardstr = ""

        for i in range(len(self.barArr)):
            if i%2 == 0:
                boardstr += " "
                for j in range(len(self.barArr[0])):
                    if self.barArr[i][j] != 0:
                        boardstr += "  --   "
                    else:
                        boardstr += "  ..   "
            else:
                for j in range(len(self.barArr[1])):
                    if self.barArr[i][j] != 0:
                        boardstr += "|   "
                    else:
                        boardstr += ":   "

                    if j < len(self.barArr[1]) -1:
                        if self.boxArr[i//2][j] != 0:
                            boardstr += str(self.boxArr[i//2][j])+"  "
                        else:
                            boardstr += "   "

            boardstr += "\n"
        return (boardstr)

    def boolDisplayBoard(self):
        ''' displays all boxes and who has filled them '''
        for row in self.boxArr:
            print(row)

    def displayBoard(self):
        ''' shows string representation of board for users '''
        print(self)

    
    def valid(self,x,y):
        ''' checks if a move is a valid move
		valid if its within the board and has yet to be filled'''
        if(y%2 == 0):
            if (x < 0) or (x > self.width-1):
                return False
        else:
            if (x < 0) or (x > (self.width)):
                return False
        if(x%2 == 0):
            if (y < 0) or (y > 2*self.height):
                return False
        else:
            if (y < 0) or (y > 2*self.height):
                return False
        if self.barArr[y][x] != 0:
            return False
        return True


    def move(self, x, y, player):
        '''makes the move for the player and returns if a point was gained'''
        if self.valid(x, y):
            self.barArr[y][x] = player
            point = self.update(player)
            self.displayBoard()
        else:
            point = -1
        return point

    def update(self, player):
        '''update boxarr if a new box is filled and give it the value of the player who claimed it'''
        for i in range(len(self.boxArr)):
            for j in range(len(self.boxArr[0])):
                if not self.boxArr[i][j]:
                    if (self.barArr[i*2][j] != 0) and (self.barArr[i*2+2][j] != 0) and (self.barArr[i*2+1][j] != 0) and (self.barArr[i*2+1][j+1] !=0):
                        self.boxArr[i][j] = player
                        return 1
        return 0

    def full(self):
        ''' returns true if every box is taken'''
        for row in self.boxArr:
            for box in row:
                if not box:
                    return False
        return True

class Game:
    '''a game object holds a game of DAB'''
    def __init__(self):
        self.score = [0, 0]
        self.width = int(input("how many rows would you like in your board? "))
        self.height = int(input("how many coloumns would you like in your board? "))
        self.board = Board(self.height, self.width)

    def __repr__(self):
        return self.board

    def play(self):
        '''simulates gameplay of DOB in commandline
		takes user inputs and updates the board object and quits when someone wins
		TBD: replace with pygame method'''
        gameover = 0
        player = 1
        print("input your move in the form X Y")
        while gameover == 0:
            
            try: x,y = [int(x) for x in input("P"+str(player)+" make you move ").split()]
            except: continue

            move = self.board.move(x,y,player)

            while move == -1:
                print("That move is not valid!")
                x, y = [int(x) for x in input("P"+str(player)+" make a valid move ").split()]
                move = self.board.move(x,y,player)

            while move != 0 and not self.board.full():
                if player == 1:
                    self.score[0] += move
                else:
                    self.score[1] += move

                x, y = [int(x) for x in input("P"+str(player)+" make another move ").split()]
                move = self.board.move(x, y, player)

            #switch turns
            if player == 1:
                self.score[0] += move
                player = 2
            else:
                self.score[1] += move
                player = 1

            if self.board.full():
                gameover = 1
		# Display end game information
        print("P1 " + str(self.score[0]) + "  P2 " + str(self.score[1]))
        if self.score[0] > self.score[1]:
            print("P1 wins!")
        elif self.score[0] < self.score[1]:
            print("P2 wins!")
        else:
            print("It's a tie")

    def getScore(self):
        """returns how many boxs each player has taken"""
        print("P1 ",self.score[0]," P2 ",self.score[1])

# run game when file run
print("Welcome to Dots and Boxs")
g = Game()
g.play()
