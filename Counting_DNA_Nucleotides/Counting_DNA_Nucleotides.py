seq=("AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC")

def countnucleotide(sequence):
    out="{} {} {} {}".format(seq.count('A'), seq.count('C'), seq.count('G'), seq.count('T'))
    return(out)
countnucleotide(seq)