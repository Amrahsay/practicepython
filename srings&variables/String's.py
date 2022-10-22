print("This is to practise how sting's works")
comment='''
Hello user

Here is our first message to you.

Thank you for using the service,
The Author

'''
print(comment)
print('_'*20)
print(comment[20])
print('_'*20)
print(comment[2:20])
print('_'*20)
print(comment[:])
print('_'*20)
print(comment[:20])
print('_'*20)
print(comment[20:])
print('_'*20)
print(comment[-20])
print('_'*20)
print(comment[2:-2])
print('_'*20)
name= 'Yash Sharma'
print(name[1:-1])
print('_'*20)
FirstName= name[0:4]
LastName= name[5:]
print(FirstName)
print(LastName)
print('_'*20)
msg= f'{FirstName} [{LastName}] is a coder'
lmsg= len(msg)
print(msg)
print(lmsg)
print('_'*20)
print(msg.title())
print('_'*20)
print(msg.lower())
print(msg.upper())
print(msg)
print('_'*20)
print(msg.find('a'))
print(msg.replace('a coder','Amrahsay'))
print('coder' in msg)
print('_'*20)
