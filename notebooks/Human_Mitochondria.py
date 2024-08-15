"""
This script extracts the human mitochondrial DNA sequence from a large genomic FASTA file using Biopython. 
The script locates the sequence identified by the accession number "NC_012920.1," which corresponds to the 
complete human mitochondrial genome. The extracted sequence is then saved to a new FASTA file for easier 
analysis in subsequent steps.
"""



from Bio import SeqIO


fasta_file  = r"C:\Users\...\GCF_000001405.40_GRCh38.p14_genomic.fna\GCF_000001405.40_GRCh38.p14_genomic.fna"


output_file = "human_mitochondrial.fasta"


# Parsing the FASTA file
sequences = SeqIO.parse(fasta_file, "fasta")

# Find and extract the mitochondrial sequence
for record in sequences:
    if record.id == "NC_012920.1":
        mito_seq = record.seq
        # Save the mitochondrial DNA sequence to a new FASTA file

        mito_record = SeqIO.SeqRecord(mito_seq, id="NC_012920.1", description="Homo sapiens mitochondrion, complete genome")
        SeqIO.write(mito_record, output_file, "fasta")
        print(f"Mitochondrial DNA sequence saved to '{output_file}'")
        break
