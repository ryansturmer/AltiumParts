import tableview
import os, sys

PRIMARY_KEY = 'uuid'

def row_to_sql(row):
    name = row[0].lower().replace('-','_').replace(' ','_')
    cols = row[1:]
    primary_key = PRIMARY_KEY
    retval = ['CREATE TABLE "%s" (' % name]
    retval.append('\tPRIMARY KEY(%s),' % primary_key)
    for col in cols:
        if(col != ""):
            col = col.lower().replace(' ', '_').replace('-','_')
            retval.append('\t"%s" text,' % col)
    retval[-1] = retval[-1].rstrip(',')
    retval.append(');')
    return '\n'.join(retval)

def main():
    infile = sys.argv[1]
    outfile = os.path.splitext(infile)[0] + '.sql'

    table = tableview.load(infile)

    with open(outfile, 'w') as fp:
        for row in table:
            fp.write(row_to_sql(row) + '\n')

    
if __name__ == "__main__":
    main()
