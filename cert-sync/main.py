#! /usr/bin/python

import sys
import subprocess
from glob import glob
import requests

BLOCK_CHAIN_REQ_ALL = 'localhost/getall'
BLOCK_CHAIN_REQ_CERT = 'localhost/get?domain='

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
    URL = BLOCK_CHAIN_REQ_ALL
    r = requests.get(url=URL)

    hosts = response.text.split(',')

    f = open('hosts.txt', 'r')
    hostFileContent = f.read()
    f.close()

    currentHosts = hostFileContent.split(',')

    hostDiff = hosts - currentHosts

    for h in hostDiff:
        URL = BLOCK_CHAIN_REQ_CERT + h
        r = requests.get(url=URL)
        writeCertFile(h + '.crt', r.text)

    f = open('hosts.txt', 'w')
    f.write(hosts)

def main():
    requestCerts()
    addCerts()

main()

