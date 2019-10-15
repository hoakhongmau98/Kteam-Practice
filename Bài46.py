a= [1,2,3,4,5,6,7,8,9,10]
#khi thực hiện gọi filter hay map, cần định nghĩa kiểu gái trị cho nó
#Vì khi call nó ra khi chưa định nghĩa sẽ trả ra là call object
print(list(map(lambda x: x**2,a)))