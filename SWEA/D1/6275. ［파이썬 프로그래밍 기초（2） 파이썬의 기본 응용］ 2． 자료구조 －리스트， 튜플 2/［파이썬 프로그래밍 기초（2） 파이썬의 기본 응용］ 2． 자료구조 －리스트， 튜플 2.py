sentence = 'Python is powerful... and fast; plays well with others; runs everywhere; is friendly & easy to learn; is Open.'
result = ''.join([s for s in sentence if s not in 'aeiou'])
print(result)