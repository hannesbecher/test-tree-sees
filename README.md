# test-tree-seqs
Generate tree sequences for testing and demonstration

# Dependencies
A recent version of msprime.  
On Eddie, you can use the HLab conda env `treeStuff`.

# Run from command line
```
# clone repo
git clone <this repo>

# navigate to src folder
cd test-tree-seqs/src

# make sure the msprim package is available, e.g. run source activate treeStuff

# Check USAGE
$ python -m testTreeSeqs -h
#### usage: testTreeSeqs [-h] [-s SEED] [-o OUT] [-p PROB] [-l CHROMOSOME_LENGTH]
#### 
#### A package to generate test data for the HLab TS pipeline. Based on msprime.
#### 
#### options:
####   -h, --help            show this help message and exit
####   -s SEED, --seed SEED  master random seed
####   -o OUT, --out OUT     output prefix
####   -p PROB, --prob PROB  probability of wrongly inferred ancestral allele, defaults to 0.01
####   -l CHROMOSOME_LENGTH, --chromosome_length CHROMOSOME_LENGTH
####                         chromosome length
#### 
#### Thanks for using testTreeSeqs!

# run as module
python -m testTreeSeqs -l 10000000 -p 0.01 # chromosome of 10M bp with 1% wrongly inferred ancestral alleles
```

# Output
Three output files:
* `<prefix>.ts` The simulated tree sequence
* `<prefix>.vcf` Corresponding VCF file
* `<prefix>_swapped.vcf`  A VCF file with proportion `p` of sites with swapped allelic state (to simulate wrong ancestral inference)  

Both VCF files can be used as input to the TS pipeline.

# Simulation params
... recombination and mutation rates are hard coded ATM in `testTreeSeqs.py` to match cattle.