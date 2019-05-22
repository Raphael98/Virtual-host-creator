from shutil import copyfile
from shutil import move
import os
'''
    Create a apache2 virtual host
'''
print('Welcome to the virtual host creator')
domain = input('What\'s the domain name?\n')
path = input('What\'s the absolute path to project dir?\n')

def createFile(domain, path):
    fileName = domain+'.conf';
    copyfile('app.meus.br.conf', fileName)
    file = open(fileName, 'r')
    content = file.read()
    content = content.replace('app.meus.br', domain)
    content = content.replace('/var/www/app', path)
    file = open(fileName, 'w')
    file.write(content)
    file.close()
    return fileName

def moveFile(file):
    move(file, '/etc/apache2/sites-available/'+file)


def addHost(domain):
    file = open('/etc/hosts','r')
    content = f'127.0.0.1       {domain}\n'+file.read()
    file = open('/etc/hosts','w')
    file.write(content)
    file.close()

addHost(domain)
fileName = createFile(domain,path)
moveFile(fileName)

os.system('a2ensite '+domain+'.conf')
os.system('systemctl reload apache2')
print('Right! All files in places.')
print('Dont forget to enable the site (a2ensite app.meus.br)...')
print('to enable mod rewrite.\nGood work!')