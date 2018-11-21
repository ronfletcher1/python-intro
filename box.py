# Print a Box
# Given a height and width, input by the user, print a box consisting of * characters as its border. Example session:

# $ python box.py
# Width? 6
# Height? 4
# ******
# *    *
# *    *
# ******

height = raw_input("what is the height of the box?")
width = raw_input("what is the width of the box?")
linetb = ""
lineside = ""
for i in range(0,int(width)):
    linetb = linetb + "*"
    if i == 0 or i == int(width) - 1:
        lineside = lineside + "*"
    else:
        lineside = lineside + " "
for i in range(0,int(height)):
    if i == 0 or i == int(height) - 1:
        print linetb
    else:
        print lineside
    



