import sys
import hashlib
import gzip
import collections
import json
import os

HOMO_SAPIENS_TAX_ID = "9606"
TYPE_OF_GENE_COL = 9


def compute_md5(filepath):
    print("Computing MD5...", flush=True)
    h = hashlib.md5()
    with open(filepath, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def open_file(filepath):
    with open(filepath, "rb") as f:
        magic = f.read(2)
    if magic == b"\x1f\x8b":
        return gzip.open(filepath, "rt", encoding="utf-8")
    return open(filepath, "r", encoding="utf-8")


def analyze(filepath):
    total_genes = 0
    homo_sapiens_genes = 0
    gene_type_counts = collections.Counter()

    print("Analyzing genes...", flush=True)

    with open_file(filepath) as f:
        for line in f:
            if line.startswith("#"):
                continue
            parts = line.rstrip("\n").split("\t")
            if len(parts) <= TYPE_OF_GENE_COL:
                continue
            total_genes += 1

            # Progress every 1 million lines
            if total_genes % 1_000_000 == 0:
                print(f"  Processed {total_genes:,} genes so far...", flush=True)

            if parts[0] == HOMO_SAPIENS_TAX_ID:
                homo_sapiens_genes += 1
            gene_type = parts[TYPE_OF_GENE_COL]
            if gene_type:
                gene_type_counts[gene_type] += 1

    return total_genes, homo_sapiens_genes, gene_type_counts


def main():
    if len(sys.argv) < 2:
        print("Usage: python gene_analyzer.py INPUT_FILE", file=sys.stderr)
        sys.exit(1)

    filepath = sys.argv[1]

    try:
        md5 = compute_md5(filepath)
        total, homo_sapiens, gene_type_counts = analyze(filepath)
    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found.", file=sys.stderr)
        sys.exit(1)
    except (OSError, UnicodeDecodeError) as e:
        print(f"Error reading file: {e}", file=sys.stderr)
        sys.exit(1)

    gene_types_sorted = sorted(gene_type_counts.keys())
    most_common_type = gene_type_counts.most_common(1)[0][0]

    # --- Required output (5 lines) ---
    print("\n=== RESULTS ===")
    print(md5)
    print(total)
    print(homo_sapiens)
    print(", ".join(gene_types_sorted))
    print(most_common_type)

    # --- Save JSON ---
    results = {
        "md5": md5,
        "total_genes": total,
        "homo_sapiens_genes": homo_sapiens,
        "gene_types": gene_types_sorted,
        "most_common_gene_type": most_common_type,
        "gene_type_counts": dict(gene_type_counts)
    }

    output_dir = os.path.dirname(filepath)
    json_path = os.path.join(output_dir, "results.json")
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2)

    print(f"\nResults saved to: {json_path}", flush=True)


if __name__ == "__main__":
    main()