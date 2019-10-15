#a = input('input vào chuỗi xử lý')
a = 'hello world and practice makes perfect and hello world again '
str_a = a.split(' ')
#gộp 3 phương thức
#set || loại bỏ các phần tử lặp trong lst, tính chất cơ bản của set
#list || biến đổi lại từ set sang list vì set là không thể thao tác
#sorted(list) || sắp xếp chuỗi, khác cách dùng với list.sort()
print(' '.join(sorted(list(set(str_a)))))
