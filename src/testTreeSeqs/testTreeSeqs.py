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

print(seeds)

def makeSim():
    ts = msprime.sim_ancestry(
        samples=10,
        recombination_rate=9.26e-09,
        sequence_length=50_000,
        population_size=1_000,
        random_seed=seeds[0]
        )

    ts = msprime.sim_mutations(
        ts,
        rate=1.2e-08,
        random_seed=seeds[1]
        )
    
    return ts


ts = makeSim()

# Write results ###########################
with open(pref + ".vcf", "w") as f:
    ts.write_vcf(f)

print("Going to swap alleles...")
import swapAlleles

swapAlleles.swapVCF(out, p)

print("All done.")

