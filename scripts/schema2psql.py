import tableview
import os, sys

PRIMARY_KEY = 'uuid'
infile = sys.argv[1]
outfile = os.path.splitext(infile)[0] + '.sql'

table = tableview.load(infile)


def row_to_sql(row):
    name = row[0].lower()
    cols = row[1:]
    primary_key = PRIMARY_KEY
    retval = ['CREATE TABLE %s {' % name]
    retval.append('\tPRIMARY KEY(%s)' % primary_key)
    for col in cols:
        if(col != ""):
            col = col.lower().replace(' ', '_')
            retval.append('\t"%s" text,' % col)
    retval[-1].rstrip(',')
    retval.append('};')
    return '\n'.join(retval)


for row in table:
    print row_to_sql(row)
