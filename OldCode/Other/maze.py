
def mark(maze1,pos):
    maze2=maze1.copy()
    maze2[pos[0]*11+pos[1]]=2
    return maze2

def print_maze(maze):
    for i in range(0, 121):
        if i % 11 == 0:
            print('')
        print(maze[i], end='')
    print("")
def find_path(maze,pos,end):
    mazecopy=mark(maze,pos)
#    print(pos)
 #   print_maze(mazecopy)
    if pos==end:
        print("-------------------------------------------------")
        for i in range(0,121):
            if i%11==0:
                print('')
            print(mazecopy[i],end='')

    if maze[(pos[0]-1)*11+pos[1]]==0:
        postmp1=[pos[0]-1,pos[1]]
     #   mazetmp1=maze
    #    print(postmp1)
    #    print_maze(maze)
        find_path(mazecopy,postmp1, end)
   # print_maze(maze)
    if maze[pos[0]*11+pos[1]-1]==0:
        postmp2=[pos[0],pos[1]-1]
        mazetmp2 = maze
    #    print(postmp2)
     #   print_maze(maze)
        find_path(mazecopy, postmp2, end)
 #   print_maze(maze)
    if maze[pos[0]*11+pos[1]+1]==0:
        mazetmp3 = maze
        postmp3=[pos[0],pos[1]+1]
     #   print(postmp3)
     #   print_maze(maze)
        find_path(mazecopy,postmp3, end)
  #  print_maze(maze)
    if maze[(pos[0]+1)*11+pos[1]]==0:
        mazetmp4 = maze
        postmp4=[pos[0]+1,pos[1]]
    #    print(postmp4)
    #    print_maze(maze)
        find_path(mazecopy, postmp4, end)
 #   print_maze(maze)



if __name__=='__main__':
    maze0 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
            1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1,
            1, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1,
            1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1,
            1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1,
            1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1,
            1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1,
            1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1,
            1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1,
            1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1,
            1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    pos = [1, 1]
    end = [9, 9]
    find_path(maze0,pos,end)
