#Author: Jacob Neaderland
#setting the 4 original colors
colors = ["red", "green", "blue", "yellow"]
#print statements for me to check
print (colors)
#adding to the list
colors.extend (["purple", "teal", "pink"])
print (colors)
#adding even more
colors.insert (0, "black")
print (colors)
colors.insert (3, "white")
print (colors)
#cloning the list
color2 = colors[:]
print (color2)
#removing an item from the list
color2.remove ("red")
print (color2)