# !/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re

def extract_names(filename):
    fh = open(filename, 'r')
    html = fh.read()
    namelist = []
    searchyear = re.search("Popularity in (.*)<",html)
    namelist.append(searchyear.group(1))
    namesdict = {}
    searchname = re.findall("<td>(.*)</td><td>(.*)</td><td>(.*)</td>",html)
    for person in searchname:
        (num, male, female) = person
        namesdict[male]=num
        namesdict[female]=num
    sortednames=sorted(namesdict.keys())
    for name in sortednames:
        namelist.append(name + " " + namesdict[name])
    return namelist

def main():
    args = sys.argv[1:]
    args.append("--summaryfile")
    args.append("c://Users/vend/Desktop/baby1990.html")
    args.append("c://Users/vend/Desktop/baby1992.html")

    if not args:
        print('usage: [--summaryfile] file [file ...]')
        sys.exit(1)

    summary = False
    if args[0] == '--summaryfile':
        summary = True
        del args[0]

    for filename in args:
        names = extract_names(filename)
        if summary:
            output = "\n".join(names)
            writer = open(filename.replace(".html",".summary"), 'w')
            writer.write(output + '\n')
            writer.close()

if __name__ == '__main__':
    main()
