# Preliminary genome assembly step to determine suitable k-mer size
## Contents
[Description](https://github.com/ololade-g/BIO539-python/blob/main/README.md#description)

[Installation](https://github.com/ololade-g/BIO539-python/blob/main/README.md##Installation)

[Usage](##Usage)

[Example](##Example)

[Testing](##Testing)

[License](##License)

## Description
This project entails the identification of substrings in genome reads, their possible substrings, and the subsequent substrings for each substring identified. It also identifies the smallest k size for which each substring of the sequence has only one unique subsequent substring.

The provided Python script, `script_smallest_k.py`, serves three main purposes:
* `find_substrings` Function: This function defines a method `find_substrings(sequence, k)` that takes an input DNA sequence and a desired substring length k. It identifies all valid substrings of length k containing only the characters A, C, G, and T. Additionally, it determines the immediate subsequent substring for each valid substring.
* `file_sequences` Function: This function processes DNA sequences from an input file. It reads the sequences, applies the `find_substrings` function, and stores the results in a dictionary. Each sequence is associated with its valid substrings and their subsequent substrings.
* `smallest_unique_k` Function: This function finds the smallest k for which there is only one possible unique subsequent substring for all substrings. It iterates through increasing k values until this condition is met or returns None if no such k exists.

## Installation
Installation of python3.0 or higher is required to reproduce this work

## Usage
Clone this repository to your local computer.
Ensure you have Python installed.
Run the scripts as needed:
Modify the input file path and desired substring length in `script_smallest_k.py`.
To process the sequences and generate results, execute:
```
python3 script_smallest_k.py
```

## Example
Download the provided `example.txt` file containing DNA sequence reads to your local computer. To analyze these sequences and find valid substrings, follow these steps:
Edit script_smallest_k.py to specify the correct file path to the `example.txt` file
Run the script: 
```
python3 script_smallest_k.py
```
The results will be the smallest size of k for which each substring has only one unique subsequent substring

## Testing
The functions in the script_smallest_k.py script can be tested using pytest. A test script `test_script.py` was created to test if the functions in `script_smallest_k.py` are being implemented correctly.
Navigate to the working directory, install pytest using pip and run the test: 
```
pip install pytest
pytest [path to test_script.py]
```

## License
This project is licensed under the MIT License
