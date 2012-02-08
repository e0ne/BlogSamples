import SOAPpy

def hello():
    return 'hello from soap server'

if __name__ == "__main__":
    try:
        SOAPpy.Config.debug = 1
        server = SOAPpy.SOAPServer(("localhost", 8080))
        server.registerFunction(hello)
        server.serve_forever()
    except KeyboardInterrupt:
        exit(0)

