# Exercise 1.2 from Think Stats vs2 by Allen B. Downey
# Data used is provided by various sources
# Example code provided by A. B. Downey (all available on github)

# This code written by S. Chappell as part of exercise and from
# examples provided in Think Stats (Allen B. Downey).
# Meant for self-educating purposes only.

import thinkstats2
import pandas as pd

def readResp(dct_file='2002FemResp.dct',dat_file='2002FemResp.dat.gz'):
    resp_dict = thinkstats2.ReadStataDct(dct_file)
    resp_df = resp_dict.ReadFixedWidth(dat_file, compression='gzip')
    return resp_df

def compCB(resp):
    print resp.pregnum.value_counts().sort_index()
    # to compare to codebook, sum for 7 or more
    print resp[resp.pregnum >= 7].pregnum.count()

# codebook: https://www.icpsr.umich.edu/nsfg6/Controller?displayPage=labelDetails&fileCode=FEM&section=R&subSec=7869&srtLabel=606835
