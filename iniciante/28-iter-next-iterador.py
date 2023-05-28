text = 'Felipe'

print(iter(text))
text = text.__iter__()
print(text)

print(text.__next__())
print(text.__next__())
print(text.__next__())
print(text.__next__())
print(text.__next__())
print(text.__next__())
# print(text.__next__()) # erro StopIteration

text = 'Felipe'.__iter__()
print(next(text))