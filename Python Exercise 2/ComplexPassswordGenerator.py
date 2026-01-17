import random


class ComplexPasswordGenerator:
    """
    A password generator that creates complex passwords with guaranteed
    inclusion of uppercase letters, lowercase letters, numbers, and symbols.
    """
    @staticmethod
    def Generate(password_length):
        """
        Generates a random complex password of the specified length.
        
        Args:
            password_length (int): The desired length of the password
            
        Returns:
            str: A shuffled password containing at least one character
                 from each category (uppercase, lowercase, number, symbol)
        """
        password = ""
        special_chars = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    
        # Add at least one character from each category to ensure complexity
        password += chr(random.randint(65, 90))  # Uppercase letter (A-Z)
        password += chr(random.randint(97, 122))  # Lowercase letter (a-z)
        password += chr(random.randint(48, 57))  # Digit (0-9)
        password += special_chars[random.randint(0, len(special_chars) - 1)]  # Special symbol
        
        # Fill remaining length by randomly selecting characters from any category
        while len(password) < password_length:
            # Randomly choose a character category and generate a character
            match random.randint(1, 4):
                case 1:
                    password += chr(random.randint(65, 90))  # Uppercase letter
                case 2:
                    password += chr(random.randint(97, 122))  # Lowercase letter
                case 3:
                    password += chr(random.randint(48, 57))  # Digit
                case 4:
                    password += special_chars[random.randint(0, len(special_chars) - 1)]  # Special symbol
        
        # Shuffle the password to randomize character positions
        password = ''.join(random.sample(password, len(password)))
        return password


# Test the password generator
passwd = ComplexPasswordGenerator.Generate(12)
print(passwd)
