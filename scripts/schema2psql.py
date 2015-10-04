import tableview
import os, sys

infile = sys.argv[1]
outfile = os.path.splitext(infile)[0] + '.sql'

table = tableview.load(infile)
for row in table:
    table_name = row[0]
    columns = row[1:]
    print table_name
