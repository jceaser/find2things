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
    '''Enum of menu options'''
    looking = False
    
    def __init__(self, first, second):
        pass
        self.first = first
        self.second = second
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
                    print "%s\n%s" % (line_first.strip(), line.strip())
        
def main(argv):
    f = Find2Things(argv[0], argv[1])
    f.work()
    
if __name__ == "__main__":
   main(sys.argv[1:])