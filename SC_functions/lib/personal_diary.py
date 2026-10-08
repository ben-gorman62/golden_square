# A function called make_snippet that takes a string as an argument and returns the first five words and 
# then a '...' if there are more than that.

#def make_snippet(snippet):
#    word_list = snippet.split(" ")
#    shortened_list = []
#    for word in word_list[:5]:
#        shortened_list.append(word)
#    if len(word_list) > 5:
#        return " ".join(shortened_list) + "..."
#    return " ".join(shortened_list)

def make_snippet(text):
    word_list = text.split(" ")
    return " ".join(word_list[:5]) + ("..." if len(word_list) > 5 else "")

def time_to_read(text):
    total_words = len(total_words.split())
    print(total_words)