
left_border = "[!"
right_border = "!]"
inner = "_"
outter = "_"
name = "Ryequell"
length = 11
for i in range(10):
 print(left_border+inner+name+outter+right_border)


user_input = int(input("I would like to run this, this many times..."))
user_name = str(input("My name is... "))
for r in range(user_input):
  print(user_name)