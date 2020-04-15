import argparse
from socket import socket, AF_INET, SOCK_STREAM


def scan(start, finish):
    for port in range(start, finish + 1):
        s = socket(AF_INET, SOCK_STREAM)
        s.settimeout(0.01)
        try:
            s.connect(('localhost', port))
        except:
            continue
        else:
            print("Port %d open." % port)
        s.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="This is TCP ports scanner",
        usage="scanner.py [-h] [--help] [--start] [--finish]")
    parser.add_argument(
        "--start", type=int, required=True,
        help="start of range")
    parser.add_argument(
        "--finish", type=int, required=True,
        help="end of range")
    args = parser.parse_args()
    scan(args.start, args.finish)
