'''
Created on Sep 26, 2013

@author: anuj
'''

import decimal

class word_frequency_finder:
    def __init__(self, book_name, output):
        self.book_name = book_name
        self.output = output

    # OPENING THE STRIPPED FILE
    # PUTTING WORDS IN A HASHMAP    
    def find_wordcount(self):
        words = {}
        stripped_file = open(self.output, 'r')
        wordscount = 0;
        for line in stripped_file:
            wordscount += 1
            if(words.__contains__(line.strip())):
                words[line.strip()] += 1
            else:    
                words[line.strip()] = 1
        
        stripped_file.close()
                
        sorted_words = sorted(words.items(), key=lambda x:x[1])
        sorted_words.reverse()
        return  sorted_words, wordscount

if __name__ == '__main__':

    # CONSTANTS
    book_name = "ALICE'S ADVENTURES IN WONDERLAND"
    output = "output.txt"
    
    downloadedbook = word_frequency_finder(book_name, output)
    sorted_words, wordcount = downloadedbook.find_wordcount()

    count = 0;
    fwordcount = 0;
    
    mostfrequent = {}
    mostFfrequent = {}
    f_word_rank = []
    unique_words = 0
    more_than_five = 0;
    
    
    for word in sorted_words:
        count += 1
        
        if(count <= 25):
            mostfrequent[word[0]] = word[1]
        if(fwordcount <= 25):
            if(word[0][0] == 'f' and word[0] not in mostfrequent):
                fwordcount += 1
                mostFfrequent[word[0]] = word[1]
                f_word_rank.append(count)
        if(word[1] == 1):
            unique_words += 1 
        if(word[1] >= 5):
            more_than_five += word[1]       
    
    print '******************************************************'        
    print "Most frequent 25 words in %s " % book_name  
    
    sorted_mostfrequent = sorted(mostfrequent.items(), key=lambda x:x[1])
    sorted_mostfrequent.reverse()
    for word in sorted_mostfrequent:
        print "word : " + word[0] + " and occurrence : %s" % word[1]
    
    print '******************************************************'
    print "Most frequent 25 words with rank starting with 'f' in %s " % book_name  
    
    sorted_mostFfrequent = sorted(mostFfrequent.items(), key=lambda x:x[1])
    sorted_mostFfrequent.reverse()
    count = 0;
    
    for word in sorted_mostFfrequent:
        probability = round((decimal.Decimal(float(word[1]) / wordcount) * 
                                 100), 4)
        product = probability * f_word_rank[count]
        print "word : " + word[0] + " occurrence : %s" % word[1] + \
              " times rank : %s" % f_word_rank[count] + " Probability : %s" \
              % probability + " product : %s" % product 
        count += 1
    
    print '******************************************************'
    print 'Total unique words : %s' % unique_words
    print "Total words : %s" % wordcount    
    print "Total fewer than five words : %s" % (wordcount - more_than_five)

