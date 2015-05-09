#!/usr/bin/env python
# encoding: utf-8

import sys
import os
import re
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

if __name__ == '__main__':
    summary = os.popen("gcovr -r %s --gcov-exclude 'gtest/*' -e 'lib/gtest/*' -e '%s/tests/' -s"%(sys.argv[1], sys.argv[1])).read()
    print bcolors.HEADER
    print "REPORT\n"
    print bcolors.OKBLUE
    print summary
    print bcolors.ENDC
    string  = summary.split('\n')[-3]
    string2 = summary.split('\n')[-2]
    pattern = re.compile(r"(\d+\.\d)%")
    # pattern = re.compile(r"(\d+\.\d)")
    lines_cov  = float(pattern.search(string).group(1))
    branch_cov = float(pattern.search(string).group(1))
    if lines_cov < 95 or branch_cov < 95:
        print bcolors.FAIL + "Failure" + bcolors.ENDC
        exit(1)
    else:
        print bcolors.OKGREEN + "Success" + bcolors.ENDC
