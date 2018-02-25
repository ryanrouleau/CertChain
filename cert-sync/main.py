import sys
import subprocess
from glob import glob

CERT_HEADER = '-----BEGIN CERTIFICATE-----'
CERT_FOOTER = '-----END CERTIFICATE-----'

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
    f.write(CERT_HEADER + '\n')
    f.write(certText)
    f.write(CERT_FOOTER + '\n')
    f.close()

def requestCerts():
    

    return certs

def main():
    addCerts()

main()

