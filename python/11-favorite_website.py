#!/usr/bin/python3

import webbrowser

print ("1-google  \n2-youtube \n3-gmail")

index= int (input ("Choose 1 ,2 or 3 : "))

websites= {1:'https://www.google.com',
           2:"https://www.youtube.com",
           3:"https://mail.google.com/"}

if  index in websites :
    webbrowser.open_new_tab(websites[index])


print (websites[index])