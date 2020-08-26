import collections
import pandas as pd

import sys
# Read input file, note the encoding is specified here 
# It may be different in your text file
file = open(sys.argv[1], encoding="utf8")
a= file.read()

wordcount = {}
# To eliminate duplicates, remember to split by punctuation, and use case demiliters.
for word in a.split():
    if word not in wordcount:
        wordcount[word] = 1
    else:
        wordcount[word] += 1
# Print most common word
n_print = int(input("How many most common words to print: "))
print("\nOK. The {} most common words are as follows\n".format(n_print))
word_counter = collections.Counter(wordcount)
for word, count in word_counter.most_common(n_print):
    print(word, ": ", count)
# Close the file
file.close()
# Create a data frame of the most common words 
# Draw a bar chart
lst = word_counter.most_common(n_print)
df = pd.DataFrame(lst, columns = ['Word', 'Count'])
df.to_csv("frequency_blogs.csv")