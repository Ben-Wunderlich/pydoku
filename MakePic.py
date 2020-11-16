from PIL import Image, ImageDraw, ImageFont

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
DIMENSIONS = (850, 1100)
FONT = ImageFont.truetype("arial.ttf", 25)


def MakeLine(drawn, start, end, width):
    drawn.line((start, end), fill=BLACK, width=width)

BORDER = 150
FROM_TOP = 100
SEP = 145 #needs to be this
SMOL_SEP = 48
TOP_ADD = 435 + 50

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
    TOP_ADD = 435 + 50

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

    #MakeLine(drawn, (BORDER, 100), (DIMENSIONS[0]-BORDER, 100), 3)

def AddAllText(drawn, numbers1, numbers2, pageNum):
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

def main(numbers1, numbers2, page):
    #print("weewoo")
    img = Image.new('RGB', DIMENSIONS, color = WHITE)
    drawn = ImageDraw.Draw(img)

    CreateAllLines(drawn)
    AddAllText(drawn, numbers1, numbers2, page)
    #d.text((10,10), "Hello world", font=FONT, fill=BLACK)

    
    img.save('page1.pdf')
    img.show()

if __name__ == "__main__":
    main(1,1)