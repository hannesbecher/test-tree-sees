
import msprime

def makeSim(clen):
    ts = msprime.sim_ancestry(
        samples=nInd,
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

def swapDipCall(gt):
    if gt == "0|1": return "1|0"
    elif gt == "1|1": return "1|1"
    elif gt == "1|0": return "0|1"
    elif gt == "0|0": return "1|1"

def swapCalls(ln, p):
    fields=ln[:-1].split("\t")
    gts = [swapDipCall(i) for i in fields[9:]]
    return "\t".join(fields[:9] + gts) + "\n"
    
def swapVCF(prefix, p):
    with open(prefix + ".vcf", "r") as f:
        with open(prefix + "_swapped.vcf", "w") as o:
            for line in f:
                if random.random() > p or line.startswith("#"):
                    o.write(line)
                else:
                    o.write(swapCalls(line, p))
                    
