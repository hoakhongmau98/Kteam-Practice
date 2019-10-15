file_object = open('H:\Python_Kteam\Kteam_practice\Bài12.txt.txt', mode = 'r', encoding = 'Utf-8')
lst_line = file_object.read()
new_lst = lst_line.split('\n')
for i in range(len(new_lst)):
	print(new_lst[i].upper())
