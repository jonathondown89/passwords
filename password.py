import random
import string


num = string.digits
let = string.ascii_letters
spec = "!@£$%^&*[]{}"


content = num + spec + let
long = 25

password = str().join(random.sample(content, long))

print(f"The randomly generated password is", password)
