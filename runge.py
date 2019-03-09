import parser, math, PyQt5


def parseEquation(exp):
    return parser.expr(exp).compile()

def f(exp, x,y):
    return eval(exp)

def RungeKutta(xmax, exp, x, y, h):
    if x+h >= xmax:
        return []
    else:
        k1 = h * f(exp,x,y)
        k2 = h * f(exp,x+h/2,y+k1/2)
        k3 = h * f(exp,x+h/2,y+k2/2)
        k4 = h * f(exp,x+h,y+k3)
        ans = y + (1/6*(k1 + 2*k2 + 2*k3 + k4))
        return [ans] + RungeKutta(xmax,exp,x+h,ans,h)



if __name__ == "__main__":
    way = int(input("1 -- hands. 2 -- from file"))
    if way == 1:
        exp = parseEquation(input("Enter f(x) = "))
        y = float(input("Enter y0: "))
        x = float(input("Enter x0: "))
        h = float(input("Enter step size: "))
        xmax = float(input("Enter xmax: "))
    if way == 2:
        with open ("data.txt", "r") as myfile:
            data = myfile.readlines()
            print(data)
            exp = parseEquation(data[0])
            y = float(data[1])
            x = float(data[2])
            h = float(data[3])
            xmax = float(data[4])

    ans = RungeKutta(xmax,exp,x,y,h)
    track = h
    f = open('output.txt', 'w')
    for i in ans:
        print("y{:.2f} = {:.5f}".format(track, i))
        f.write("y{:.2f} = {:.5f}".format(track, i) + "\n")
        track += h