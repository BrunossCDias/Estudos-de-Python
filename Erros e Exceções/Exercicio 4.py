import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://pudim.com.br/')
except urllib.error.URLError:
    print('O endereço que esta tentando acessar, não esta disponivel no momento')
else:
    print("O endereço solicita esta diponivel para acesso.")
    print(site.read())
