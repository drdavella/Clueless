import sys


def main(ver, port):
    if ver == "server":
        print "You are running the server on port " + port
    elif ver == "client":
        print "You are running the client on port " + port
    else:
        print "I have no idea what you want to run"


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
