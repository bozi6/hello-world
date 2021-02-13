#!/usr/bin/env python3


text = 'Today is a beautiful day. Andy went fishing.'
words = text.replace('.', '')

sorted_words = sorted(words.split(), key=str.lower)
print('Case insensitive:', sorted_words)

sorted_words2 = sorted(words.split())
print('Case sensitive:', sorted_words2)
