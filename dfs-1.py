#! python3

# imports
import tkinter
import random

# initialisation
window = tkinter.Tk()
window.resizable(width = False, height = False)
window.title("Maze Creator 1")
window.geometry("500x500")

background = tkinter.Canvas(window, width = 500, height = 500, background="#000", bd=0, highlightthickness=0)
background.pack()

class Cell:
    def __init__(self, x, y):
        self.object = background.create_rectangle(x, y, x+10, y+10, fill="#000", outline="")
        self.visited = False
        self.pos = [int(x/10), int(y/10)]

    def unwall(self):
        background.itemconfig(self.object, fill="#FFF")
        self.visited = True

    def adjacent(self, full = False):
        temp = []
        if (self.pos[0]-1 >= 0): temp.append(Cells[self.pos[1]][self.pos[0]-1])
        if (self.pos[0]+1 <= 49): temp.append(Cells[self.pos[1]][self.pos[0]+1])
        if (self.pos[1]-1 >= 0): temp.append(Cells[self.pos[1]-1][self.pos[0]])
        if (self.pos[1]+1 <= 49): temp.append(Cells[self.pos[1]+1][self.pos[0]])
        return temp

def motion():
    global pos
    current = Cells[pos[1]][pos[0]]
    current.visited = True
    current.unwall()
    adjacent = current.adjacent()
    print('Current: %s' % (current.pos))
    print([cell.pos for cell in adjacent])
    for i in reversed(range(len(adjacent))):
        if (adjacent[i].visited == True): # adjacent = [cell for cell in adjacent if cell.visited == False]
            del adjacent[i]
        else: # difficult with [x for x]
            for temp in adjacent[i].adjacent():
                if (temp.visited == True and temp.pos != current.pos):
                    del adjacent[i]
                    break
    print([cell.pos for cell in adjacent])
    if (len(adjacent)-1 < 0): # backtracking
        try:
            pos = queue[-1]
            del queue[-1]
        except IndexError:
            print('Finished!')
    else:
        queue.append(pos)
        pos = adjacent[random.randint(0, len(adjacent)-1)].pos
    window.after(20, motion)

Cells = [[Cell(x, y) for x in range(0, 500, 10)] for y in range(0, 500, 10)]

pos = [0, 4]
queue = []

motion()
window.mainloop()
