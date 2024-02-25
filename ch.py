with open("lst.excel", 'a+') as file:
	file.seek(0)
	file.read()
	for line in file:
		file.write(line.replace("li", " "))

# import re
# def replacetext(search_text,replace_text):
# 	with open("lst.excel",'a+') as f:
# 		file = f.read()
# 		file = re.sub(search_text, replace_text, file)
# 		f.seek(0)
# 		f.write(file)
# 	return "Text replaced"

# search_text = "li"
# replace_text = ""
# print(replacetext(search_text,replace_text))
