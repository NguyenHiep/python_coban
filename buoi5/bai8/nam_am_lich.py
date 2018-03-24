# Viết chương trình tính năm âm lịch từ năm dương lịch
'''
Can là lấy năm chia lấy dư cho 10  
Chi là lấy năm chia lấy dư cho 12 
'''

def tinh_can(nam):
    lst_can = ['Canh','Tân', 'Nhâm', 'Quý', 'Giáp', 'Ất', 'Bính', 'Đinh', 'Mậu', 'Kỷ']
    key = nam % 10
    return lst_can[key]
    
def tinh_chi(nam):
    lst_chi = ['Thân','Dậu', 'Tuất', 'Hợi', 'Tý', 'Sửu', 'Dần', 'Mão', 'Thìn', 'Tỵ', 'Ngọ', 'Mùi']
    key = nam % 12
    return lst_chi[key]

if __name__ == '__main__':
    nam = eval(input('Nhập năm: \n'))
    print('Năm',nam,' âm lịch là năm', tinh_can(nam), '', tinh_chi(nam))