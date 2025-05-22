def taotupletulist(lst):
    return tuple(lst)

input_list = input("nhap danh sach cac so, cach nhau bang dau phay: ")

numbers = list(map(int, input_list.split(',')))

my_tuple = taotupletulist(numbers)
print("list: ", numbers)
print("tuple tu list: ", my_tuple)

