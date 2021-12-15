import fbchat
import re
fbchat._util.USER_AGENTS    = ["Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"]
fbchat._state.FB_DTSG_REGEX = re.compile(r'"name":"fb_dtsg","value":"(.*?)"')
from getpass import getpass 
username = 'tranlamphong7504@gmail.com' 
password = 'mitCollege123'
client = fbchat.Client(username, password) 


friend = 'Khoa Tran'
msg = 'hello khoa' 
sent = client.send(fbchat.models.Message( msg), thread_id = int(friend.uid)) 
if sent: 
    print("Message sent successfully!") 