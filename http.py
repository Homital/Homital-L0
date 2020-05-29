def http_get(host, path, port):
    import socket
    #_, _, host, path = url.split('/', 3)
    addr = socket.getaddrinfo(host, port)[0][-1]
    s = socket.socket()
    s.connect(addr)
    s.send(bytes('GET /%s HTTP/1.0\r\nHost: %s\r\n\r\n' % (path, host), 'utf8'))
    res = ""
    while True:
        data = s.recv(520)
        if data:
            res = str(data, 'utf8')
        else:
            break
    s.close()
    return res

def percent_decode(code):
    return code.replace("%21", "!").replace("%23", "#").replace("%24", "$").replace("%25", "%").replace("%26", "&").replace("%27", "'").replace("%28", "(").replace("%29", ")").replace("%2A", "*").replace("%2B", "+").replace("%2C", ",").replace("%2F", "/").replace("%3A", ":").replace("%3B", ";").replace("%3D", "=").replace("%3F", "?").replace("%40", "@").replace("%5B", "[").replace("%5D", "]")