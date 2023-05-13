import os

# Exercise 1
if (os.path.isfile('p1.py')):
    try:
        from p1 import check_sublist
        print('Load p1.py')
        #check_sublist([321,33,22,80,13,288],266,88,76)
        test1 = [[321,33,22,80,13,288]]
        test2 = [266]
        test3 = [88]
        test4=[76]
        expected1 = [([33, 22, 13], [33, 22, 80, 13], [33, 22, 80, 13])]
        # check_sublist([22,25,321,123],23,20,1)
        test5=([[22,25,321,123]])
        test6=[23]
        test7=[20]
        test8=[1]
        expected2=[([], [22, 25], [22])]
        # check_sublist([203,312,31241,13],3213,432,213)
        test9=([[203,312,31241,13]])
        test10=[3213]
        test11=[432]
        test12=[213]
        expected3=[([203, 13], [203, 312, 13], [203, 312, 13])]
        try:
            print('Testing...')
            answer1 = list(map(check_sublist, test1, test2, test3,test4))
            answer2 = list(map(check_sublist, test5, test6, test7, test8))
            answer3 = list(map(check_sublist, test9, test10, test11, test12))
            print(answer1)
            print(answer2)
            if set(answer1[0][0]) == set(expected1[0][0]) and set(answer1[0][1]) == set(expected1[0][1]) and set(answer1[0][2]) == set(expected1[0][2])\
                    and set(answer2[0][0]) == set(expected2[0][0]) and set(answer2[0][1]) == set(expected2[0][1]) and set(answer2[0][2]) == set(expected2[0][2]) \
                    and set(answer3[0][0]) == set(expected3[0][0]) and set(answer3[0][1]) == set(expected3[0][1]) and set(answer3[0][2]) == set(expected3[0][2]):
                print("You passed all the tests!")
            else:
                print("Wrong answer, you failed the tests!")
        except:
            print('Runtime error when testing check_sublist, please check your code!')
    except:
        print('Cannot load check_sublist, please check the function name or syntax.')
else:
    print('Cannot find p1.py, please put p1.py and this test script in the same folder.')
