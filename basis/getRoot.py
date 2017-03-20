import math
import os


def get_root(a, b, c):
    delta = b * b - 4 * a * c
    if delta >= 0:
        x1 = (-b + math.sqrt(b * b - 4 * a * c)) / (2 * a)
        x2 = (-b - math.sqrt(b * b - 4 * a * c)) / (2 * a)
        return x1, x2
    else:
        return False


v1 = float(input("a:"))  # 二次项系数
v2 = float(input("b:"))    # 一次项系数
v3 = float(input("c:"))     # 常数项系数
if get_root(v1, v2, v3):
    root1, root2 = get_root(v1, v2, v3)
    if root1 != root2:
        print('root1 = %.2f , root2 = %.2f' % (root1, root2))
    else:
        print("root1 = root2 = %.2f" % root1)
else:
    print("The equation has no real root")

os.system("pause")  
