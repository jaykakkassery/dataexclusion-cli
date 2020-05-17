import sys
import mysql.connector
import argparse
import subprocess
import os

def main():
    import csv
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('-m', '--mainfile', help='Provide main file')
    parser.add_argument('-f', '--filterfile', help='Provide filter file', default='employee')
    args = parser.parse_args()

    f1 = open(args.mainfile, 'r')
    f2 = open(args.filterfile, 'r')
    f3 = open('results.csv', 'w')


    c1 = csv.reader(f1)
    c2 = csv.reader(f2)
    c3 = csv.writer(f3,  quoting=csv.QUOTE_ALL)

    masterlist = list(c2)

    for fist_row in c1:  # secondfile
        row = 1
        found = False
        for second_row in masterlist:  # firstfile
            results_row = fist_row
            if (fist_row[0] == second_row[0]):
                found = True
                break
        if (found == False):
            c3.writerow(results_row)

    f1.close()
    f2.close()
    f3.close()

if __name__ == '__main__':
    main()