text_input = raw_input("Nhap vao doan van: ")
vowels = {"a" : 0, "o": 0, "i": 0, "u": 0, "e": 0}
for i in list(text_input):
	if vowels.has_key(i):
		vowels[i] += 1
print vowels
