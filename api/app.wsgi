import sys
sys.path.insert(0, '/var/www/phishing-api')

activate_this = 'venv'
with open(activate_this) as file_:
  exec(file.read(), dict(__file__=activate_this))

from app import app as application