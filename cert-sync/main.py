import sys
import subprocess
from glob import glob
import urllib2

BLOCK_CHAIN_REQ_ALL = 'localhost:4443/getall'
BLOCK_CHAIN_REQ_CERT = 'localhost:4443/get?domain='

CERT_DIR = 'cert/'

CONFIG_CERT_DIR = '~/.mozilla/firefox/hh5nkz9n.default/'

def addCerts():
    crtFiles = glob(CERT_DIR + '*.crt')
    for s in crtFiles:
        cmd = ''
        cmd += ('certutil ')
        
        cmd += '-A '
        cmd += '-n '
        cmd += '\"' + s.split('/')[1].replace('.crt', '')  + '\" '
        cmd += '-t '
        cmd += '\"TCu,TCu,TCu\" '
        cmd += '-i '
        cmd += 'cert/hi.crt '
        cmd += '-d '
        cmd += CONFIG_CERT_DIR
        
        print(cmd)
        subprocess.call(cmd, shell = True)

    subprocess.call('rm cert/*crt',  shell = True)
    
def writeCertFile(fileName, certText):
    f = open(CERT_DIR + fileName, 'w')
    f.write(certText)
    f.close()

def requestCerts():
    response = urllib2.urlopen(BLOCK_CHAIN_REQ_ALL).read()
    hosts = response.split(',')

    f = open('hosts.txt', 'r')
    hostFileContent = f.read()
    f.close()

    currentHosts = hostFileContent.split(',')

    hostDiff = hosts - currentHosts

    for h in hostDiff:
        response = urllib2.urlopen(BLOCK_CHAIN_REQ_CERT + h).read()
        writeCertFile(h + '.crt', response)

def main():
    requestCerts()
    addCerts()

main()

