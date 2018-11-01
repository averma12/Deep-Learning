# import pdb
from helpers import normalize, blur

def initialize_beliefs(grid):
    height = len(grid)
    width = len(grid[0])
    area = height * width
    belief_per_cell = 1.0 / area
    beliefs = []
    for i in range(height):
        row = []
        for j in range(width):
            row.append(belief_per_cell)
        beliefs.append(row)
    return beliefs

def sense(color, grid, beliefs, p_hit, p_miss):
    
    new_beliefs = []
    #print(grid)
    #print(beliefs)
    #
    # TODO - implement this in part 2
    #
    width = len(beliefs[0])
    print(width)
    for arr in range(len(beliefs)):
        
        q = []
        #print(len(arr))
        for i in range(width):
            
            print(i)
            hit = (color == grid[arr][i])
            q.append(beliefs[arr][i] * (hit * p_hit + (1-hit) * p_miss))
        new_beliefs.append(q)
    s = 0
    for arr in new_beliefs:
        s = s + sum(arr)
    for arr in range(len(new_beliefs)):
        
        for i in range(width):
             new_beliefs[arr][i] = new_beliefs[arr][i]/s    
            
    

    return new_beliefs

def move(dy, dx, beliefs, blurring):
    height = len(beliefs)
    width = len(beliefs[0])
    new_G = [[0.0 for i in range(width)] for j in range(height)]
    for i, row in enumerate(beliefs):
        for j, cell in enumerate(row):
            new_i = (i + dy ) % width
            new_j = (j + dx ) % height
            # pdb.set_trace()
            new_G[int(new_i)][int(new_j)] = cell
    return blur(new_G, blurring)