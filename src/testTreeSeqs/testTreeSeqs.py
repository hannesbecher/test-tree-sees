import argparse
import msprime

parser = argparse.ArgumentParser(
                    prog='testTreeSeqs',
                    description='A package to generate test data for the HLab TS pipeline. Based on msprime.',
                    epilog='Thanks for using testTreeSeqs!')


parser.add_argument("-s", "--seed") # random seed


parser.parse_args()

def makeSim():
    ts = msprime.sim_ancestry(
        samples=10,
        recombination_rate=9.26e-09,
        sequence_length=50_000,
        population_size=1_000,
        random_seed=123456)

    ts = msprime.sim_mutations(
        ts,
        rate=1.2e-08,
        random_seed=54321
        )
    
    return ts
