# if the name and password entered correctly it will show a welcome message
# esle it will print incorrect message and ask you if you want to try again

user_name = ['Ahmed','Ali','Amr']
password = [1394,6078,9345]

flag = 1



while flag == 1:

    name = input("please enter the name :\n")

    if name in user_name:

        passcode = int(input("please enter the password:\n"))
        index = user_name.index(name)

        if passcode == password[index]:
            
            print("welcome " + name)
            flag = 0

        else :

            print('incorrect password')
            flag = int(input("to try again enter 1 to exit enter 0:\n"))

    else:

        print("incorrect name")
        flag = int(input("to try again enter 1 to exit enter 0:\n"))