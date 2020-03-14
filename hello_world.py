while (True):
    text = input()
    if (len(text) < 5):
        print('message is too short for me')
    else:
        print('Thanks! text is: ', text)
        print('Bye!')
        break
