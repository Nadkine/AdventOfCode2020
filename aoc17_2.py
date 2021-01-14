import numpy as np
import copy

sizecube = 28
half = int((sizecube-1)/2)
cube = np.zeros(shape =(sizecube,sizecube,sizecube,sizecube),dtype='int8')

def checkneighbors(cube,x,y,z,w):
    thesum = cube[x-1:x+2,y-1:y+2,z-1:z+2,w-1:w+2].sum()
    own = cube[x,y,z,w]
    return (thesum-own), own

with open('data17.txt','r') as f:
   for index,line in enumerate(f.readlines()):
       for jindex, letter in enumerate(line):
           if letter == '#':
              cube[14][14][13+index][13+jindex] = 1


#print(cube[13:16,13:16,13:16,13:16])

for i in range(6):
    print("---------")
    cube_copy = copy.deepcopy(cube)
    for x in range(0,cube.shape[0]-1):
        for y in range(0,cube.shape[1]-1):
            for z in range(0,cube.shape[2]-1):  
                for w in range(0,cube.shape[3]-1):  
                    neighbours,_ = checkneighbors(cube,x,y,z,w)
                    if cube[x,y,z,w] == 1 and (neighbours == 2 or neighbours ==3):
                        cube_copy[x,y,z,w] = 1
                    elif cube[x,y,z,w] == 1:
                        cube_copy[x,y,z,w] = 0
                    elif cube[x,y,z,w] == 0 and neighbours == 3:
                        cube_copy[x,y,z,w] = 1
    print(cube_copy[13:16,13:16,13:16])
    cube = cube_copy
print(cube.sum())

