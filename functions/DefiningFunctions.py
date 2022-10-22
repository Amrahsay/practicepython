def greet_user(nickname,name):#name is parameter
    print('''Hi there!
Welcome abroad ''')
    print(f"{nickname} [{name}]")
#_________
def square(number):
    return  number*number#By default u get "none"as a output is u don't use 'return'
##_________
print("Start")
greet_user("Amrahsay",name="Yash Sharma")#amrahsay is simply positional argument#name here is keyword argument
print("Finish")#You can't write positional argument after key argument
#_________
print(square(number=float(input('Type a number to calculate its square '))))
