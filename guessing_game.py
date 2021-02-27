secret_no = 5
guess_count = 0
while guess_count < 3 :
    num = input('Guess the number: ')
    try :
        guess = float(num)
    except :
        print('Please enter a number...')
        exit()
    guess_count += 1
    if guess == secret_no :
        print('Correct')
        break
else :
    print('Failed! Try again...')