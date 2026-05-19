# Exercise 06 – DNA to Protein Discussion

## Task 1 – DNA to Protein using given functions

The functions `transcribe_dna_to_rna` and `translate_rna_to_protein` are used to translate a DNA sequence step by step: DNA to RNA, then RNA to protein.

## Task 2 – SequenceUtils (Static Methods Pattern)

A utility class `SequenceUtils` contains both methods as `@staticmethod`. Static methods belong to the class, not to an instance, so no object needs to be created to call them.

```python
rna = SequenceUtils.transcribe(dna_seq.seq)
protein = SequenceUtils.translate(rna)
```

## Task 3 – SequenceStorage

A class `SequenceStorage` that stores sequences by name using `save()` and retrieves them with `read()`.

## Task 4 – Singleton Pattern

The design pattern used is the Singleton Pattern. It ensures that only one instance of `SequenceStorage` can ever exist. Any call to `SequenceStorage()` returns the same object.

```python
storage1 = SequenceStorage()
storage2 = SequenceStorage()
storage1 is storage2  # True
```

This is useful when one shared storage should exist across the entire program.

Note: Tasks 3 and 4 are combined in the implementation. `SequenceStorage` was built directly as a Singleton. The key difference is conceptual: Task 3 introduces the storage class, Task 4 restricts it to one instance only.

## Task 5 – CD28 Protein Sequence

The coding sequence of CD28 is read from `cd28_cds.fasta` and translated using `SequenceUtils.transcribe()` and `SequenceUtils.translate()`. The stop codon (`*`) is removed as it is not part of the protein.

The protein sequence of CD28 (220 aa):
```
MLRLLLALNLFPSIQVTGNKILVKQSPMLVAYDNAVNLSCKYSYNLFSREFRASLHKGLDSAVEVCVVYGNYSQQLQVYSKTGFNCDGKLGNESVTFYLQNLYVNQTDIYFCKIEVMYPPPYLDNEKSNGTIIHVKGKHLCPSPLFPGPSKPFWVLVVVGGVLACYSLLVTVAFIIFWVRSKRSRLLHSDYMNMTPRRPGPTRKHYQPYAPPRDFAAYRS
```

The sequence can be verified against the official NCBI protein record [NP_006130.1](https://www.ncbi.nlm.nih.gov/protein/NP_006130.1).

## Task 6 – DNASequence and ProteinSequence classes

`DNASequence` wraps a BioPython `Seq` object and provides a `to_protein()` method to transcribe and translate the sequence.

`ProteinSequence` stores an amino acid sequence and provides:
- `length()` returns the number of amino acids
- `is_valid()` checks that all characters are valid amino acids (A, C, D, E, F, G, H, I, K, L, M, N, P, Q, R, S, T, V, W, Y)

## Task 7 – Factory Pattern

`SequenceFactory.create(type, sequence)` returns either a `DNASequence` or `ProteinSequence` based on the given type flag (`'dna'` or `'protein'`).

```python
dna = SequenceFactory.create('dna', 'ATGGCCATTGTAATGGGCCGCTGA')
prot = SequenceFactory.create('protein', 'MAAIVLVLLFLSAGQSIS')
```

This pattern centralizes object creation so the caller does not need to know which class to instantiate.

## Results

The full output of running `dna2protein.py` is documented in the README. The results are also saved to:

- [`results.json`](results.json) – structured output with all sequences
- [`results.txt`](results.txt) – plain text output
