def tinhtongsochan(lst):
    tong = 0
    for num in lst:
        if num % 2 == 0:
            tong += num
    return tong

input_list = input("nhap danh sach cac so, cach nhau bang dau phay: ")
numbers = list(map(int, input_list.split(',')))
tongchan = tinhtongsochan(numbers)
print("tong cac so chan trong list la: ", tongchan)
