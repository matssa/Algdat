#!/usr/bin/python3                              #husk å endre dette etterpå!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


#from sys import stdin                          #husk å endre dette etterpå!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


def max_value(widths, heights, values, paper_width, paper_height):
    return 0


def main():
    f = open('input7.txt', 'r')
    widths, heights, values = [], [], []
    sedler = []
    for triple in f.readline().split():
        dim_value = triple.split(':', 1)
        dim = dim_value[0].split('x', 1)
        width = int(dim[0][1:])
        height = int(dim[1][:-1])
        value = int(dim_value[1])
        widths.append(int(width))
        heights.append(int(height))
        values.append(int(value))
        for 

    print(widths, heights, values)

    for line in f:
        #for line in stdin:
        x = 0
        print((max_value(0, 0, 0, 0, 0)))




    f.close()                                   #fjern!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

if __name__ == "__main__":
    main()