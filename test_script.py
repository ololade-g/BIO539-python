
#1) TEST THE find_substrings FUNCTION

from script_smallest_k import find_substrings

def test_find_substrings():
    # Test 1: Basic input
    sequence = "AGTCTA"
    k = 2
    all_substrings, subsequent_substrings = find_substrings(sequence, k)
    assert all_substrings == ["AG", "GT", "TC", "CT", "TA"]
    assert subsequent_substrings == {"AG": {"GT"}, "GT": {"TC"}, "TC": {"CT"}, "CT": {"TA"}}

    # Test 2: larger k-mer and longersequence
    sequence = "ATGTCTATAG"
    k = 3
    all_substrings, subsequent_substrings = find_substrings(sequence, k)
    assert all_substrings == ["ATG", "TGT", "GTC", "TCT", "CTA", "TAT", "ATA", "TAG"]
    assert subsequent_substrings == {"ATG": {"TGT"}, "TGT": {"GTC"}, "GTC": {"TCT"}, "TCT": {"CTA"}, "CTA": {"TAT"},
    "TAT": {"ATA"}, "ATA": {"TAG"}}

    # Test 3: Empty sequence
    sequence = ""
    k = 1
    all_substrings, subsequent_substrings = find_substrings(sequence, k)
    assert all_substrings == []
    assert subsequent_substrings == {}
    
    # Test 4: At least one substring with more than one unique subsequent substring
    sequence = "AGTCTAGC"
    k = 2
    all_substrings, subsequent_substrings = find_substrings(sequence, k)
    assert all_substrings == ["AG", "GT", "TC", "CT", "TA", "AG", "GC"]
    assert subsequent_substrings == {"AG": {"GT","GC"}, "GT": {"TC"}, "TC": {"CT"}, "CT": {"TA"}, "TA": {"AG"}}
    
    # Test 5: Sequence with repeated characters
    sequence = "ATTTTT"
    k = 3
    all_substrings, subsequent_substrings = find_substrings(sequence, k)
    assert all_substrings == ["ATT", "TTT", "TTT", "TTT"]
    assert subsequent_substrings == {"ATT": {"TTT"}, "TTT": {"TTT"}}

    # Test 6: Sequence with characters other than A,G,T,C
    sequence = "xyz"
    k = 1
    all_substrings, subsequent_substrings = find_substrings(sequence, k)
    assert all_substrings == []
    assert subsequent_substrings == {}
    
    # Test 7: Sequence with mixed valid and invalid characters
    sequence = "ACGTXYZACGTG"
    k = 3
    all_substrings, subsequent_substrings = find_substrings(sequence, k)
    assert all_substrings == ['ACG', 'CGT', 'ACG', 'CGT', 'GTG']
    assert subsequent_substrings == {'ACG': {'CGT'}, 'CGT': {'GTG'}}

if __name__ == "__main__":
    import pytest
    pytest.main()
    


#2) TEST THE find_sequences FUNCTION
    
import pytest

from script_smallest_k import file_sequences


# Test 1: File with valid sequences

# Fixture to create a test file with valid sequences
@pytest.fixture
def valid_sequences_file(tmp_path):
    file_path = tmp_path / 'valid_sequences.txt'
    file_content = 'ACGTACGT'
    # Create the file and write the content
    file_path.write_text(file_content)
    # Return the file path for the test to use
    return str(file_path)

# Test function using the valid_sequences_file fixture
def test_file_sequences(valid_sequences_file):
    k = 3
    expected_results = {
        'ACGTACGT': {
            'all_substrings': ['ACG', 'CGT', 'GTA', 'TAC', 'ACG', 'CGT'],
            'subsequent_substrings': {'ACG': {'CGT'}, 'CGT': {'GTA'}, 'GTA': {'TAC'}, 'TAC': {'ACG'}}
        },
        # Add more sequences and expected results here
    }
    assert file_sequences(valid_sequences_file, k) == expected_results


# Test 2: File with an empty sequence

# Fixture to create an empty test file
@pytest.fixture
def empty_sequences_file(tmp_path):
    file_path = tmp_path / 'empty_sequences.txt'
    file_content = ''
    # Create the file and write the content
    file_path.write_text(file_content)
    # Return the file path for the test to use
    return str(file_path)

# Test function using the empty_sequences_file fixture
def test_file_sequences_empty_file(empty_sequences_file):
    k = 3
    expected_results = {}
    assert file_sequences(empty_sequences_file, k) == expected_results


# Test 3: File with sequences containing invalid characters

# Fixture to create a test file with invalid characters
@pytest.fixture
def invalid_sequences_file(tmp_path):
    file_path = tmp_path / 'invalid_sequences.txt'
    file_content = 'ACGTXYZACGT\nACGTACGTACA\n'  # Add invalid characters here
    # Create the file and write the content
    file_path.write_text(file_content)
    # Return the file path for the test to use
    return str(file_path)

# Test function using the invalid_sequences_file fixture
def test_file_sequences_invalid_chars(invalid_sequences_file):
    k = 3
    expected_results = {
        'ACGTXYZACGT': {
            'all_substrings': ['ACG', 'CGT', 'ACG', 'CGT'],
            'subsequent_substrings': {'ACG': {'CGT'}}
        },
        'ACGTACGTACA': {
            'all_substrings': ['ACG', 'CGT', 'GTA', 'TAC', 'ACG', 'CGT', 'GTA', 'TAC', 'ACA'],
            'subsequent_substrings': {'ACG': {'CGT'}, 'CGT': {'GTA'}, 'GTA': {'TAC'}, 'TAC': {'ACG', 'ACA'}}
        },
    }
    assert file_sequences(invalid_sequences_file, k) == expected_results



# Test 4: File with sequences of varying lengths

# Fixture to create a test file with sequences of varying lengths
@pytest.fixture
def varying_length_sequences_file(tmp_path):
    # Define the file path for the test file
    file_path = tmp_path / 'varying_length_sequences.txt'
    # Define the content of the file, which includes sequences of varying lengths
    file_content = 'ACGT\nAC\n'  # The first sequence is 4 characters long, the second is 2
    # Create the file and write the content
    file_path.write_text(file_content)
    # Return the file path for the test to use
    return str(file_path)

# Test function to check if file_sequences handles sequences of varying lengths correctly
def test_file_sequences_varying_lengths(varying_length_sequences_file):
    # Define the length of substrings to be found
    k = 3
    # Define the expected results for sequences of varying lengths
    expected_results = {
        'ACGT': {
            'all_substrings': ['ACG', 'CGT'],  # Expected substrings of length 3 from 'ACGT'
            'subsequent_substrings': {'ACG': {'CGT'}}  # 'CGT' follows 'ACG'
        },
        'AC': {
            'all_substrings': [],  # No substrings of length 3 can be formed from 'AC'
            'subsequent_substrings': {}  # No subsequent substrings as there are no valid substrings
        },
    }
    # Call the file_sequences function with the path provided by the fixture and the substring length
    # Assert that the actual results match the expected results
    assert file_sequences(varying_length_sequences_file, k) == expected_results



# Test 5: File with sequences and k larger than any sequence length

@pytest.fixture
def large_k_sequences_file(tmp_path):
    # Define the file path for the test file
    file_path = tmp_path / 'large_k_sequences.txt'
    # Define the content of the file, which is a single sequence
    file_content = 'ACGTACGTACGTC'  # No invalid characters are present
    # Create the file and write the content
    file_path.write_text(file_content)
    # Return the file path for the test to use
    return str(file_path)

# Test function to check if file_sequences handles large k values correctly
def test_file_sequences_large_k(large_k_sequences_file):
    # Define the large value of k
    k = 10
    # Define the expected results for a large k value
    expected_results = {
        'ACGTACGTACGTC': {
            'all_substrings': ['ACGTACGTAC', 'CGTACGTACG', 'GTACGTACGT', 'TACGTACGTC'],
            'subsequent_substrings': {'ACGTACGTAC': {'CGTACGTACG'}, 'CGTACGTACG': {'GTACGTACGT'}, 'GTACGTACGT': {'TACGTACGTC'}
            }
        },
        # Add more sequences and expected results here if needed
    }
    # Use the file path provided by the fixture and assert that the actual results match the expected results
    assert file_sequences(large_k_sequences_file, k) == expected_results



