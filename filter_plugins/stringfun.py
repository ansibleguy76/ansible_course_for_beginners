# we make custom ansible filter plugin

class FilterModule(object):

    def filters(self):
        return {
            'reverse_string': self.reverse_string,
            'title_string': self.title_string,
            'prefix_string': self.prefix_string,
            'suffix_string': self.suffix_string,
            'get_middle_word_of_sentence': self.get_middle_word_of_sentence,
            
        }

    def reverse_string(self, value):
        return value[::-1]
    
    def title_string(self, value):
        # the method return the string but with a space every 1 character and all caps
        return ' '.join(value.upper())
    
    def prefix_string(self, value, prefix):
        return prefix + value
    
    def suffix_string(self, value, suffix):
        return value + suffix

    def get_middle_word_of_sentence(self, value):
        # the method return the middle word of a sentence
        # if the sentence has an even number of words, it returns the two middle words
        words = value.split()
        if len(words) % 2 == 0:
            return words[len(words) // 2 - 1], words[len(words) // 2]
        else:
            return words[len(words) // 2]