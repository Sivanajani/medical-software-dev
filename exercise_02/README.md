# Exercise 02 – GC Content Calculator

A command-line tool that computes the GC-content of a DNA sequence from a FASTA file. The GC-content is the percentage of bases in the sequence that are either `G` or `C`.

## Background

This exercise is based on the gene CD28, which is involved in T-cell activation. The drug Theralizumab targeted CD28 and caused a severe adverse reaction in a first-in-human study — an example of why genomic analysis tools matter in medical software development.

## Usage

```bash
python3 gccompute.py INPUT_FILE
```

## Output

Since the FASTA file can contain multiple sequences, the script processes all of them. For each sequence it prints exactly 2 lines to stdout:

```
<sequence header>
<GC-content as float>
```

Example with `cd28.fasta` (contains 2 sequences — primary assembly and alternate locus):

```bash
python3 gccompute.py cd28.fasta
```

```
NC_000002.12:203706482-203738912
40.004933551231844
NC_060926.1:204188401-204220837
39.9975336806733
```

After the run, results are also saved to `results.json` and `results.txt` in the `exercise_02/` folder, including a timestamp so you know when and by which script they were generated.

## Error handling

- No filename provided: prints usage message to stderr, exits with code 1.
- File not found: prints error to stderr, exits with code 1.
- File not readable or invalid encoding: prints error to stderr, exits with code 1.
- No valid FASTA sequences in file: prints error to stderr, exits with code 1.

## Where to find things

| What | Where |
|---|---|
| Script | `gccompute.py` |
| Input data (CD28) | `cd28.fasta` (extracted from the NCBI dataset zip and renamed from `gene.fna`) |
| Result output (JSON) | `results.json` |
| Result output (text) | `results.txt` |
| Discussion & answers | `exercise_02.md` |

## Data source

The CD28 FASTA sequence was downloaded from NCBI Datasets:

```
https://www.ncbi.nlm.nih.gov/datasets
```

The full dataset is in the `ncbi_dataset/` folder.