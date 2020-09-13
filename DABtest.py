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





""" 
def sethedge(x,y) {      #Sets horizontal edge
	hedge[x][y]=1
	if (x>0) box[x-1][y]++:
	if (x<m) box[x][y]++:
	document.images[2*x*nn+2*y+1].src=n2.src:
	checkh(x,y)
	player=1-player
}

def setvedge(x,y) {      #Sets vertical edge
 	vedge[x][y]=1
	if (y>0) box[x][y-1]++
	if (y<n) box[x][y]++
	document.images[(2*x+1)*nn+2*y].src=n2.src
	checkv(x,y)
	player=1-player
}

def takeedge(zz,x,y) {    #Set hedge if zz=1 and vedge if zz=2.
	if (zz>1) setvedge(x,y)
	else sethedge(x,y)
}

def makemove() {
	takesafe3s()                                #take all single boxes and double boxes with 3 sides
	if (sides3()) {                             #if there is a box with three sides
		if (sides01()) {                        #
			takeall3s()                         #
			takeedge(zz,x,y)                    #
		} else {
			sac(u,v)                            #
		}	
		if (score[0]+score[1]==m*n) {           #if the game is over display the score
			alert("Game over.\r Score Red = "+score[0]+",  Blue = "+score[1])
		}
	} 
    else if (sides01())                         #
        takeedge(zz,x,y)                        #
	else if (singleton())                       #
        takeedge(zz,x,y)                        #
	else if (doubleton())                       #
        takeedge(zz,x,y)                        #
	else 
        makeanymove()                           # if no squares to take, take a random edge 
}

def takesafe3s() {     #Take all singleton and doubleton 3's.
	for (var i=0;i<m;i++) {
		for (var j=0;j<n;j++) {
			if (box[i][j]==3) {                                 #if theres a box with 3 sides
				if (vedge[i][j]<1) {
					if (j==0 or box[i][j-1]!=2) 
                        setvedge(i,j)
				} else if (hedge[i][j]<1) {
					if (i==0 or box[i-1][j]!=2) 
                        sethedge(i,j)
				} else if (vedge[i][j+1]<1) {
					if (j==n-1 or box[i][j+1]!=2) 
                        setvedge(i,j+1)
				} else {
					if (i==m-1 or box[i+1][j]!=2) 
                        sethedge(i+1,j)
				}
			}
		}
	}
}

def sides3() {     #Returns true and u,v if there is a box(u,v)=3.
	for (var i=0;i<m;i++) {
		for (var j=0;j<n;j++) {
			if (box[i][j]==3) {
				u=i
				v=j
				return true
			}
		}
	}
	return false
}

def takeall3s() {
	while (sides3()) takebox(u,v)
}

def sides01() {                         #Returns true and zz,x,y if there is a safe edge(x,y).
	if (Math.random()<.5) 
        zz=1 
    else 
        zz=2                            #zz=1 if horizontal, zz=2 if vertical
	var i=Math.floor(m*Math.random())
	var j=Math.floor(n*Math.random())
	if (zz==1) {
		if (randhedge(i,j)) 
            return true
		else {
			zz=2
			if (randvedge(i,j)) 
                return true
		}
	} else {
		if (randvedge(i,j))
            return true
		else {
			zz=1
			if (randhedge(i,j)) 
                return true
		}
	}
	return false
}

def safehedge(i,j) {     #Returns true if (i,j) is a safe hedge
	if (hedge[i][j]<1) {
		if (i==0) {
			if (box[i][j]<2) return true
		} else if (i==m) {
			if (box[i-1][j]<2) return true
		}
		else if (box[i][j]<2 && box[i-1][j]<2) return true
	}
	return false
}

def safevedge(i,j) {
	if (vedge[i][j]<1) {
		if (j==0) {
			if (box[i][j]<2) return true
		} else if (j==n) {
			if (box[i][j-1]<2) return true
		}
		else if (box[i][j]<2 && box[i][j-1]<2) return true
	}
	return false
}

def randhedge(i,j) {
	x=i
	y=j
	do {
		if (safehedge(x,y)) return true
		else {
			y++
			if (y==n) {
				y=0
				x++
				if (x>m) x=0
			}
		}
	} while (x!=i || y!=j)
	return false
}

def randvedge(i,j) {
	x=i
	y=j
	do {
		if (safevedge(x,y)) return true
		else {
			y++
			if (y>n) {
				y=0
				x++
				if (x==m) x=0
			}
		}
	} while (x!=i || y!=j)
	return false
}
	
def singleton() {     #Returns true and zz,x,y if edge(x,y) gives exactly
	var numb              #1 square away
	for (var i=0;i<m;i++) {
		for (var j=0;j<n;j++) {
			if (box[i][j]==2) {
				numb=0
				if (hedge[i][j]<1) {
					if (i<1 or box[i-1][j]<2) numb++
				}
				zz=2
				if (vedge[i][j]<1) {
					if (j<1 or box[i][j-1]<2) numb++
					if (numb>1) {
						x=i
						y=j
						return true
					}
				}
				if (vedge[i][j+1]<1) {
					if (j+1==n or box[i][j+1]<2) numb++
					if (numb>1) {
						x=i
						y=j+1
						return true
					}
				}
				zz=1
				if (hedge[i+1][j]<1) {
					if (i+1==m or box[i+1][j]<2) numb++
					if (numb>1) {
						x=i+1
						y=j
						return true
					}
				}
			}
		}
	}
	return false
}

def doubleton() {     #Returns true and zz,x,y if edge(x,y) gives away 
	zz=2                  #exactly 2 squares
	for (i=0;i<m;i++) {
		for (j=0;j<n-1;j++) {
			if (box[i][j]==2 and box[i][j+1]==2 and vedge[i][j+1]<1) {
				if (ldub(i,j) and rdub(i,j+1)) {
					x=i
					y=j+1
					return true
				}
			}
		}
	}
	zz=1
	for (j=0;j<n;j++) {
		for (i=0;i<m-1;i++) {
			if (box[i][j]==2 and box[i+1][j]==2 and hedge[i+1][j]<1) {
				if (udub(i,j) and ddub(i+1,j)) {
					x=i+1
					y=j
					return true
				}
			}
		}
	}
	return false
}

def ldub(i,j) {      #Given box(i,j)=2 and vedge(i,j+1)=0, returns true
	if (vedge[i][j]<1) {      //if the other free edge leads to a box<2
		if (j<1 or box[i][j-1]<2) return true 
	} else if (hedge[i][j]<1) {
		if (i<1 or box[i-1][j]<2) return true
	} else if (i==m-1 or box[i+1][j]<2) {
		return true
	}
	return false
}

def rdub(i,j) {
	if (vedge[i][j+1]<1) {
		if (j+1==n or box[i][j+1]<2) return true
	} else if (hedge[i][j]<1) {
		if (i<1 or box[i-1][j]<2) return true
	} else if (i+1==m or box[i+1][j]<2) {
		return true
	}
	return false
}
				
def udub(i,j) {
	if (hedge[i][j]<1) {
		if (i<1 or box[i-1][j]<2) return true
	} else if (vedge[i][j]<1) {
		if (j<1 or box[i][j-1]<2) return true
	} else if (j==n-1 or box[i][j+1]<2) {
		return true
	}
	return false
}

def ddub(i,j) {
	if (hedge[i+1][j]<1) {
		if (i==m-1 or box[i+1][j]<2) return true
	} else if (vedge[i][j]<1) {
		if (j<1 or box[i][j-1]<2) return true
	} else if (j==n-1 or box[i][j+1]<2) {
		return true
	}
	return false
}

def sac(i,j) {     #sacrifices two squares if there are still 3's
    count=0
	loop=false
	incount(0,i,j)
	if (!loop) takeallbut(i,j)
	if (count+score[0]+score[1]==m*n) {
		takeall3s()
	} else {
		if (loop) {
			count=count-2
		}
		outcount(0,i,j)
		i=m
		j=n
	}
}

def incount(k,i,j) {                    #enter with box[i][j]=3 and k=0
    count++                             #returns count = number in chain starting at i,j
	if (k!=1 and vedge[i][j]<1) {       #k=1,2,3,4 means skip left,up,right,down.
		if (j>0) {
			if (box[i][j-1]>2) {
				count++
				loop=true
			} else if (box[i][j-1]>1) incount(3,i,j-1)
		}
	} else if (k!=2 and hedge[i][j]<1) {
		if (i>0) {
			if (box[i-1][j]>2) {
				count++
				loop=true
			} else if (box[i-1][j]>1) incount(4,i-1,j)
		}
	} else if (k!=3 and vedge[i][j+1]<1) {
		if (j<n-1) {
			if (box[i][j+1]>2) {
				count++
				loop=true
			} else if (box[i][j+1]>1) incount(1,i,j+1)
		}
	} else if (k!=4 and hedge[i+1][j]<1) {
		if (i<m-1) {
			if (box[i+1][j]>2) {
				count++
				loop=true
			} else if (box[i+1][j]>1) incount(2,i+1,j)
		}
	}
}

def takeallbut(x,y) {
	while (sides3not(x,y)) {
		takebox(u,v)
	}
}
	
def sides3not(x,y) {                
	for (var i=0;i<m;i++) {
		for (var j=0;j<n;j++) {
			if (box[i][j]==3) {
				if (i!=x or j!=y) {
					u=i
					v=j
					return true
				}
			}
		}
	}
	return false
}

def takebox(i,j) {                      # takes a box by filling in last bar
	if (hedge[i][j]<1) sethedge(i,j)
	else if (vedge[i][j]<1) setvedge(i,j)
	else if (hedge[i+1][j]<1) sethedge(i+1,j)
	else setvedge(i,j+1)
}

def outcount(k,i,j) {     #Takes all but count-2 squares and exits
	if (count>0) {
		if (k!=1 and vedge[i][j]<1) {
			if (count!=2) setvedge(i,j)
			count--
			outcount(3,i,j-1)
		} else if (k!=2 and hedge[i][j]<1) {
			if (count!=2) sethedge(i,j)
			count--
			outcount(4,i-1,j)
		} else if (k!=3 and vedge[i][j+1]<1) {
			if (count!=2) setvedge(i,j+1)
			count--
			outcount(1,i,j+1)
		} else if (k!=4 and hedge[i+1][j]<1) {
			if (count!=2) sethedge(i+1,j)
			count--
			outcount(2,i+1,j)
		}
	}
}

def makeanymove() {         #makes the first possiple 
	x=-1
	for (i=0;i<=m;i++) {
		for (j=0;j<n;j++) {
			if (hedge[i][j]<1) {
				x=i
				y=j
				i=m+1
				j=n
			}
		}
	}
	if (x<0) {
		for (i=0;i<m;i++) {
			for (j=0;j<=n;j++) {
				if (vedge[i][j]<1) {
					x=i
					y=j
					i=m
					j=n+1
				}
			}
		}
		setvedge(x,y)
	} else {
		sethedge(x,y)
	}
	if (player==0) makemove()
}

def checkh(x,y) {     #check if h edge move scores any points
	var hit=0
	if (x>0) {
		if (box[x-1][y]==4) {
			var uu=x-1
			document.images[(2*uu+1)*nn+2*y+1].src=flag[player]
			score[player]++
			hit=1
		}
	}
	if (x<m) {
		if (box[x][y]==4) {
			document.images[(2*x+1)*nn+2*y+1].src=flag[player]
			score[player]++
			hit=1
		}
	}
	if (hit>0) player=1-player
}

def checkv(x,y) {    #check if v edge move scores any points
	var hit=0
	if (y>0) {
		if (box[x][y-1]==4) {
			var vv=y-1
			document.images[(2*x+1)*nn+2*vv+1].src=flag[player]
			score[player]++
			hit=1
		}
	}
	if (y<n) {
		if (box[x][y]==4) {
			document.images[(2*x+1)*nn+2*y+1].src=flag[player]
			score[player]++
			hit=1
		}
	}
	if (hit>0) player=1-player
}
 """