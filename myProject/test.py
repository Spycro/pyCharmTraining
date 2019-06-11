import string


a = "This is a long phrase,--the thing ?"

print(a.replace(string.punctuation, ' '))
t = a.split()


print('///////////////////')

res = []
for line in t:
    word = line.strip(string.punctuation)
    res.append(word)
for i in range(len(res)):
    res[i] = res[i].replace('-', ' ')


print(res)

res.remove('')
print(res)