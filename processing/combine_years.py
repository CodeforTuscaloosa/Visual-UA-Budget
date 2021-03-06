#!/usr/bin/python3

#
# After downloading data in CSV format one fiscal year at a time from open.ua.edu,
# this script can be used to combine the years into one file and add a FY column.
# The input and output files should be located in _data in the parent directory.
# (If you try to download all the data at once, their server crashes.)
#

__author__='mleeds95'

import csv

files = ['UA_FY_2010.csv', 'UA_FY_2011.csv', 'UA_FY_2012.csv', 'UA_FY_2013.csv', 'UA_FY_2014.csv', 'UA_FY_2015.csv']

totalRows = 0
outFilename = 'ua_expenses.csv'
with open('../_data/' + outFilename, 'w') as outFile:
    writer = csv.writer(outFile)
    for (i, fname) in enumerate(files):
        with open('../_data/' + fname) as inFile:
            reader = csv.reader(inFile)
            for (j, row) in enumerate(reader):
                if j > 0 or i == 0:
                    writer.writerow(row)
            print('Read ' + str(j) + ' rows from ' + fname)
            totalRows += j

print('Wrote ' + str(totalRows) + ' rows to ' + outFilename)

