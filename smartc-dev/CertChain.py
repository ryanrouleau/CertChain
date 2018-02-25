from boa.blockchain.vm.Neo.Storage import GetContext, Put, Delete, Get
from boa.code.builtins import concat


def Main(operation, args):
    """
    Main definition for CertChain 
    :param operation: the operation to be performed
    :type operation: str
    :param args: list of arguments.
        args[0] is domain name in operations of get_cert and put_cert
        args[1] is certificate string in operation of put_cert
    :param type: str
    :return:
        bytearray: The result of the operation
    """
    
    if operation == "put_cert":
        if len(args) > 1:
            domain = args[0]
            cert = args[1]
            return put_cert(domain, cert)

    if operation == "get_cert":
        if len(args) > 0:
            domain = args[0]
            return get_cert(domain)
    
    if operation == "get_all_domains":
        return get_all_domains()

    return "err" 

def put_cert(domain, cert):
    curr_domains = Get(GetContext, "all_domains")
    if curr_domains:
        Delete(GetContext, "all_domains")
        curr_domains = concat(curr_domains, ",")
        new_curr_domains = concat(curr_domains, domain)
        Put(GetContext, "all_domains", new_curr_domains)
    else:
        Put(GetContext, "all_domains", domain)
    Put(GetContext, domain, cert)
    return "ok" 

def get_cert(domain):
    cert = Get(GetContext, domain)
    if cert:
        return cert 
    return "err" 

def get_all_domains():
    return Get(GetContext, "all_domains")
