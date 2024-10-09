#!/usr/bin/python

import argparse, random, sys

class Shuf:
    def __init__(self, args):
        self.args = args
        
        if args.input_range:
            self.lines = list(args.input_range)
        elif args.echo:
            self.lines = args.echo
        else:
            if args.file == "-":
                f = sys.stdin
            else:
                f = open(args.file, "r")

            self.lines = f.readlines()
            f.close()
            self.lines = [i.rstrip('\n') for i in self.lines] #strip '\n'
            
    def get_rand(self):
        if self.args.repeat:
            return random.choice(self.lines)
        else:
            r = random.randrange(len(self.lines))
            return self.lines.pop(r)


def str_range(string):
    index = string.index("-")
    LO = int(string[:index])
    HI = int(string[(index + 1):])
    
    return range(LO, HI + 1)

def line_count(n):
    n = int(n)
    if n < 0: 
        raise ValueError
    else:
        return n

def shuffle_out(args):
    # set up shuf object
    try:
        shuffler = Shuf(args)
    except FileNotFoundError: #to prevent long stack trace (otherwise error handling is done by arg parse)
        print(f"shuf.py: {args.file}: No such file or directory")
        return 1

    # print random lines to stdout
    count = 0
    while len(shuffler.lines) and count < args.head_count:
        print(shuffler.get_rand())
        count += 1

    return 0


def main():
    #set up argument parsing
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    
    ## positional args
    group.add_argument("file", nargs="?", default="-", help="file to read from")

    ## optional args
    group.add_argument("-e", "--echo",
                       help="treat each ARG as an input line",
                       nargs="*")
    group.add_argument("-i", "--input-range",
                       metavar="LO-HI",
                       help="treat each number LO through HI as an input line",
                       type=str_range) 
    parser.add_argument("-n", "--head-count",
                        help="output at most COUNT lines",
                        type=line_count,
                        default=float('inf'))
    parser.add_argument("-r", "--repeat",
                        help="output lines can be repeated",
                        action="store_true")

    args = parser.parse_args()

    return shuffle_out(args)

if __name__ == "__main__":
    main()
