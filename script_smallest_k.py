#QUESTION 1
def find_substrings(sequence, k):
    """
    Finds all substrings of length k in the given sequence and identifies the immediate subsequent substring for each.

    Args:
        sequence (str): The input sequence.
        k (int): The desired length of substrings.

    Returns:
        tuple: A tuple containing:
            - list: All substrings of size k.
            - dict: A dictionary where keys are substrings and values are sets of unique subsequent substrings.
    """
    # This function finds all substrings of length k in the given sequence
    all_substrings = [sequence[i:i+k] for i in range(len(sequence) - k + 1)]
    
    # This dictionary will hold the immediate subsequent substring for each substring
    subsequent_substrings = {}
    
    # Iterate over each substring
    for index, substring in enumerate(all_substrings):
        # Only consider the substring that directly follows the current one
        next_index = index + 1
        if next_index < len(sequence) - k + 1:
            next_substring = sequence[next_index:next_index+k]
            # Check if the next substring is already in the dictionary
            if substring not in subsequent_substrings:
                subsequent_substrings[substring] = set()
            # Add the next substring to the set for the current substring
            subsequent_substrings[substring].add(next_substring)
    
    return all_substrings, subsequent_substrings


#QUESTION 2
def process_file_sequences(file_path, k):
    """
    Processes sequences from a file, finding all substrings and their subsequent substrings.

    Args:
        file_path (str): Path to the input file containing sequences.
        k (int): The desired length of substrings.

    Returns:
        dict: A dictionary where keys are sequences and values are dictionaries with 'all_substrings' and 'subsequent_substrings'.
    """
    # Open the file and read all sequences
    with open(file_path, 'r') as file:
        sequences = file.read().splitlines()
    
    # Dictionary to hold the results for each sequence
    results = {}
    
    # Process each sequence in the file
    for sequence in sequences:
        # Use the find_substrings function to get all substrings and their subsequent substrings
        all_substrings, subsequent_substrings = find_substrings(sequence, k)
        # Store the results in the dictionary
        results[sequence] = {
            'all_substrings': all_substrings,
            'subsequent_substrings': subsequent_substrings
        }
    
    return results

if __name__ == "__main__":
    file_path = "../../shared/439539/reads.fa"
     
#QUESTION 3
def find_smallest_unique_k(results):
    """
    Finds the smallest k for which there is only one possible unique subsequent substring for all substrings.

    Args:
        results (dict): The dictionary returned by process_file_sequences function.

    Returns:
        int: The smallest k value or None if no such k exists.
    """
    # Initialize k to 1
    k = 1
    
    # Flag to check if all substrings have a unique subsequent substring
    all_unique = False
    
    # Loop until all substrings have a unique subsequent substring
    while not all_unique:
        all_unique = True  # Assume all are unique for the current k
        
        # Check each sequence's substrings for uniqueness
        for sequence in results:
            substrings_info = results[sequence]
            for substr, subsequents in substrings_info['subsequent_substrings'].items():
                if len(subsequents) != 1:
                    all_unique = False
                    break  # No need to check further if one is not unique
            
            if not all_unique:
                break  # No need to check other sequences if one sequence fails
        
        # If not all are unique, increment k and repeat the process
        if not all_unique:
            k += 1
            # Re-process the file with the new k value
            results = process_file_sequences(file_path, k)
        else:
            # All substrings have a unique subsequent substring
            return k
    
    # If the loop exits without finding a unique k, return None
    return None

# Example usage:
# Assuming 'file_path' is defined and accessible
results = process_file_sequences(file_path, 1)
smallest_k = find_smallest_unique_k(results)
if smallest_k is not None:
    print(f"The smallest k size for which there is only one possible unique subsequent substring for all the substring is: {smallest_k}")
else:
    print("No such k size exists where each substring has a unique subsequent substring.")
