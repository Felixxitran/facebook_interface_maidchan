import fbchat 
from getpass import getpass

username = 'tranlamphong7504@gmail.com'
password = 'mitCollege123'
client = fbchat.Client(username, password)

no_of_friends = int(raw_input("Number of friends: ")) 

for i in xrange(no_of_friends): 
    
    name = str(raw_input("Name: "))
    
    friends = client.searchForUsers(name)  # return a list of names
    
    friend = friends[0]
    
    msg = raw_input("Message: ") 
    
    sent = client.send(Message(text = msg), thread_id = int(friend.uid), thread_type=ThreadType.USER)
    
    if sent: 
        
        print("Message sent successfully!")