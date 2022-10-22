customer = {
    "name": "Amrahsay",
    "age": 22,
    "is_verified": True
}
print(customer.get("birthdate"))
customer["birthdate"] = "march 2 2000"
print(customer["birthdate"])
print(customer.get("sex", "male"))
customer['name']= 'Yash Sharma'
print(customer["name"])
phoneNumber = input("Number: ")
digits_mapping = {
    '0':'zero',
    '1':'one',
    '2':'two',
    '3':'three',
    '4':'four',
    '5':'five',
    '6':'six',
    '7':'seven',
    '8':'eight',
    '9':'nine',
}
output = ""
for char in phoneNumber:
    output += digits_mapping.get(char,"!") + " "
print(output)
print('_'*20)

message = input(">")
words = message.split(' ')
emojis = {
    ":)":"😊",
    ":(":"☹"
}
output = ''
for word in words:
    output +=emojis.get(word, word) + ' '
print(output)