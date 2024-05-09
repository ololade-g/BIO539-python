#!/usr/bin/env python3

file_path = "../../shared/439539/reads.fa"

#QUESTION 1
def find_substrings(sequence, k):
    """
    Finds all substrings of length k in the given sequence that contain only A, C, G, and T,
    and identifies the immediate subsequent substring for each.

    Args:
        sequence (str): The input sequence.
        k (int): The desired length of substrings.

    Returns:
        tuple: A tuple containing:
            - list: All substrings of size k that contain only A, C, G, and T.
            - dict: A dictionary where keys are substrings and values are sets of unique subsequent substrings.
    """
    # Define the valid characters
    valid_chars = {'A', 'C', 'G', 'T'}
    
    # Initialize the list of all valid substrings and the dictionary for subsequent substrings
    all_substrings = []
    subsequent_substrings = {}
    
    # Initialize the index
    i = 0
    # Loop through the sequence until there are no more substrings of length k
    while i <= len(sequence) - k:
        # Extract the substring of length k
        substring = sequence[i:i+k]
        # Check if the substring contains only valid characters
        if set(substring).issubset(valid_chars):
            # If valid, add the substring to the list of all substrings
            all_substrings.append(substring)
            # Check if there is a subsequent substring to consider
            if i < len(sequence) - k:
                # Extract the subsequent substring
                next_substring = sequence[i+1:i+k+1]
                # Check if the subsequent substring is also valid
                if set(next_substring).issubset(valid_chars):
                    # If valid, add it to the set of subsequent substrings
                    if substring not in subsequent_substrings:
                        subsequent_substrings[substring] = set()
                    subsequent_substrings[substring].add(next_substring)
            # Move to the next character in the sequence
            i += 1
        else:
            # If an invalid character is found, skip it
            i += 1
            # Continue skipping any subsequent invalid characters
            while i < len(sequence) and sequence[i] not in valid_chars:
                i += 1

    # Return the list of all valid substrings and the dictionary of subsequent substrings
    return all_substrings, subsequent_substrings


#QUESTION 2
def file_sequences(file_path, k):
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
     
#QUESTION 3
def smallest_unique_k(results):
    """
    Finds the smallest k for which there is only one possible unique subsequent substring for all substrings.

    Args:
        results (dict): The dictionary returned by "file_sequences" function.

    Returns:
        int: The smallest k value or None if no such k exists.
    """
    # If results is empty, return None
    if not results:
        return None
    
    # Initialize k to 1
    k = 1
    
    # Loop until all substrings have a unique subsequent substring
    while True:
        # Check each sequence's substrings for uniqueness
        all_unique = True  # Assume all are unique for the current k
        for sequence in results:
            subsequents = results[sequence]['subsequent_substrings']
            for substr, subsequent_set in subsequents.items():
                if len(subsequent_set) != 1:
                    all_unique = False
                    break  # No need to check further if one is not unique
            if not all_unique:
                break  # No need to check other sequences if one sequence fails
        
        # If all are unique, return the current k
        if all_unique:
            return k
        
        # Otherwise, increment k and re-process the file
        k += 1
        results = file_sequences(file_path, k)
    
    # If the loop exits without finding a unique k, return None
    return None

# Print the lowest k size identified by the find_smallest_unique_k function
if __name__ == "__main__":
  results = file_sequences(file_path, 1)
  smallest_k = smallest_unique_k(results)
  if smallest_k is not None:
    print(f"The smallest k size for which there is only one possible unique subsequent substring for all the substrings is: {smallest_k}")
else:
    print("No such k size exists where each substring has a unique subsequent substring.")
