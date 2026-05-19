# Exercise 06 – DNA to Protein

A Python script that translates a DNA sequence into a protein sequence using BioPython. The exercise demonstrates three design patterns: Static Methods, Singleton, and Factory.

## Setup

Install BioPython if not already installed:

```bash
pip install biopython
```

## Usage

```bash
python3 dna2protein.py
```

## Output

```
DNA:     GTGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG
RNA:     GUGGCCAUUGUAAUGGGCCGCUGAAAGGGUGCCCGAUAG
Protein: VAIVMGR*KGAR*

SequenceUtils.transcribe: AUGGCCAUUGUAAUGGGCCGCUGA
SequenceUtils.translate:  MAIVMGR*

Singleton: storage1 is storage2 = True
Stored sequence: ATGGCCATTGTAATGGGCCGCTGA

CD28 CDS length: 663 bp
CD28 protein sequence (220 aa): MLRLLLALNLFPSIQVTGNKILVKQSPMLVAYDNAVNLSCKYSYNLFSREFRASLHKGLDSAVEVCVVYGNYSQQLQVYSKTGFNCDGKLGNESVTFYLQNLYVNQTDIYFCKIEVMYPPPYLDNEKSNGTIIHVKGKHLCPSPLFPGPSKPFWVLVVVGGVLACYSLLVTVAFIIFWVRSKRSRLLHSDYMNMTPRRPGPTRKHYQPYAPPRDFAAYRS
Stored sequences: ['test_dna', 'cd28_dna', 'cd28_protein']

Factory DNA:     ATGGCCATTGTAATGGGCCGCTGA
Factory Protein: MAAIVLVLLFLSAGQSIS
Protein length:  18 aa
Protein valid:   True

Random DNA:     ...
Random protein: ...
```

## Where to find things

| What | Where |
|---|---|
| Script | [`dna2protein.py`](dna2protein.py) |
| CD28 CDS sequence | [`cd28_cds.fasta`](cd28_cds.fasta) |
| Result output (JSON) | [`results.json`](results.json) |
| Result output (text) | [`results.txt`](results.txt) |
| Discussion & answers | [`exercise_06.md`](exercise_06.md) |

## Data source

The CD28 CDS sequence was downloaded from [NCBI Gene (Gene ID: 940)](https://www.ncbi.nlm.nih.gov/gene/940).
