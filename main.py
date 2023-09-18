import requests
from user_agent import generate_user_agent
import pyfiglet
from pyfiglet import figlet_format
import colorama
colorama.init()
Z = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
Z1 = '\033[2;31m' #احمر ثاني
F = '\033[2;32m' #اخضر
A = '\033[2;34m'#ازرق
C = '\033[2;35m' #وردي
B = '\033[2;36m'#سمائي
Y = '\033[1;34m' #ازرق فاتح
logo = pyfiglet.figlet_format('*Headers*')
print(logo)
print(X+'* '*15+A)
url = input('EnTer uRl : ')
yahia = requests.get(url)
k = print(yahia.headers)

