#!/usr/bin/python3
import sys
from math import *

everything = list()
expX = list()
expY = list()

def calc_one(a, b):
    print("\tX=10\tX=20\tX=30\tX=40\tX=50\tY law")
    y = 10
    val = 0.0
    marg = 0.0
    test = 0
    while (y <= 60):
        x = 10
        if (y == 60):
            print("X law", end='')
        else:
            print("Y=%d" %(y), end='')
        while (x <= 50):
            val = ((a - x) * (b - y)) / ((5 * a - 150) * (5 * b - 150))
            marg += val
            if (y == 60):
                var_y = 0
                total = 0.0
                i = test
                while (var_y < 5):
                    total += everything[i]
                    var_y += 1
                    i += 5
                print("\t%0.3f" %(total), end='')
                test += 1
                expX.append(total)
            else:
                everything.append(val)
                print("\t%0.3f" %(val), end='')
            x += 10
        if (y == 60):
            print("\t1")
        else:
            print("\t%0.3f" %(marg))
            expY.append(marg)
            marg = 0.0
        y += 10

def calc_two():
    print("----------------------------------------")
    print("z\t20\t30\t40\t50\t60\t70\t80\t90\t100\ttotal\np(Z=z)", end='')

def calc_three(abs, ordo):
    x = 10
    y = 10
    i = 0
    total = 0.0
    total2 = 0.0

    while (x <= 50):
        total = total + expX[i] * x
        total2 = total2 + expY[i] * x
        i = i + 1
        x = x + 10
    i = 0
    varX = 0.0
    varY = 0.0
    while (i < 5):
        varX = varX + ((i + 1) * 10 - total) * ((i + 1) * 10 - total) * expX[i]
        varY = varY + ((i + 1) * 10 - total2) * ((i + 1) * 10 - total2) * expY[i]
        i = i + 1
    print("\n")
    print("----------------------------------------")
    print("expected value of X:\t%0.1f" %(total))
    print("variance of X:\t%0.1f" %(varX))
    print("expected value of Y:\t%0.1f" %(total2))
    print("variance of Y:\t%0.1f" %(varY))
    print("expected value of Z:\t%0.1f" %(total + total2))
    print("variance of Z:\t%0.1f" %(varX + varY))
    print("----------------------------------------")


def do_all():
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    calc_one(a, b)
    calc_two()
    abs = int(sys.argv[1])
    ordo = int(sys.argv[2])
    calc_three(abs, ordo)

def usage():
    print("USAGE")
    print("\t\t./202unsold a b")
    print("\nDESCRIPTION")
    print("\t\ta\tconstant computed from the past results")
    print("\t\tb\tconstant computed from the past results")

def check_error():
    if (len(sys.argv) == 2):
        if (sys.argv[1] == "-h"):
            usage()
    if (len(sys.argv) != 3):
        exit (84)
    try:
        nb1 = int(sys.argv[1])
        nb2 = int(sys.argv[2])
    except:
        exit (84)
    if (nb1 <= 50 or nb2 <= 50):
        exit (84)

def main():
    check_error()
    do_all()


if __name__ == "__main__":
    main()