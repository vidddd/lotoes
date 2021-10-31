import secrets
import string
from werkzeug.security import generate_password_hash
  
alphabet = string.ascii_letters + string.digits
password = ''.join(secrets.choice(alphabet) for i in range(90))

password = ''
print(generate_password_hash(password))