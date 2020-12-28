#line drawing functions
def horizontal_line(width,strng): 
    #I: Width and character
    #P: multiplies both
    #O: returns characters multiplied over "width" times
    return width*strng

def vertical_line(shift, height,strng):
    #I: Horizontal shift, how many lines, character
    #P: constructs verticle line
    #O: returns characters with shift,over (height) number of lines
    draw = ""
    for o in range (height):
        for i in range(shift):
            draw+=" "
        draw+=strng
        draw+="\n"
    return draw

def vertical_line2(shift, height,strng):  #used to draw two lines next to each other
    #I: Horizontal shift, how many lines, character
    #P: constructs verticle line
    #O: returns characters with shift,over (height) number of lines
    draw = ""
    for o in range (height):
        for i in range(shift):
            draw+=" "
        draw+=strng*2
        draw+="\n"
    return draw

def two_vertical_lines(width, height, strng):
    #I: total width, how many lines, character
    #P: constructs two vertical lines
    #O:: returns two columns of characters with width and over heigh lines
    draw = ""
    for i in range(height):
        draw+=strng
        for o in range (width-(len(strng)*2)):
            draw+=" "
        draw+=strng
        draw+="\n"
    return draw

#digital numbers 
def number_0(width,strng):      #number 0
    pattern = horizontal_line(width,strng)
    pattern+="\n"
    pattern+=two_vertical_lines(width, 3, strng)
    pattern+= horizontal_line(width,strng)    
    return pattern


def number_1(width, strng):     #number 1
    pattern = vertical_line(width-1, 5, strng)
    return pattern

def number_2(width, strng):
    pattern = horizontal_line(width, strng)
    pattern += "\n"
    pattern+=vertical_line(width-1,1, strng)
    pattern += horizontal_line(width, strng)
    pattern += "\n"
    pattern+=vertical_line(width-(width+1),1, strng)
    pattern += horizontal_line(width, strng)
    return pattern

def number_3(width, strng):
    pattern = horizontal_line(width, strng)
    pattern += "\n"
    pattern+=vertical_line(width-1,1, strng)
    pattern += horizontal_line(width, strng)
    pattern += "\n"
    pattern+=vertical_line(width-1,1, strng)
    pattern += horizontal_line(width, strng)
    return pattern

def number_4(width,strng):
    pattern = two_vertical_lines(width,2,strng)
    pattern+=horizontal_line(width,strng)
    pattern+="\n"
    pattern+=vertical_line(width-1,2,strng)
    return pattern

def number_5(width,strng):
    pattern = horizontal_line(width, strng)
    pattern+="\n"
    pattern+=vertical_line(width-(width+1),1, strng)
    pattern+=horizontal_line(width, strng)
    pattern+="\n"
    pattern+=vertical_line(width-1,1,strng)
    pattern+=horizontal_line(width, strng)
    return pattern

def number_6(width,strng):
    pattern = horizontal_line(width, strng)
    pattern+="\n"
    pattern+=vertical_line(width-(width+1),1,strng)
    pattern += horizontal_line(width, strng)
    pattern+="\n"
    pattern+=two_vertical_lines(width,1,strng)
    pattern += horizontal_line(width, strng)
    return pattern

def number_7(width,strng):
    pattern = horizontal_line(width, strng)
    pattern+="\n"
    pattern+=vertical_line(width-1,4,strng)
    return pattern

def number_8(width,strng):
    pattern = horizontal_line(width, strng)
    pattern+="\n"
    pattern+=two_vertical_lines(width,1,strng)
    pattern += horizontal_line(width, strng)
    pattern+="\n"
    pattern+=two_vertical_lines(width,1,strng)
    pattern+=horizontal_line(width, strng)
    return pattern

def number_9(width,strng):
    pattern = horizontal_line(width, strng)
    pattern+="\n"
    pattern+=two_vertical_lines(width,1,strng)
    pattern += horizontal_line(width, strng)
    pattern+="\n"
    pattern+=vertical_line(width-1,2,strng)
    return pattern

#prints given number
def print_number(num,width,strng):
    if num==0:
        print(number_0(width,strng))
    elif num==1:
        print(number_1(width,strng))
    elif num==2:
        print(number_2(width,strng))
    elif num==3:
        print(number_3(width,strng))
    elif num==4:
        print(number_4(width,strng))
    elif num==5:
        print(number_5(width,strng))
    elif num==6:
        print(number_6(width,strng))
    elif num==7:
        print(number_7(width,strng))
    elif num==8:
        print(number_8(width,strng))
    elif num==9:
        print(number_9(width,strng))
     

#operators
def plus(width,strng):
    if width%2==0:
        pattern= vertical_line2(width//2-1,2,strng)
        pattern+=horizontal_line(width,strng)
        pattern+="\n"
        pattern+=vertical_line2(width//2-1,2,strng)
    else:
        pattern= vertical_line(width-1-(width//2),2,strng)
        pattern+=horizontal_line(width,strng)
        pattern+="\n"
        pattern+=vertical_line(width-1-(width//2),2,strng)
    return pattern

def minus(width,strng):
    pattern= horizontal_line(width,strng)
    return pattern

#checks math
def check_answer(num1,num2,ans,op):
    if op=="-":
        return num1 - num2 ==ans
    if op=="+":
        return num1 +num2 ==ans


