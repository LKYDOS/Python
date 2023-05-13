import os

# Exercise 5
if (os.path.isfile('p5.py')):
    try:
        import p5
        print('Load p5.py')
        try:
            print('Testing...')
            test_string = 'Alice was born in 2000 and born in hong kong.'
            test2='dashkdabcascfas'
            actual_ans = []
            actual_ans.append(p5.count_alphabet(test_string))
            actual_ans.append(p5.hksar_capitalization(test_string))
            actual_ans.append(p5.concat(test_string, ' She is 22 now.'))
            actual_ans.append(p5.search(test_string, 'born'))
            actual_ans.append(p5.search(test_string, 'now'))
            actual_ans.append(p5.search(test2, 'cas'))
            actual_ans.append(p5.hksar_capitalization(test2))
            expected_ans = [31, 'Alice wAS boRn in 2000 And boRn in Hong Kong.',
                            'Alice was born in 2000 and born in hong kong. She is 22 now.', 27, -1,8,'dASHKdAbcAScfAS']
            if actual_ans == expected_ans:
                print("You passed all the tests!")
            else:
                print("Wrong answer, you failed the tests!")
        except:
            print('Runtime error when testing TextProcessor, please check your code!')
    except:
        print('Cannot load TextProcessor, please check the class name or syntax.')
else:
    print('Cannot find p5.py, please put p5.py and this test script in the same folder.')
