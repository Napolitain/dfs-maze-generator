#! python3

# imports
import tkinter
import random

# initialisation
window = tkinter.Tk()
window.resizable(width = False, height = False)
window.title("Maze Creator 2")
window.geometry("500x500")

background = tkinter.Canvas(window, width = 500, height = 500, background="#000", bd=0, highlightthickness=0)
background.pack()

class Wall:
    def __init__(self, x, y, d):
        if (d == 'down'):
            self.object = background.create_rectangle(x, y+9, x+10, y+11, fill="#FFF", outline="")
        else:
            self.object = background.create_rectangle(x+9, y, x+11, y+10, fill="#FFF", outline="")

class Cell:
    def __init__(self, x, y):
        self.object = background.create_rectangle(x, y, x+10, y+10, fill="#000", outline="")
        self.visited = False
        self.pos = [int(x/10), int(y/10)]
        self.walls = {'down':Wall(x, y, 'down'), 'right':Wall(x, y, 'right')}

    def unwall(self):
        if (newpos[0] < pos[0]):
            background.delete(Cells[newpos[1]][newpos[0]].walls['right'].object)
            del Cells[newpos[1]][newpos[0]].walls['right']
        elif (newpos[1] < pos[1]):
            background.delete(Cells[newpos[1]][newpos[0]].walls['down'].object)
            del Cells[newpos[1]][newpos[0]].walls['down']
        elif (newpos[0] > pos[0]):
            background.delete(self.walls['right'].object)
            del self.walls['right']
        else:
            background.delete(self.walls['down'].object)
            del self.walls['down']
        self.visited = True

    def adjacent(self, full = False):
        temp = []
        if (self.pos[0]-1 >= 0): temp.append(Cells[self.pos[1]][self.pos[0]-1])
        if (self.pos[0]+1 <= 49): temp.append(Cells[self.pos[1]][self.pos[0]+1])
        if (self.pos[1]-1 >= 0): temp.append(Cells[self.pos[1]-1][self.pos[0]])
        if (self.pos[1]+1 <= 49): temp.append(Cells[self.pos[1]+1][self.pos[0]])
        return temp

def motion():
    global pos, newpos
    current = Cells[pos[1]][pos[0]]
    current.visited = True
    adjacent = current.adjacent()
    print('Current: %s' % (current.pos))
    print([cell.pos for cell in adjacent])
    for i in reversed(range(len(adjacent))):
        if (adjacent[i].visited == True): # adjacent = [cell for cell in adjacent if cell.visited == False]
            del adjacent[i]
    print([cell.pos for cell in adjacent])
    if (len(adjacent)-1 < 0): # backtracking
        try:
            pos = queue[-1]
            del queue[-1]
        except IndexError:
            print('Finished!')
    else:
        queue.append(pos)
        newpos = adjacent[random.randint(0, len(adjacent)-1)].pos
        current.unwall()
        pos = newpos
    window.after(10, motion)

Cells = [[Cell(x, y) for x in range(0, 500, 10)] for y in range(0, 500, 10)]

pos = [0, 4]
newpos = []
queue = []

input() # wait
motion()
window.mainloop()
