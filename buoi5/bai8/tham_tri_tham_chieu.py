# Tham trị và tham chiếu trong python
# 1. Tham trị

def tinh_binh_phuong(so):
    # Tinh binh phuong cua mot so
    so = so * so
    print('So in function = ', so)
    return
# 2. Tham chiếu

def  change_list(lst):
    # Thêm vào sau list
    lst.append(10)
    lst.append(20)
    print('List in function: ', lst)
    return


if __name__ == '__main__':
    # Tham trị
    so = 8
    tinh_binh_phuong(so)
    print('So out function = ', so)

    # Tham chiếu

    lst = [ 1, 2, 3, 4]
    print('List:', lst)
    change_list(lst)
    