#!/usr/bin/env python

import cmd
import os, subprocess, sys
import httplib, urllib, urllib2
import json
import re

'''
'''

################################################################################

class Find2Things():
    looking = False
    
    def __init__(self, first, second, one_line):
        pass
        self.first = first
        self.second = second
        self.one_line = one_line
    def work(self):
        line_first = ""
        line_second = ""
        
        reg_one = re.compile(self.first)
        reg_two = re.compile(self.second)
        
        self.looking = False
        for line in sys.stdin:
            if reg_one.match(line)!=None:
                self.looking = True
                line_first = line
                continue
            elif self.looking:
                if reg_two.match(line)!=None:
                    self.looking = False
                    if self.one_line:
                        fmt = "%s %s"
                    else:
                        fmt = "%s\n%s"
                    print fmt % (line_first.strip(), line.strip())

def main(argv):
    one_line = True
    if 2<len(argv) and (argv[2]=="-l" or argv[2]=="--line"):
        one_line = True
    else:
        one_line = False
    
    f = Find2Things(argv[0], argv[1], one_line)
    f.work()

if __name__ == "__main__":
    main(sys.argv[1:])