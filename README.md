# find2things #
Find two things

## Overview ##

A quick hack to find two lines of interest in a stream but only if the first is followed by the second.

## Usage ##
    >cat src/find2things.py | python src/find2things.py '^def.*' '.*main.*'
    def main(argv):
    if __name__ == "__main__":

The command takes two parameters and an input stream on standard in

* Regular expresion for the first matching line
* Regular expression for the second matching line

Result will be output to standard output