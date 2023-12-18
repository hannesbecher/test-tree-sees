# test-tree-sees
Generate tree sees for testing and demonstration

# Dependencies
A recent version of msprime.  
On Eddie, you can use the HLab conda env `treeStuff`.

# Run from command line
```
# clone repo
git clone <this repo>

# navigate to src folder
cd test-tree-seqs/src

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
####   -p PROB, --prob PROB  probability of wrongly infrerred ancestral allele, defaults to 0.01
####   -l CHROMOSOME_LENGTH, --chromosome_length CHROMOSOME_LENGTH
####                         chromosome length
#### 
#### Thanks for using testTreeSeqs!

# run as module
python -m testTreeSeqs
```

# Output
Theer output files:
* `<prefix>.ts` The simulated tree sequence
* `<prefix>.vcf` Corresponding VCF file
* `<prefix>.ts` A VCF file with proportion `p` of sites with swapped allel state (to simulate wrong ancestral inference)