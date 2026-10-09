class DiaryEntry:
    def __init__(self, title, contents):
        self.title = title
        self.contents = contents
        self.read_words = []

# Returns the title and contents in a Title: Contents format
    def format(self):
        return f"{self.title}: {self.contents}"

# Returns an integer representing the total number of words in contents
    def count_words(self):
        return len(self.contents.split(" "))

# Returns an integer number of minutes, rounded up, of the approximated time to read the 
# text given the reading speed of the user in words per minute.
    def reading_time(self, wpm):
        words_per_second = wpm / 60
        total_time = self.count_words() / words_per_second
        mins = total_time // 60 
        remainder = (total_time / 60) - mins
        if remainder > 0.05:
            mins += 1
        
        mins_label = "minute" if mins == 1 else "minutes"
        return f"{int(mins)} {mins_label}."

# Returns a chunk of the contents that the user could read in the given number of minutes and 
# with a given reading speed in words per minute.
    def reading_chunk(self, wpm, minutes):
        
        # The total number of readable words
        readable_words = wpm * minutes
        
        # If self.read_words has any existing words within, return the words of self.contents
        # starting from the index we left off at.
        if len(self.read_words) > 0:
            next_chunk_to_read = self.contents.split(" ")[
                len(self.read_words) : len(self.read_words) + readable_words
                ]
            
            # Adds the next set of read words into the list
            self.read_words.extend(next_chunk_to_read)
                
            if len(self.read_words) >= self.count_words():
                self.read_words = []
                
            return " ".join(next_chunk_to_read)
        
        
        # If the total amount of readable words in the time given is more than the total number 
        # of words in the contents, returns the full contents.
        if readable_words > self.count_words():
            return self.contents
        
        # The chunk_to_read is a list of all of the words that are needed to be read.
        # Found by splitting contents into a list of every words and slicing up to the total 
        # number of readable words.
        chunk_to_read = self.contents.split(" ")[:readable_words + 1]
        
        for word in chunk_to_read:
            self.read_words.append(word)
        
        # Returns the joined chunk list
        return " ".join(chunk_to_read)