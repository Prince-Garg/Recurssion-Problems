arr = [
    [ 1 , 1 , 1 , 1 ],
    [ 1 , 0 , 0 , 1 ],
    [ 1 , 0 , 0 , 1 ],
    [ 1 , 0 , 0 , 1 ]
]

max_rows = 3
max_cols = 3

def solveMaze(row, col, result):
    if row == max_rows and col == max_cols:
        return True
    
    if row > max_rows or col > max_cols:
        return False    
    
    if arr[row][col] == 0:
        return False
    

    ret = False
    result.append((row + 1, col))
    ret = solveMaze(row + 1, col, result)
    if not ret:
        result.pop()
        result.append((row, col + 1))
        ret = solveMaze(row, col + 1, result)
        if not ret:
            result.pop()
    return ret

result = [(0,0)]
solveMaze(0, 0, result)
print result