# import numbey module
import numpy as np
# input 2 int and return the sum of them


def J12(a, b):
    return a**2 + 2*(b**2)


def J01(a, b):
    return a**2 + 2*(b**2) + 1

# main function


if __name__ == "__main__":
    x2 = [0, 0.5, 1.0, 1.5]
    u = [-1.0, -0.5, 0.0, 0.5, 1.0]
    for i in range(len(x2)):
        for j in range(len(u)):
            a = x2[i]
            b = u[j]
            x_next = a + b
            J_result = J12(x_next, b)
            # print the sum of them
            # check whether x_next is an element in list x2
            if x_next in x2:
                print("x(2):", x_next, " u:", b, " J:",
                      J_result)
            else:
                print("x(2):", x_next, " u:", b, " not admissible")
        print("\n\r")
