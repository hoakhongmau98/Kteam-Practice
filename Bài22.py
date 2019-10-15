from operator import itemgetter,attrgetter
j = [x for x in input('Nhập vào từng chuỗi: ').split(',')]
#(0,1,2) thứ tự ưu tiên sắp xếp
print(soted(j, key = itemgetter(0,1,2)))