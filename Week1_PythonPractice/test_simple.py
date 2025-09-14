def isAlienSorted(words, order):
    # Compare each pair of adjacent words
    for i in range(len(words) - 1):
        word1 = words[i]
        word2 = words[i + 1]
        
        # Compare these two words character by character
        for j in range(min(len(word1), len(word2))):
            char1 = word1[j]
            char2 = word2[j]
            
            # Find the position of each character in the alien alphabet
            position1 = order.find(char1)
            position2 = order.find(char2)
            
            # If word1's character comes after word2's character, they're not in order
            if position1 > position2:
                return False
            # If word1's character comes before word2's character, they are in order
            elif position1 < position2:
                break
            # If characters are equal, continue to next character
        
        # If all compared characters were equal, shorter word should come first
        if len(word1) > len(word2):
            return False
    
    # If we checked all pairs and they were all in order, the list is sorted
    return True

# Test it
words = ["hello", "leetcode"]
order = "hlabcdefgijkmnopqrstuvwxyz"
result = isAlienSorted(words, order)
print(f"Result: {result}")
