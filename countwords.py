text_input = raw_input("Nhap vao doan van can dem so tu: ")
dic = {}
arr_text = text_input.split()
for x in arr_text:
	if dic.has_key(x):
		dic[x] += 1
	else:
		dic[x] = 1
print dic
	