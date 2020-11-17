from PIL import Image, ImageDraw, ImageFont
import os
import re

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
DIMENSIONS = (850, 1100)
FONT = ImageFont.truetype("arial.ttf", 26)

BORDER = 205
FROM_TOP = 100
SEP = 145 #needs to be this
SMOL_SEP = 48
TOP_ADD = 435 + 50

###########################

PUZZLE_FILE_PREFIX = "page"
currFolder = os.path.dirname(__file__)
PUZZLE_FOLDER = os.path.join(currFolder, "puzzles")

if not os.path.exists(PUZZLE_FOLDER):
    os.mkdir(PUZZLE_FOLDER)

PATTERN = "^{}(\d+).pdf$".format(PUZZLE_FILE_PREFIX)
COMPILED = re.compile(PATTERN)

##############################

ANSWER_FILE_PREFIX = "answerspage"
ANSWER_FOLDER = os.path.join(currFolder, "answers")

if not os.path.exists(ANSWER_FOLDER):
    os.mkdir(ANSWER_FOLDER)


def MakeLine(drawn, start, end, width):
    drawn.line((start, end), fill=BLACK, width=width)


def CreateAllLines(drawn):
    #first outline
    for i in range(4):#horzontal
        MakeLine(drawn, (BORDER, FROM_TOP+SEP*i), (BORDER+SEP*3, FROM_TOP+SEP*i), 3) 
    
    for i in range(4):#vertical
        MakeLine(drawn, (BORDER+SEP*i, FROM_TOP), (BORDER+SEP*i, FROM_TOP+SEP*3), 3)

    #first fine lines
    for i in range(0, 435, SMOL_SEP):#horiz mini
        if i > 435-SMOL_SEP:
            break
        MakeLine(drawn, (BORDER, FROM_TOP+i), (BORDER+SEP*3, FROM_TOP+i), 1)

    for i in range(0, 435, SMOL_SEP):#vertical mini
        if i > 435-SMOL_SEP:
            break
        MakeLine(drawn, (BORDER+i, FROM_TOP), (BORDER+i, FROM_TOP+SEP*3), 1)

    ##second box

    #first outline
    for i in range(4):#horzontal
        MakeLine(drawn, (BORDER, FROM_TOP+SEP*i + TOP_ADD), (BORDER+SEP*3, FROM_TOP+SEP*i + TOP_ADD), 3) 
    
    for i in range(4):#vertical
        MakeLine(drawn, (BORDER+SEP*i, FROM_TOP+ TOP_ADD), (BORDER+SEP*i, FROM_TOP+SEP*3 + TOP_ADD), 3)

    #first fine lines
    for i in range(0, 435, SMOL_SEP):#horiz mini
        if i > 435-SMOL_SEP:
            break
        MakeLine(drawn, (BORDER, FROM_TOP+i+ TOP_ADD), (BORDER+SEP*3, FROM_TOP+i+ TOP_ADD), 1)

    for i in range(0, 435, SMOL_SEP):#vertical mini
        if i > 435-SMOL_SEP:
            break
        MakeLine(drawn, (BORDER+i, FROM_TOP+ TOP_ADD), (BORDER+i, FROM_TOP+SEP*3+ TOP_ADD), 1)

def AddAllText(drawn, numbers1, numbers2, pageNum, isAnswerKey):
    PADDING = 15

    for x, row in enumerate(numbers1):#top puzzle
        for y, value in enumerate(row):
            if value != -1:
                #print("value is", value)
                MakeText(drawn, y*SMOL_SEP + BORDER+PADDING, x*SMOL_SEP+FROM_TOP+PADDING, value)

    for x, row in enumerate(numbers2):#bottom puzzle
        for y, value in enumerate(row):
            if value != -1:
                #print("value is", value)
                MakeText(drawn, y*SMOL_SEP + BORDER+PADDING, x*SMOL_SEP+FROM_TOP+PADDING+TOP_ADD, value)

    #add page number
    MakeText(drawn, DIMENSIONS[0]-70, DIMENSIONS[1]-50, pageNum)

def MakeText(drawn, x, y, value):
    drawn.text((x, y), str(value),BLACK, font=FONT)

def NewFileName():
    #check to see what highest suffix is
    maxNum = 0
    for file in os.listdir(PUZZLE_FOLDER):
        numStr = re.findall(COMPILED, file)
        if len(numStr) == 0:
            continue
        numStr = int(numStr[0])

        if numStr > maxNum:
            maxNum = numStr

    newNum = maxNum+1

    newName = PUZZLE_FILE_PREFIX+str(newNum)+".pdf"
    ansName = ANSWER_FILE_PREFIX+str(maxNum)+".pdf"
    ansPath = os.path.join(ANSWER_FOLDER, ansName)
    return newNum, os.path.join(PUZZLE_FOLDER, newName), ansPath


def MakePage(numbers1, numbers2, isAnswerKey):
    img = Image.new('RGB', DIMENSIONS, color = WHITE)
    drawn = ImageDraw.Draw(img)

    CreateAllLines(drawn)

    pgNum, pgPath, ansPath = NewFileName()
    if isAnswerKey:
        pgNum -= 1

    AddAllText(drawn, numbers1, numbers2, pgNum, isAnswerKey)
    if(isAnswerKey):
        img.save(ansPath)
    else:
        img.save(pgPath)

    return pgNum

if __name__ == "__main__":
    input("This file is not to be run, try running main.py\n\npress enter to exit this")