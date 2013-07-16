#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''Command Line Tool for reading data from nhl.com'''

import sys
import csv
import argparse

import nhl


def main():

    parser = argparse.ArgumentParser(description='Read stats from nhl.com')
    
    parser.add_argument('-p', '--playoff', dest='playoff', action='store_true', default=False, help='Playoff stats')
    parser.add_argument('--header', dest='header', action='store_true', help='Writes header row', default=False)
    parser.add_argument('-s', '--season', metavar='season', required=True, dest='season', action='store', help='Season, e.g. 20122013')
    parser.add_argument('-o', dest='outfile',action='store', help='Output file')
    parser.add_argument('--report', choices=['bios', 'summary'], default='bios', dest='view', action='store', help='Report type')

    args = parser.parse_args()


    if args.playoff:
        gametype = 'playoff'
    else:
        gametype = 'regular'


    reader = nhl.reader(args.season, gametype, args.view)

    if args.outfile:
        fp = open(args.outfile, "w")
    else:
        fp = sys.stdout        
    writer = csv.writer(fp)

        
    if args.header:
        writer.writerow(reader.fieldnames)
    
    writer.writerows(reader)


if __name__ == '__main__':
    main()
