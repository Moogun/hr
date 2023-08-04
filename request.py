from pyxing.session import *
from pyxing.query import *

def login():
    f = open("account.txt", "rt")
    lines = f.readlines()
    id = lines[0].strip()
    pwd = lines[1].strip()
    cert = lines[2].strip()
    f.close()

    # Login
    xasession = XASession()
    xasession.login(id=id, password=pwd, cert=cert, block=True)
    print("서버: ", xasession.get_server_name(), " connected - ", xasession.is_connected(), " accountList(0) - ",
          xasession.get_account_list(0))


def tr_val(mk, when):
    xaquery = XAQuery()
    df = xaquery.block_request("t1463",gubun=mk,jnilgubun=when)
    print(df[1])


