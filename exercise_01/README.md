# Exercise 01 – Gene Analyzer

A command-line tool that analyzes the NCBI `gene_info` dataset and extracts key statistics: total gene count, Homo sapiens gene count, all gene types, and the most frequent gene type. Results are printed to stdout and also saved as `results.json` and `results.txt`.

## Setup

Download the gene_info file from NCBI:

```
https://ftp.ncbi.nlm.nih.gov/gene/DATA/gene_info.gz
```

Extract it into this folder:

```bash
gunzip gene_info.gz
```

This produces a file called `gene_info` (~9 GB).

## Usage

```bash
python3 gene_analyzer.py gene_info
```

The script also works directly on the compressed file without extracting:

```bash
python3 gene_analyzer.py gene_info.gz
```

## Output

Since the `gene_info` file is very large (~9 GB, 68+ million genes), the script includes a progress indicator. Every 1 million processed genes a status line is printed to stderr so you can follow along:

```
  Processed 1,000,000 genes...
  Processed 2,000,000 genes...
  ...
```

If any malformed lines are detected (too few columns), a warning is printed to stderr at the end:

```
Warning: X malformed line(s) skipped.
```

Once processing is complete, the 5 result lines are printed to stdout:

```
<MD5 hash of the input file>
<total gene count>
<homo sapiens gene count>
<TYPE_1, TYPE_2, ..., TYPE_N>
<most frequent type>
```

**Actual results from running on the current `gene_info` file:**

```
309f8103b2b7efb7f899fc06a56d8b90
68523888
193793
biological-region, miscRNA, ncRNA, other, protein-coding, pseudo, rRNA, scRNA, snRNA, snoRNA, tRNA, unknown
protein-coding
```

**Files written to the same folder as the input:**

| File | Content |
|---|---|
| `results.json` | Full results including per-type counts, as structured JSON |
| `results.txt` | Same 5-line output as stdout |

## Discussion

Answers to the exercise questions — including data results and software engineering questions — are in [`answers.md`](answers.md).
