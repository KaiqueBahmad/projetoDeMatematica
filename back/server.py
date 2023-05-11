import socket
from utils.render import render

#Setup do servidor HTTP
HOST, PORT = 'localhost', 8080
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(1)
print(f'Server rodando em http://{HOST}:{PORT}')


def parseRequestPath():
    global request
    try:
        #Extraindo caminho acessado do cabeçalho da requisição.
        path = request.split('\n')[0].split(' ')
    except Exception:
        #caso haja erros na extração do caminho, a requisição será tratada como se seu caminho fosse para '/'
        path = ['GET', '/']
        print("Incapaz de parse: ", request.split('\n')[0])
    return path

def readRequestCookies(request):
    header = request.split('\r\n\r\n')[0].split('\n')
    print(header)

def readCookies():
    readRequestCookies()

def assignCookie():
    global header, response
    cookie = str(input("valor do cookie: "))
    SETCOOKIE_COMMAND = b'Set-Cookie: password={COOKIE_VALUE}{HEADER_END}\r\n'.replace(b'{COOKIE_VALUE}',cookie.encode())
    header = header.replace(b'{HEADER_END}', SETCOOKIE_COMMAND)
    template = open('./views/cookieSet.html', 'r')
    response = template.read().replace('{COOKIE_VALUE}', cookie)
    template.close()

def showNotFound(*args):
    return ''



#Dicionário que define quais funções serão chamadas para atender cada requisição, diferenciando também pelo tipo 
#da requisição, GET ou POST
handles = {
    "GET": {
        "/": ['readCookies'],
        "/setcookies": ['assignCookie'],
        "/notfound": ['showNotFound']
    },
    "POST": {
        "/": ['readCookies']
    }
}

while True:
    client_socket, client_address = server_socket.accept()
    request = client_socket.recv(1024).decode()
    requestPath = parseRequestPath(request)
    header = b'HTTP/1.1 200 OK\r\n{HEADER_END}\r\n'

    # Colocando o arquivo HTML na resposta
    
    response = ''
    if requestPath not in handles:
        requestPath = '/notFound'

    for step in handles[requestPath.lower()]:
        eval(f'{step}()')
    
    # indexHTML = open('./views/index.html', 'rb')
    # response = indexHTML.read()
    # indexHTML.close()

    print(header.replace(b'{HEADER_END}', b'')+response.encode())
    client_socket.sendall(header.replace(b'{HEADER_END}', b'')+response.encode())
    client_socket.close()
