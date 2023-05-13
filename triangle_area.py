import os
import math

# Exercise 5
if (os.path.isfile('p4.py')):
    try:
        from p4 import *
        print('Load p4.py')
        # test input
        triangles = [(3,4,5),(3,6,1),(6,8,5),(6,8,10)]

        # expected answers
        expected_ans = [False,
                        6.0,
                        12,
                        True,True,24.0]
        try:
            print('Testing...')
            actual_ans = []

            actual_ans.append(is_obtuse_triangle(triangles[0]))

            actual_ans.append(area(triangles[0]))

            actual_ans.append(perimeter(triangles[0]))

            actual_ans.append(check_invalid(triangles[1]))

            actual_ans.append(is_obtuse_triangle(triangles[2]))

            actual_ans.append(area(triangles[3]))
            if actual_ans == expected_ans:
                print("You passed all the tests!")
            else:
                print("Wrong answer, you failed the tests!")
        except:
            print('Runtime error when testing triangle, please check your code!')
    except:
        print('Cannot load triangle, please check the class name or syntax.')
else:
    print('Cannot find p4.py, please put p4.py and this test script in the same folder.')
