text = raw_input("Nhap vao string: ")
arr_text = list(text)  #giong split in javascript
print arr_text
arr_resever = []
for i in reversed(arr_text):
	arr_resever.append(i)
print arr_resever
text_resever = "".join(arr_resever)
print text_resever