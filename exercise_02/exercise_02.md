# Exercise 02 – Discussion

**Sources:** [`gccompute.py`](gccompute.py) · [`cd28.fasta`](cd28.fasta) · [`results.json`](results.json) · [`results.txt`](results.txt)

## Results

| Sequence | GC-Content |
|---|---|
| NC_000002.12:203706482-203738912 (CD28) | 40.004933551231844 |
| NC_060926.1:204188401-204220837 (CD28) | 39.9975336806733 |

---

## Discussion Questions

### What is the GC-content value of the Human Gene CD28?
40.004933551231844 for the primary sequence `NC_000002.12:203706482-203738912`.

### What is a FASTA file?
A FASTA file is a text-based format for representing nucleotide or amino acid sequences. Each entry starts with a header line beginning with `>` followed by a sequence identifier and optional description. The subsequent lines contain the sequence data (one or more lines of letters). Example:
```
>NC_000002.12:203706482-203738912 CD28 [organism=Homo sapiens] [GeneID=940] [chromosome=2]
ATCAAAACAACGTTATATCCTGTGTGAAATGCTGCAGTCA...
```

### What happens if there are multiple sequences in the FASTA file?
The program iterates over all sequences in the file and prints the header and GC-content for each one. The `cd28.fasta` file contains two sequences (primary assembly and alternate locus), and both are processed and displayed.

### What happens if the FASTA file is invalid?
- If no filename is provided: a usage message is printed to stderr and the program exits with code 1.
- If the file does not exist: an error message is printed to stderr and the program exits with code 1.
- If the file is not readable (OS error): same error handling applies.
- If the file has invalid encoding (UnicodeDecodeError): an error message is printed to stderr and the program exits with code 1.
- If the file contains no valid FASTA sequences (no `>` header found): an error message is printed and the program exits with code 1.

### What happens if there are upper case and lower case letters in the sequence?
The `compute_gc_content` function converts the entire sequence to uppercase before counting G and C bases. This ensures correct results regardless of letter case (e.g., `g`, `c`, `G`, `C` are all counted).

### Where can you download a sequence for a human gene?
Sequences can be downloaded from **NCBI Datasets** (https://www.ncbi.nlm.nih.gov/datasets). Steps:
1. Open the link and click on the **"Gene"** tab in the navigation bar.
2. Search for the gene name (e.g. "CD28") and select *Homo sapiens*.
3. Download the FASTA sequence.