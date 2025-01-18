class Solution(object):
    def doesValidArrayExist(self, derived):
        # Get the length of the derived array
        n = len(derived)
        
        # Try both possible initial values for the original array: 0 and 1
        for initial in [0, 1]:
            # Start the original array with the initial value
            original = [initial] 
            
            # Construct the rest of the original array
            # Each element is derived[i] XOR the last element of the original array
            for i in range(n - 1):
                original.append(derived[i] ^ original[-1])
            
            # Check if the last element of the original array XOR the first element
            # equals the last element of the derived array
            if (original[-1] ^ original[0]) == derived[-1]:
                return True  # A valid original array exists
        
        # If no valid original array is found, return False
        return False
