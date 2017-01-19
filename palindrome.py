text = raw_input("Nhap vao string: ")
arr_text = list(text)  #giong split in javascript
arr_resever = []
for i in reversed(arr_text):
	arr_resever.append(i)
text_resever = "".join(arr_resever)
if text_resever == text:
	print("palindrome!")
else:
	print("not a palindrome!")
