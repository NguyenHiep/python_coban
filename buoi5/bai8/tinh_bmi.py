'''
Yêu cầu: Viết chương trình tính chỉ số BMI 
Cách tính BMI: 
-  BMI = Cân nặng / (Chiều cao * Chiều cao) 
-  Bảng đánh giá BMI:  
    +  Gầy: <18.5 
    +  Bình thường: 18.5 – 24.99 
    +  Thừa cân: >=25 

'''

def tinh_bmi(can_nang, chieu_cao):
    bmi = can_nang / (chieu_cao * chieu_cao)
    return bmi

def danh_gia_bmi(bmi):
    danh_gia = ''
    if bmi < 18.5:
        danh_gia = 'Gầy'
    elif bmi < 24.99:
        danh_gia = 'Bình thường'
    else:
        danh_gia = 'Thừa cân'
    return danh_gia

if __name__ == '__main__':
    weight = eval(input('Nhập cân nặng: '))
    height = eval(input('Nhập chiều cao: '))
    bmi    = tinh_bmi(weight, height)
    print('Chỉ số BMI của bạn: %.2f'%bmi)
    print('Kết quả: Bạn ', danh_gia_bmi(bmi))
            
