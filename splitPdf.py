from ast import arg
from distutils.debug import DEBUG
from PyPDF2 import PdfFileWriter, PdfFileReader
import sys
import datetime
import re

DEBUG = False

# https://www.codeforests.com/2020/08/08/how-to-split-or-merge-pdf-files/

def main(*args):
    if DEBUG:
        print(args)
    try:
        inFil, start, end = args[0], int(args[1]), int(args[2])
    except:
        print("Invalid arguments!")
    try:
        outName = args[3]
    except:
        outName = f"Splitted__{datetime.datetime.now().strftime('%Y-%m-%d_%H.%M.%S')}.pdf"
    input_pdf = PdfFileReader(inFil)
    if start <= 0 or end <= 0:
        print("Enter positive start and end page numbers!")
        return
    if input_pdf.getNumPages() < end:
        print("End page cannot be greater than overall page number!")
        return
    output = PdfFileWriter()
    for i in range(start-1, end):
        output.addPage(input_pdf.getPage(i))
    with open(outName, "wb") as fil:
        output.write(fil)
    print(f"New PDF created successfully: {outName}")

if __name__ == "__main__":
    args = sys.argv
    if DEBUG:
        print(args)
    args.remove(__file__)
    if DEBUG:
        print(args)
    if len(args) < 3:
        raise SyntaxError("Too few arguments.")
    elif len(args) > 4:
        raise SyntaxError("Too many arguments.")
    else:
        main(*args)