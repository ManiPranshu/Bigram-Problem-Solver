# Helper function to extract bigrams from a word
def generate_bigrams(word):
    """Generates a list of bigrams for a given word."""
    return [word[i:i+2] for i in range(len(word) - 1)]

def sort_bigrams(bigrams):
    """Sorts the bigrams using the specified procedure and returns the 5 smallest."""
    # Initialize the array of size 676
    array = [0] * (26 * 26)
    
    # Mark the array based on the bigrams
    for bigram in bigrams:
        index = 26 * (ord(bigram[0]) - ord('a')) + (ord(bigram[1]) - ord('a'))
        array[index] = 1
    
    # Traverse the array to get the first 5 smallest bigrams
    sorted_bigrams = []
    for i in range(26 * 26):
        if array[i] == 1:
            first_char = chr(i // 26 + ord('a'))
            second_char = chr(i % 26 + ord('a'))
            sorted_bigrams.append(first_char + second_char)
            if len(sorted_bigrams) == 5:
                break
    
    return sorted_bigrams

def process_words(words):
    """Processes the list of words to generate the unordered map."""
    bigram_map = {}
    
    for word in words:
        bigrams = generate_bigrams(word)
        sorted_bigrams = sort_bigrams(bigrams)  # Get 5 smallest lexicographically sorted bigrams
        key = tuple(sorted_bigrams)  # Use tuple to make it hashable for dictionary key
        
        if key not in bigram_map:
            bigram_map[key] = []
        
        if len(bigram_map[key]) < 5:
            bigram_map[key].append(word)
    
    return bigram_map

def print_model(model):
    """Prints all key-value pairs in the trained model."""
    for key, value in model.items():
        print(f"Key (sorted bigrams): {key} -> Value (original words): {value}")

################################
# Non Editable Region Starting #
################################
def my_fit(dictionary):
################################
#  Non Editable Region Ending  #
################################
    # Do not perform any file IO in your code
    # Use this method to train your model using the word list provided
    
    bigram_map = process_words(dictionary)
    
    # Print all key-value pairs in the trained model
    print_model(bigram_map)
    
    return bigram_map

    # Return the trained model


################################
# Non Editable Region Starting #
################################
def my_predict(model, bigram_list):
################################
#  Non Editable Region Ending  #
################################
    key = tuple(bigram_list)
    
    # Return the words corresponding to the bigram_list key
    return model.get(key, [])
    # Do not perform any file IO in your code
    # Use this method to predict on a test bigram_list
    # Ensure that you return a list even if making a single guess
