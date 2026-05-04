# Exercise 01 – Discussion

**Sources:** [`results.json`](results.json) · [`results.txt`](results.txt)

## Gene Data Results

| Question | Answer |
|---|---|
| How many genes are listed? | 68,523,888 |
| How many genes are listed for Homo Sapiens? | 193,793 |
| Most common gene type | protein-coding |

**All gene types:**
biological-region, miscRNA, ncRNA, other, protein-coding, pseudo, rRNA, scRNA, snRNA, snoRNA, tRNA, unknown

---

## Discussion Questions

### 1. Is the filename hardcoded?
No. The filename is passed as a command-line argument via `sys.argv[1]`. This makes the tool flexible and reusable with any input file without modifying the source code.

### 2. How to increase the speed of testing?
- Use a small subset of the input file (e.g. first 10,000 lines) instead of the full dataset.
- Write unit tests with mock data or fixtures that don't require the real large file.

For more complex projects with many test cases, additional techniques become relevant:
- Use `pytest` with parameterized tests to cover multiple edge cases without duplicating test code.
- Run tests in parallel using `pytest-xdist` to reduce total runtime across a large test suite.

### 3. What happens if no input file is provided?
The program prints a usage message to stderr and exits with code 1:
```
Usage: python gene_analyzer.py INPUT_FILE
```
This is handled explicitly at the start of `main()`.

### 4. What happens if the input file contains an error?
Two cases are handled separately:

**File access errors**: if the file does not exist (`FileNotFoundError`), cannot be read (`OSError`, e.g. permission denied), or has invalid encoding (`UnicodeDecodeError`), the program prints a descriptive error message to stderr and exits with code 1.

**Malformed content**: lines with too few columns are skipped. Header lines starting with `#` are intentionally skipped (the `gene_info` format uses them). For any other malformed line, a warning is printed to stderr at the end of the run:

```
Warning: X malformed line(s) skipped.
```

This makes data loss visible instead of silent, especially important in a scientific context where unexpected skips could affect the result.

### 5. How to document the software?
- Add docstrings to all functions and classes (Google or NumPy style).
- Write a README.md with setup instructions, usage examples, and expected output.
- Use type hints to clarify function signatures.
- Generate API documentation automatically with tools like `pdoc` or `Sphinx`. Not necessary for this script, since it has only 3 functions and a single entry point. This becomes relevant when building a larger library or package with many modules, classes, and public APIs that other developers will import and use.

### 6. How to track changes?
Use Git as a version control system:
- Commit changes with descriptive messages.
- Use branches for new features or bug fixes.
- Host the repository on GitHub/GitLab for collaboration and history.

### 7. How could the software be delivered to clients?

**For technical users with Python installed:**
- Deliver as a zip file containing the script and README, simplest option, no installation needed beyond Python.
- Package it as a Python package (`pip install`) via PyPI.
- Bundle it as a Docker container for a reproducible environment (requires Docker knowledge).

**For end users without Python:**
- Provide a standalone executable built with PyInstaller, packages the script and Python runtime into a single binary. The client just runs the file, no Python installation required.

**Not suitable for this script:**
- Deploy as a REST API (e.g. with Flask) this script processes a 9 GB local file that cannot realistically be sent over HTTP. Even compressed (gzip), the file is still ~1.5 GB too large for a practical HTTP upload. This would make sense if the software were redesigned as a query service, e.g. looking up individual genes by ID from a pre-processed database.

### 8. How could the software be updated (on client environment)?
The update method depends on how the software was delivered (see Q7):
- ZIP: client downloads the new version and replaces the old script manually.
- Python package: `pip install --upgrade <package>` fetches the latest version from PyPI.
- Docker: `docker pull <image>` pulls the updated image; client restarts the container.
- Standalone executable: client downloads and replaces the new binary.

On the developer side, a CI/CD pipeline can automate building and publishing a new version (e.g. to PyPI or Docker Hub) on every release, but the client still updates via one of the methods above.

### 9. What is a good way to prevent bugs after an update?
- Maintain a comprehensive automated test suite (unit + integration tests).
- Use continuous integration (CI) to run tests on every commit/PR.
- Apply semantic versioning and a changelog to track breaking changes.
- Use linters (e.g. pylint, flake8) and type checkers (mypy) to catch issues early.
- Perform code review before merging any changes.