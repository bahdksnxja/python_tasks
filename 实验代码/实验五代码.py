#第一题
"""
words = "hey fellow warrior".split()
spinning_words = [word[::-1] if len(word) >= 5 else word for word in words]
result = " ".join(spinning_words)
"""

#第二题
"""
def find_outlier(int):
    odds = [x for x in int if x%2!=0]
    evens= [x for x in int if x%2==0]
    return odds[0] if len(odds)<len(evens) else evens[0]
"""

#第三题
"""
def is_pangram(s):

    s = s.lower()

    for char in 'abcdefghijklmnopqrstuvwxyz':
        if char not in s:
            return False
    
    return True
"""
#第四题
"""
def validate_sudoku(board):
    elements = set(range(1, 10))
    
    # row
    for b in board:
        if set(b) != elements: 
            return False
    
    # column
    for b in zip(*board): 
        if set(b) != elements: 
            return False
    
    # magic squares
    for i in range(3, 10, 3):
        for j in range(3, 10, 3):
            if elements != {(board[q][w]) 
                            for w in range(j-3, j) 
                            for q in range(i-3, i)}:
                return False
            
    return True
"""


#第五题
"""
def triangle(row):
    reduce=[3**i+1 for i in range(10) if 3**i<=100000][::-1]
    
    COLOR = {'GG':'G', 'BB':'B', 'RR':'R', 'BR':'G', 
            'BG':'R', 'GB':'R', 'GR':'B', 'RG':'B', 'RB':'G'}

    for length in reduce:
        while len(row)>=length:
            row=[ COLOR[row[i] + row[i+length-1]] for i in range(len(row)-length+1)]
    return row[0]
"""