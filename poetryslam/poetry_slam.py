#open file and print lines with line number
def get_file_lines(filename):
    poem = filename
    openpoem = open(poem, "r")
    poem_lines = openpoem.readlines()
    
    #adding lines to poem list from txt file
    for line in poem_lines:
        poem_list.append(line)
    openpoem.close()
    
    #adding line number to lines and printing to console
    line_count = 1
    for line in poem_list:
        print( str(line_count) + " " + line)
        line_count+=1

#print lines backwards from poem list
def lines_printed_backwards(lines_list):
    backward_list = []
    list_length = len(lines_list)
    #last index starts at negative one
    num = -1
    #want to access and print lines from poem list backwards so I am using negative indexes
    while num < list_length:
        
        #stop loop when we reach the last line
        if (num * -1) -1 == list_length:
            break


        line = lines_list[num]
        backward_list.append(line)
        num -= 1
    
    
    for line in backward_list:
        print( str(list_length) + " " + line)
        list_length-=1



#want to use this list in and out of the function       
poem_list = []
get_file_lines("poetryslam/poem.txt")
#print statement to separate the regular and backward list
print("------------------------------------------------------------------------")
lines_printed_backwards(poem_list)


    
