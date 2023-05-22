flag = True


class NegativeException(Exception):
    pass


while flag:
    while True:
        try:
            user_input = int(input("Please enter a number: "))
            if user_input < 0:
                raise NegativeException
            break
        except (ValueError, NegativeException) as error:
            print("Oops!  That was no valid number.  Try again...")

    list1 = [int(x) for x in str(user_input)]
    left = 0
    right = len(list1) - 1
    for count in range(len(list1) // 2):
        if list1[left] != list1[right]:
            print('this is not a palindrome number')
            break
        if count == len(list1) // 2 - 1:
            flag = False
            break
print('this is a palindrome number')
