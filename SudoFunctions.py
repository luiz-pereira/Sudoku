import sys
import random


def pick_random_empty_cell(sudoku):
    cellchosen=0
    countzero=sudoku.count(0)
    cellzerochosen = random.randint(1,countzero+1)
    contador=0
    for i in range(0,81):
        if sudoku[i]==0:
            contador=contador+1
        if contador == cellzerochosen:
            cellchosen = i
            break
    return cellchosen

def pick_next_empty_cell(sudoku):
    cellchosen = 0
    for i in range(0,81):
        if sudoku[i]==0:
            cellchosen = i
            break
    return cellchosen

def pick_last_empty_cell(sudoku):
    cellchosen = 0
    for i in range(len(sudoku)-1,-1,-1):
        if sudoku[i]==0:
            cellchosen = i
            break
    return cellchosen

def get_listx(cell,sudoku):
    line = (cell)//9
    linestart = line*9
    lineend=line*9+8
    return sudoku[linestart:lineend+1]

def get_listy(cell, sudoku):
    column = cell % 9
    return sudoku[column:column+73:9]


def get_listbox(cell, sudoku):
    linebox = ((cell)//9) % 3
    columnbox= cell % 9 % 3
    cellstart = cell - 9*linebox - columnbox
    listbox = sudoku[cellstart:cellstart+3]
    listbox.extend(sudoku[cellstart+9:cellstart+9+3])
    listbox.extend(sudoku[cellstart + 9 + 9:cellstart + 9 + 9 + 3])
    return listbox

def list_possibilities(cell, sudoku):
    list_x = get_listx(cell, sudoku)
    list_y = get_listy(cell, sudoku)
    list_box = get_listbox(cell, sudoku)
    list_possibilities= [1,2,3,4,5,6,7,8,9]
    list_possibilities=list(set(list_possibilities)-set().union(list_x,list_y,list_box))
    return list_possibilities

def put_sudo_txt(sudoku, outfile):
    strtxt = ""
    for i in range(0, 81):
        if sudoku[i] == 0:
            strtxt = strtxt + " |"
        else:
            strtxt = strtxt + str(sudoku[i]) + "|"
            a = (i + 1) % 9
        if (i + 1) % 9 == 0:
            strtxt = strtxt + "\n"
    with open(outfile, "w") as text_file:
        print(strtxt, file=text_file)

def fill_pencils(sudoku):
    pencils = [0 for i in range(0,81)]

    for i in range(0,81):
        if sudoku[i]>0:
            pencils[i] = sudoku[i]
        else:
            pencils[i]=list_possibilities(i,sudoku)
    return pencils

def fill_stupid(pencils):
    newcell = False
    worklist=pencils.copy()
    for i in range(0,81):
        if type(pencils[i]) is int:
            worklist[i]=pencils[i]
        else:
            if len(pencils[i])==1:
                worklist[i] = pencils[i][0]
                newcell = True
            else:
                worklist[i] = 0
    return worklist,newcell

def check_solution(sudoku):
    check_solution=True
    for cell in range (0,81):
        if not sudoku[cell]==0:
            list_x = get_listx(cell, sudoku)
            list_y = get_listy(cell, sudoku)
            list_box = get_listbox(cell, sudoku)
            if list_x.count(sudoku[cell])>1:
                check_solution=False
                break
            if list_y.count(sudoku[cell])>1:
                check_solution=False
                break
            if list_box.count(sudoku[cell])>1:
                check_solution=False
                break
    return check_solution

def solve_sudoku(sudoku):
    listsudotest = sudoku.copy()
    listpencil = fill_pencils(sudoku)
    listpenciltest = listpencil.copy()
    listsudotest, newcell = fill_stupid(listpenciltest)
    listpenciltest = fill_pencils(listsudotest)

    solution = False

    for i in range(0, 5000):
        nextCell = pick_next_empty_cell(listsudotest)
        i = nextCell
        listsudotest[nextCell] = listpenciltest[nextCell][0]
        optionused = listsudotest[nextCell]
        newcell = True
        nosolution = False
        listsudotest2 = listsudotest.copy()

        while newcell:
            listpenciltest2 = fill_pencils(listsudotest2)
            if listpenciltest2.count([]) > 0:
                nosolution = True
                break
            listsudotest2, newcell = fill_stupid(listpenciltest2)
            if listsudotest2.count(0) == 0:
                if check_solution(listsudotest2):
                    solution = True
                else:
                    nosolution = True
                break
        if solution:
            put_sudo_txt(listsudotest2, "solution.txt")
            break

        if nosolution:
            moreoptions = False
            while not moreoptions:
                listsudotest[nextCell] = 0
                listpenciltest = fill_pencils(listsudotest)
                while not optionused == listpenciltest[nextCell][0]:
                    listpenciltest[nextCell].pop(0)
                if len(listpenciltest[nextCell]) == 1:
                    nextCell = pick_last_empty_cell(sudoku[0:nextCell])
                    optionused = listsudotest[nextCell]
                    listpenciltest[nextCell] = listpencil[nextCell]
                else:
                    listpenciltest[nextCell].pop(0)
                    listpenciltest[nextCell + 1:81] = listpencil[nextCell + 1:81]
                    listsudotest[nextCell + 1:81] = sudoku[nextCell + 1:81]
                    moreoptions = True
        else:
            listpenciltest = fill_pencils(listsudotest)
        if listsudotest.count(0) == 0:
            break

    put_sudo_txt(listsudotest, "puzzle.txt")

def make_sudo (numberofcells):
    listsudo17 = []

    for i in range(0,81):
        listsudo17.insert(i,0)

    contador = 0
    for i in range(0,numberofcells):
        contador = contador + 1
        nextCell = pick_random_empty_cell(listsudo17)
        if i<8:
            list_distinct = list(set(listsudo17) - {0})
            list_free = list(set(list_possibilities(nextCell,listsudo17))-set(list_distinct))
        else:
            list_free = list_possibilities(nextCell,listsudo17)
        listsudo17[nextCell]=random.sample(list_free,1)[0]
    return listsudo17


#x= input("digite o sudoku:")
#x=[int(i) for i in x]
#if not len(x)<81:
x=make_sudo(17)
solve_sudoku(x)