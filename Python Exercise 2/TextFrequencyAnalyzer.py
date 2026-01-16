class TextFrequencyAnalyzer:
    """
    A utility class for analyzing word frequency in text.
    """
    @staticmethod
    def word_frequency(text):
        """
        Count the frequency of each word in the given text.
        
        Args:
            text (str): The input text to analyze
        
        Returns:
            dict: A dictionary where keys are words and values are their frequencies
        """
        # Convert text to lowercase and split into a list of words
        word_list=text.lower().split(" ")
        # Initialize an empty dictionary to store word counts
        word_count={}

        # Iterate through each word in the list
        for word in word_list:
            # Initialize count to 0 if this word hasn't been seen before
            if word not in word_count:
                word_count[word]=0

            # Increment the count for the current word
            word_count[word]+=1
        return word_count
    

# Get input text from the user
text=input("Enter the text to analyze frequency of each word used in text: \n")
# Analyze the text and get word frequency dictionary
word_frequency=TextFrequencyAnalyzer.word_frequency(text)
# Display the results
print(word_frequency)
