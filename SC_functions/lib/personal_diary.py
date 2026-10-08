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

def count_words(text):
    if type(text) != str:
        raise Exception("Text is not a string.")
    if text == "":
        raise Exception("Text is empty.")
    return len(text.split(" "))

#TODO both of these need more tests i.e. not a string being input, and etc

# 200 wpm
def time_to_read(text):
    words_per_second = 200 / 60
    total_time = count_words(text) / words_per_second
    mins = total_time // 60 
    remainder = (total_time / 60) - mins
    secs = remainder * 60
    
    mins_label = "minute" if mins == 1 else "minutes"
    secs_label = "second" if secs == 1 else "seconds"
    
    if total_time > 60:
        return f"{int(mins)} {mins_label} {int(secs)} {secs_label}."
    return f"{int(total_time)} {secs_label}."
