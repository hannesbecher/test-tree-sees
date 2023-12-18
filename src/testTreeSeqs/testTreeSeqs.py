import argparse
import msprime
import random

parser = argparse.ArgumentParser(
                    prog='testTreeSeqs',
                    description='A package to generate test data for the HLab TS pipeline. Based on msprime.',
                    epilog='Thanks for using testTreeSeqs!')

parser.add_argument("-s", "--seed", type=int, help="master random seed") # random seed
parser.add_argument("-o", "--out", type=str, help="output prefix")
parser.add_argument("-p", "--prob", type=str, help="swap prob")
parser.add_argument("-l", "--chromosome_length", type=str, help="chromosome length")

args = parser.parse_args()



if args.prob:
    p=args.prob
else:
    p=0.01

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

print(seeds)

def makeSim(clen):
    ts = msprime.sim_ancestry(
        samples=10,
        recombination_rate=9.26e-09,
        sequence_length=clen,
        population_size=1_000,
        random_seed=seeds[0]
        )

    ts = msprime.sim_mutations(
        ts,
        rate=1.2e-08,
        random_seed=seeds[1]
        )
    
    return ts


# Running the simulation ######################
print("Simulating tree seq...")
ts = makeSim(ll)


# Write results ###########################
print("Writing TS...")
with open(pref + ".ts", "w") as f:
    ts.dump(f)

print("Writing VCF...")
with open(pref + ".vcf", "w") as f:
    ts.write_vcf(f)

# Swapping alleles###########################
print("Swapping (some) alleles...")
import swapAlleles

# p is the probability of swap
swapAlleles.swapVCF(pref, p)

print("All done.")

