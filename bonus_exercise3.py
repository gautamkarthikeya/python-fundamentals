words_str=input('Enter a set of words separated by commas:')
list=words_str.split(',')
print(','.join(sorted(list)))