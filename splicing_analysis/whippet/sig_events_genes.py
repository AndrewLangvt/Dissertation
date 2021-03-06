# sig_events_genes.py
# Andrew S. Lang
# Created: 23MAR2018
# Last Modified: 02APR2018

# This script will take an input diff.gz file from whippet, and write all of the genes in which significant 
# splicing events (prob > 0.95 and abs(PSI)>=0.1) occur

import re
import sys
import gzip

def sig_ev(fname):
    name_trimmed = re.sub(r'.*/', '', str(fname)).replace("_comparison.diff.gz","")
    outfile_name = "spliced_genes-" + name_trimmed + ".tsv"
    outfile = open(outfile_name, "w")
    with gzip.open(fname, 'rt') as file2 :
        file = file2.readlines()[1:]
        spliced_genes = ""
        spliced_genes_list = []

        for line in file:
            column = line.rstrip().split("\t")

            geneID = str(column[0])
            prob = float(column[8])
            psi = abs(float(column[7]))
            event = str(column[2])

            if prob >= float(0.95) :
                if psi >= float(0.1) :
                    spliced_genes+= geneID + "\t" + str(psi) + "\t" + event + "\n"
                else:
                    continue
            else:
                continue

        outfile.write("Analysis:Whippet " + name_trimmed + "\t" + "Event_Loci" + "\n" + spliced_genes)
        outfile.close()

if __name__ == '__main__':
    filename = sys.argv[1]
    sig_ev(filename)
