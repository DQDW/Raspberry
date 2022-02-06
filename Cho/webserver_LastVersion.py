import socket

def ReadFile(filename):
    file = open("main.html", 'r')
    content =''
    while True:
        line = file.readline()
        if line =='':
            break
        content += line
    file.close()
    return content

HOST, PORT = '', 5001

listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listen_socket.bind((HOST, PORT))
listen_socket.listen(1)
print ('Serving HTTP on port', PORT, '...')
while True:
    client_connection, client_address = listen_socket.accept()
    request = str(client_connection.recv(1024),'euc-kr')
    print (request)

    http_response = """\
HTTP/1.1 200 OK

"""
    
    html_file = ReadFile("main.html")
    http_response += html_file
    client_connection.sendall(bytes(http_response,'euc-kr'))
    client_connection.close()

