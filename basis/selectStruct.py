#选择结构的小程序示例

import os

print('This is a health test program !')
print("Let's start the first step ！")
height=float(input("Pls input your height (unit:m):"))
weight=float(input("Next input your weight (unit:kg):"))

bmi=weight/(height*height)


if bmi>32:
    print('严重肥胖')
elif bmi>28:
    print('肥胖')
elif bmi>25:
    print('过重')
elif bmi>18.5:
    print('正常')
else:
    print('过轻')
    

print('The test has finished !')
print('Thank you !')

os.system("pause")
