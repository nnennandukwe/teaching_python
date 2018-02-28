def hello(random_word,funny_word,mean_word):
    return random_word, funny_word, mean_word

a = hello("school","hahaha","ugly")
b = hello("happy","silly","whatever")
print(a)
print(b)

def goodbye(name):
	return "goodbye " + name

def add(first,second):
	total = first / second
	return "first number divided by second number: " + str(total)

print(add(4,5))

print(goodbye("Ashley"))
print(goodbye("Katie"))