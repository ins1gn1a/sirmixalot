#!/usr/bin/env python3


import argparse

parser = argparse.ArgumentParser(description='SirTalkAlot: Wordlist generation tool')

parser.add_argument('-l',help="Wordlist: Positioned to left",dest='left_wl',required=True)
parser.add_argument('-m',help="Wordlist: Positioned in middle",dest='mid_wl')
parser.add_argument('-r',help="Wordlist: Positioned to right",dest='right_wl',required=True)
parser.add_argument('-s',help='Include spaces between words',action='store_true',default=False,dest='space')


args = parser.parse_args()

def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass

    return i + 1


mid_num_lines = file_len(args.mid_wl)
right_num_lines = file_len(args.right_wl)

# Left list larger
if (args.mid_wl):
    with open(args.left_wl,'r') as left_wl:
        if (int(mid_num_lines) > int(right_num_lines)):
            for left in left_wl:
                
                # Mid list longer
                with open(args.mid_wl,'r') as mid_wl:
                    for mid in mid_wl:
                        with open(args.right_wl, 'r') as right_wl:
                            for right in right_wl:
                                if args.space:
                                    print(left.rstrip() + " " + mid.rstrip() + " " + right.rstrip())
                                else:
                                    print (left.rstrip() + mid.rstrip() + right.rstrip())

        else:
            for left in left_wl:
                
                # Right list longer
                with open(args.right_wl, 'r') as right_wl:
                    for right in right_wl:
                        with open(args.mid_wl, 'r') as mid_wl:
                            for mid in mid_wl:
                                if args.space:
                                    print(left.rstrip() + " " + mid.rstrip() + " " + right.rstrip())
                                else:
                                    print(left.rstrip() + mid.rstrip() + right.rstrip())

else:
    left_wl = open(args.left_wl,'r')
    for left in left_wl:
        right_wl = open(args.right_wl, 'r')
        for right in right_wl:
            if args.space:
                print(left.rstrip() + " " + right.rstrip())
            else:
                print (left.rstrip() + right.rstrip())
        right_wl.close()

