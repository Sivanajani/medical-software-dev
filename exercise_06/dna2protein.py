"""DNA to Protein translator demonstrating Static Methods, Singleton, and Factory patterns."""
from Bio.Seq import Seq
import random
import os
import json
from datetime import datetime


# --- Utility functions (kept for backwards compatibility) ---

def transcribe_dna_to_rna(dna: Seq) -> Seq:
    """Transcribe a DNA sequence to RNA."""
    return dna.transcribe()


def translate_rna_to_protein(rna: Seq) -> Seq:
    """Translate an RNA sequence to a protein sequence."""
    return rna.translate()


# --- Utility class with static methods ---

class SequenceUtils:
    """Utility class for DNA/RNA/protein sequence operations (Static Methods Pattern)."""

    @staticmethod
    def transcribe(dna_seq: Seq) -> Seq:
        """Transcribe a DNA sequence to RNA."""
        return dna_seq.transcribe()

    @staticmethod
    def translate(rna_seq: Seq) -> Seq:
        """Translate an RNA sequence to a protein sequence."""
        return rna_seq.translate()

    @staticmethod
    def dna_to_protein(dna_seq: Seq) -> Seq:
        """Transcribe and translate a DNA sequence to protein in one step."""
        rna = SequenceUtils.transcribe(dna_seq)
        return SequenceUtils.translate(rna)


# --- Singleton Pattern applied to SequenceStorage ---

class SequenceStorage:
    """Stores named sequences. Only one instance can exist (Singleton Pattern)."""

    _instance = None

    def __new__(cls) -> 'SequenceStorage':
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.data = {}
        return cls._instance

    def save(self, name: str, seq: object) -> None:
        """Store a sequence under the given name."""
        self.data[name] = seq

    def read(self, name: str) -> object:
        """Retrieve a sequence by name. Returns None if not found."""
        return self.data.get(name)

    def all_names(self) -> list[str]:
        """Return a list of all stored sequence names."""
        return list(self.data.keys())


# --- Sequence classes ---

class DNASequence:
    """Represents a DNA sequence with translation capability."""

    def __init__(self, raw: str) -> None:
        self.seq = Seq(raw.upper())

    def to_protein(self) -> str:
        """Transcribe and translate to protein string."""
        return str(SequenceUtils.dna_to_protein(self.seq))

    def __str__(self) -> str:
        return str(self.seq)


class ProteinSequence:
    """Represents a protein (amino acid) sequence."""

    VALID_AMINO_ACIDS = set('ACDEFGHIKLMNPQRSTVWY')

    def __init__(self, raw: str) -> None:
        self.seq = raw.upper()

    def length(self) -> int:
        """Return the number of amino acids in the sequence."""
        return len(self.seq)

    def is_valid(self) -> bool:
        """Return True if the sequence contains only valid amino acid characters."""
        return all(aa in self.VALID_AMINO_ACIDS for aa in self.seq)

    def __str__(self) -> str:
        return self.seq


# --- Factory Pattern ---

class SequenceFactory:
    """Creates DNASequence or ProteinSequence objects based on a type flag (Factory Pattern)."""

    @staticmethod
    def create(sequence_type: str, raw_sequence: str) -> DNASequence | ProteinSequence:
        """Return a DNASequence or ProteinSequence based on sequence_type ('dna' or 'protein')."""
        if sequence_type == 'dna':
            return DNASequence(raw_sequence)
        if sequence_type == 'protein':
            return ProteinSequence(raw_sequence)
        raise ValueError(f"Unknown sequence type: {sequence_type}")


# --- DNA Sequence Generator ---

class DNASequenceGenerator:
    """Generates random DNA sequences."""

    alphabet = ['A', 'C', 'G', 'T']

    def create_sequence(self, n: int) -> str:
        """Return a random DNA sequence of length n."""
        return ''.join(random.choice(DNASequenceGenerator.alphabet) for _ in range(n))


# --- Helper functions ---

def read_fasta_sequence(filepath: str) -> dict[str, str]:
    """Parse a FASTA file and return a dict of header to sequence string."""
    sequences = {}
    current_header = None
    current_seq = []
    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line.startswith('>'):
                if current_header:
                    sequences[current_header] = ''.join(current_seq)
                current_header = line[1:].split()[0]
                current_seq = []
            else:
                current_seq.append(line)
    if current_header:
        sequences[current_header] = ''.join(current_seq)
    return sequences


def find_first_orf(dna_str: str) -> tuple[str | None, str | None]:
    """Return the first open reading frame (ATG to stop codon) found."""
    dna = dna_str.upper()
    for i in range(len(dna) - 2):
        if dna[i:i+3] == 'ATG':
            codon_seq = dna[i:]
            remainder = len(codon_seq) % 3
            if remainder:
                codon_seq = codon_seq[:-remainder]
            protein = Seq(codon_seq).translate()
            stop_pos = str(protein).find('*')
            if stop_pos > 0:
                return dna[i:i + (stop_pos + 1) * 3], str(protein[:stop_pos])
    return None, None


if __name__ == '__main__':
    # 1. Simple translation of a known coding sequence
    test_dna = Seq('GTGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG')
    rna = transcribe_dna_to_rna(test_dna)
    protein = translate_rna_to_protein(rna)
    print(f"DNA:     {test_dna}")
    print(f"RNA:     {rna}")
    print(f"Protein: {protein}")
    print()

    # 2. Using utility class static methods explicitly
    dna_seq = DNASequence('ATGGCCATTGTAATGGGCCGCTGA')
    rna = SequenceUtils.transcribe(dna_seq.seq)
    protein = SequenceUtils.translate(rna)
    print(f"SequenceUtils.transcribe: {rna}")
    print(f"SequenceUtils.translate:  {protein}")
    print()

    # 3. Singleton storage
    storage1 = SequenceStorage()
    storage2 = SequenceStorage()
    storage1.save('test_dna', dna_seq)
    print(f"Singleton: storage1 is storage2 = {storage1 is storage2}")
    print(f"Stored sequence: {storage2.read('test_dna')}")
    print()

    # 4. CD28 coding sequence from CDS FASTA
    cds_path = os.path.join(os.path.dirname(__file__), 'cd28_cds.fasta')
    if os.path.exists(cds_path):
        seqs = read_fasta_sequence(cds_path)
        header = list(seqs.keys())[0]
        cd28_dna = seqs[header]
        print(f"CD28 CDS length: {len(cd28_dna)} bp")

        rna = SequenceUtils.transcribe(Seq(cd28_dna))
        cd28_protein = str(SequenceUtils.translate(rna)).rstrip('*')
        print(f"CD28 protein sequence ({len(cd28_protein)} aa): {cd28_protein}")

        storage = SequenceStorage()
        storage.save('cd28_dna', SequenceFactory.create('dna', cd28_dna))
        storage.save('cd28_protein', SequenceFactory.create('protein', cd28_protein))
        print(f"Stored sequences: {storage.all_names()}")
    print()

    # 5. Factory pattern: DNASequence and ProteinSequence
    dna_via_factory = SequenceFactory.create('dna', 'ATGGCCATTGTAATGGGCCGCTGA')
    prot_via_factory = SequenceFactory.create('protein', 'MAAIVLVLLFLSAGQSIS')
    print(f"Factory DNA:     {dna_via_factory}")
    print(f"Factory Protein: {prot_via_factory}")
    print(f"Protein length:  {prot_via_factory.length()} aa")
    print(f"Protein valid:   {prot_via_factory.is_valid()}")
    print()

    # 6. Random DNA
    gen = DNASequenceGenerator()
    rand_dna = DNASequence(gen.create_sequence(30))
    print(f"Random DNA:     {rand_dna}")
    print(f"Random protein: {rand_dna.to_protein()}")

    # Save results to JSON and TXT
    output_dir = os.path.dirname(os.path.abspath(__file__))
    timestamp = datetime.now().isoformat()
    results = {
        "generated_by": "dna2protein.py",
        "timestamp": timestamp,
        "cd28_protein": cd28_protein if os.path.exists(cds_path) else None,
        "cd28_protein_length": len(cd28_protein) if os.path.exists(cds_path) else None,
    }

    json_path = os.path.join(output_dir, "results.json")
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2)
    print(f"\nResults saved to: {json_path}", file=__import__('sys').stderr)

    txt_path = os.path.join(output_dir, "results.txt")
    with open(txt_path, "w", encoding="utf-8") as f:
        f.write(f"# Generated by dna2protein.py at {timestamp}\n")
        if os.path.exists(cds_path):
            f.write(f"CD28 protein ({len(cd28_protein)} aa):\n{cd28_protein}\n")
    print(f"Results saved to: {txt_path}", file=__import__('sys').stderr)
