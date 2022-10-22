username = input("Enter a username to proceed ")
if len(username) > 15:
    print("Please try a valid nickname in length of 3-15 words")
elif len(username) < 3:
    print("Please try a valid nickname in length of 3-15 words")
else:
    print(f"The username {username} is being set for your profile")