#!/usr/bin/python3

def calc_one():
    print("----------------------------------------")
    print("\tX=10\tX=20\tX=30\tX=40\tX=50\tY law")
    

def calc_two():
    print("----------------------------------------")
    print("z\t20\t30\t40\t50\t60\t70\t80\t90\t100\ttotal\np(Z=z)", end='')

def calc_three():
    print("----------------------------------------")
    int x = 10
    while (x <= 50):
        total = total +

    print("----------------------------------------")


def do_all():
    calc_one()
    calc_two()
    calc_three()

def usage():
    print("USAGE")
    print("\t\t./202unsold a b")
    print("\nDESCRIPTION")
    print("\t\ta\tconstant computed from the past results")
    print("\t\tb\tconstant computed from the past results")

def check_error():
    if (len(sys.argv == 2)):
        if (sys.argv[1] == "-h"):
            usage()
    if (len(sys.argv != 3)):
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

main()