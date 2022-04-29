import sys


def checknumber(x):
    if x == 0:
        print(f"{x} is zero and neither odd or even!")
    elif x % 2 == 0:
        print(f"{x} is even!")
    else:
        print(f"{x} is odd!")


if len(sys.argv) == 3:
    if sys.argv[1] == "-i":
        inputuser = sys.argv[2]
        if inputuser.isalpha():
            print(f"{inputuser} is not a number!")
            print("The argument must be number!")
        else:
            checknumber(int(inputuser))
    else:
        print("The correct argument is -i <input>")
else:
    print("Wrong argument!")
    print("The correct argument is -i <input>")
