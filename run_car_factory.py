from car_factroy_functions import *
if __name__ == '__main__':
    while True:
        print('Lets make a car. WWWOOOOWWW!!')
        print('what do you need to make a car?')
        user_input = input('Do you know the requirements: \n'
                           'yes or no\n').strip().lower()
        if user_input == 'yes':
            user_arg1 = input('Do you the first requirement: \n')
            user_arg2 = input('Do you the second requirement: \n')
            print(make_parts(user_arg1,user_arg2))
        elif user_input == 'no':
            print('So what do you need to do? \n')
        elif user_input == 'exit':
            print('You Have now exited the program')
            break
        else:
            print('YOU FOUL, awnser the question')
            print('Try again\n'
                  'and again till you get it right.......')
else:
    print('wrong file')