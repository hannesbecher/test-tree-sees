import argparse
import random
from . import testTreeSeqs
# parsing args ##################################
parser = argparse.ArgumentParser(
                    prog='testTreeSeqs',
                    description='A package to generate test data for the HLab TS pipeline. Based on msprime.',
                    epilog='Thanks for using testTreeSeqs!')

parser.add_argument("-s", "--seed", type=int, help="master random seed") # random seed
parser.add_argument("-o", "--out", type=str, help="output prefix")
parser.add_argument("-p", "--prob", type=float, help="probability of wrongly inferred ancestral allele, defaults to 0.01", default=0.01)
parser.add_argument("-l", "--chromosome_length", type=str, help="chromosome length")

args = parser.parse_args()



#if args.prob:
#    p=args.prob
#else:
#    p=0.01

p=args.prob

if args.seed:
    random.seed(args.seed)
    
seeds = [random.randint(0, 1000000) for i in range(10)]


if args.out:
    pref=args.out
else:
    pref="ts"

if args.chromosome_length:
    ll=args.chromosome_length
else:
    ll=50_000

nInd=50 # diploids

print(seeds)



# Running the simulation ######################
print("Simulating tree seq...")
ts = testTreeSeqs.makeSim(ll, nInd, seeds)


# Write results ###########################
print("Writing TS...")
with open(pref + ".ts", "w") as f:
    ts.dump(f)

print("Writing VCF...")
with open(pref + ".vcf", "w") as f:
    ts.write_vcf(f, contig_id='chr1')

# Swapping alleles###########################
print("Swapping (some) alleles...")

# p is the probability of swap
testTreeSeqs.swapVCF(pref, p)

# make metadata file #######################
with open("SampleMetaData.csv", "w") as f:
    f.write("ID,Pop,SubPop,Time\n")
    for i in range(nInd):
        f.write("tsk_%d,P1,P11,0\n" % i)


print("All done.")

