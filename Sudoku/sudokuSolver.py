


board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]]



def showBoard(board):

    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print ("---------------------")
        
        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print('| ', end='')

            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j])+ " ", end='')
    




def checkForEmptySpace(board):
    #iterate through the board 1 by 1 to check for 0's
    for row in range(len(board)):
        for column in range(len(board[0])):
            if board[row][column] == 0:
                return (row,column)
    return False    



def tryNum(board,pos,value):
    # check if there are any similar values in the row
    for i in range(len(board)):
        if value == board[pos[0]][i] and pos[1] != i:
            return False
    

    # check column for similar values
    for i in range(len(board[0])):
        if value == board[i][pos[1]] and pos[0] != i:
            return False

    # sudoku also doesn't allow you to have the same numbers in each 3*3 square area
    # we integer divide by 3 to find which box we're in for x and y, if our value is at [0][1] that would mean our box is the one in the top left corner
    x_pos = pos[1] // 3
    y_pos = pos[0] // 3

    for i in range(y_pos * 3, y_pos*3 + 3):
        for j in range(x_pos * 3, x_pos * 3 + 3):
            if value == board[i][j]: 
                return False
    
    # if we manage to get out of all the loops without returning that means we didnt find any similar values, thus:
    return True

def solveBoard(board):
    check = checkForEmptySpace(board) # check will hold a tuple with row, col if there is an empty space, if there is no empty space then it will hold False
    if not check:
        return True # if check is false, that means our board is fully solved and we can return true
    
    else:
        row, col = check # unpack the tuple
    
    for i in range(1,10): # we try each value from 1,10 and see if it violates sudoku rules or not
        if(tryNum(board,(row,col),i)):
            board[row][col] = i

            if(solveBoard(board)): # try to solve board with our new value
                return True

            board[row][col] = 0 # if we can't continue any further with our current solution then reset what we did previously, aka backtrack

    return False
        
                
    


showBoard(board)
print("\n\n\n")
solveBoard(board)
showBoard(board)