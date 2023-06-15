import argparse
import glob
import os
import re
import csv

parser = argparse.ArgumentParser()
parser.add_argument("--searchpath", type=str, help="Filepath to be searched. Default: ./")
parser.add_argument("--extlist", nargs="*", type=str, help="File extensions to be scanned. Default: .py .html .js")
args = parser.parse_args()

if args.searchpath is None:
    searchpath = "./**/*.*"
else:
    searchpath = os.path.join(args.searchpath, "**/*.*")

if args.extlist is None:
    extlist = [".py", ".html", ".js"]
else:
    extlist = args.extlist

filelist = glob.glob(searchpath, recursive=True)
filelist_ext = [filename for filename in filelist if os.path.splitext(filename)[1] in extlist]

resultlist_w_filename = []

for filename in filelist_ext:
    resultlist = []

    with open(filename) as f:
        for line in f:
            results = re.findall('"([^"]*)"', line)
            if len(results) > 0:
                for res in results:
                    if len(res) != len(res.encode('utf-8')):
                        resultlist.append(res)

    resultlist = list(set(resultlist))

    if len(resultlist) > 0:
        resultlist_w_filename.extend([[filename, res] for res in resultlist])

with open('japanese.csv', 'w', newline='', encoding='cp932') as outfile:
    writer = csv.writer(outfile)
    writer.writerow(['file', 'jpn'])
    for row in resultlist_w_filename:
        writer.writerow(row)
