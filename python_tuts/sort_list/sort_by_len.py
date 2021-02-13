#!/usr/bin/env python3


def w_len(e):
    return len(e)


words = ['forest', 'wood', 'tool', 'sky', 'poor', 'cloud', 'rock', 'if']

words.sort(reverse=True, key=w_len)

print(words)
