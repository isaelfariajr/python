def vowel_counter(string):
    """Counts the number of vowels in given string."""
    #vowel_count = 0
    #iterate over given string
    # for char in string:
    #     if char in 'aeiou':
    #         vowel_count += 1
    vowel_count = count_instance_of_string(string, 'aeiou')
    return vowel_count

def word_counter(sentence):
    """Counts the number of words in given sentence"""
    sentence = sentence.strip() #Remove whitespace from beginning and end of sentence
    # space_count = 0
    # for char in sentence:
    #     #check if character is single space
    #     if char in ' ':
    #         space_count += 1
    # word_count = space_count + 1

    num_spaces = count_instance_of_string(sentence, ' ')
    word_count = num_spaces + 1
    return word_count

def count_instance_of_string(string1, string2):
    """Counts characters in string1 are also in string2"""
    count = 0
    #for each char in string1, check if it's in string2
    for char in string1:
        if char in string2:
            count += 1
    return count

def main():
    while 1 == 1:
       input_string = input("Enter a String : ")
       if input_string == "-1":
           break
       print(vowel_counter(input_string), "vowels in", input_string)
       #print(word_counter(input_string), "words in", input_string)

#To execute main function
if __name__ == '__main__':
    main()