
string = input("digite sua palavra: ")

string.lower()
result = {}
vogais = 'aeiou'
for i in vogais:
    if i in string:
        result[i] = string.count(i)

print(result)