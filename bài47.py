a  = [1,2,3,4,5,6,7,8,9,10]
#hàm filter ra phần tử chẵn được chọn làm generator cho map.
#Lồng filter trước và lấy kết quả filter truyền vào hàm xử lý map
print(list(map(lambda y: y**2,(filter(lambda x: not x%2,a)))))