# Exercise 01 – Gene Analyzer

A command-line tool that analyzes the NCBI `gene_info` dataset and extracts key statistics: total gene count, Homo sapiens gene count, all gene types, and the most frequent gene type.

## Setup

Download the gene_info file from NCBI:

```
https://ftp.ncbi.nlm.nih.gov/gene/DATA/gene_info.gz
```

## Usage

```bash
python3 gene_analyzer.py gene_info.gz
```

The script detects the `.gz` extension and decompresses the file on the fly using Python's built-in `gzip` module. No manual extraction needed.

## Output

Since the `gene_info` file is very large (~9 GB, 68+ million genes), the script includes a progress indicator. Every 1 million processed genes a status line is printed to stderr:

```
  Processed 1,000,000 genes...
  Processed 2,000,000 genes...
  ...
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

## Error handling

- No filename provided: prints usage message to stderr, exits with code 1.
- File not found: prints error to stderr, exits with code 1.
- File not readable or invalid encoding: prints error to stderr, exits with code 1.
- Malformed lines (too few columns): skipped with a warning printed to stderr at the end.

## Where to find things

| What | Where |
|---|---|
| Script | `gene_analyzer.py` |
| Input data | `gene_info` (or `gene_info.gz`) |
| Result output (JSON) | `results.json` |
| Result output (text) | `results.txt` |
| Discussion & answers | `exercise_01.md` |

## Data source

The gene_info dataset was downloaded from NCBI:

```
https://ftp.ncbi.nlm.nih.gov/gene/DATA/gene_info.gz
```
