import sys

def demo(x):
    output = "AB"
    for i in range(x):
        temp = ""
        for l in output:
            if (l == 'A'):
                temp += "AB"
            else:
                temp += "BA"
        output = temp
    print(output)

demo(int(sys.argv[1]))
