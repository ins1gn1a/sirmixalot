#!/usr/bin/env python3

import argparse

parser = argparse.ArgumentParser(description='SirTalkAlot: Wordlist generation tool')

parser.add_argument('-l',help="Wordlist: Positioned to left",dest='left_wl',required=True)
parser.add_argument('-m',help="Wordlist: Positioned in middle",dest='mid_wl')
parser.add_argument('-r',help="Wordlist: Positioned to right",dest='right_wl',required=True)
parser.add_argument('-s',help='Include spaces between words',action='store_true',default=False,dest='space')

args = parser.parse_args()

if (args.mid_wl):
    left_wl = open(args.left_wl,'r')
    for left in left_wl:
        mid_wl = open(args.mid_wl,'r')
        for mid in mid_wl:
            right_wl = open(args.right_wl, 'r')
            for right in right_wl:
                if args.space:
                    print(left.rstrip() + " " + mid.rstrip() +" " + right.rstrip())
                else:
                    print (left.rstrip() + mid.rstrip() + right.rstrip())
            right_wl.close()
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

