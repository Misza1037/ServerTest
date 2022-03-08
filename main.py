import server


HOST = 'servertest-production.up.railway.app'
PORT = 65065


if __name__ == '__main__':
    server.connection(HOST, PORT)
