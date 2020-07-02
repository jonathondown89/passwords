import random
import string


numerical = string.digits
letters = string.ascii_letters
special = "!@£$%^&*[]{}"


content = letters + special + numerical
long = 25

password = ''.join(random.sample(content, long))

print(f"The random password is", password)




