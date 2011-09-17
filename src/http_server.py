import socket

content = 'HTTP/1.0 200 OK\r\nContent-Type: text/plain\r\nContent-Length: 12\r\n\r\nHello world!'

ADDR = '127.0.0.1'
PORT = 8000

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    print 'Starting HTTP server port=%s' % PORT
    s.bind((ADDR, PORT))
    s.listen(1)
    try:
        while True:
            conn, addr = s.accept()
            print '---connected---'
            try:
                data = conn.recv(1024)
                print data
                print '-------------------------'
                conn.send(content)
            finally:
                conn.close()
    except KeyboardInterrupt:
        pass

if __name__ == '__main__':
    main()
