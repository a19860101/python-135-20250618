day = 2

match day:
    case 0:
        print('星期日')
    case 1:
        print('星期一')
    case 2:
        print('星期二')
    case 3:
        print('星期三')
    case 4:
        print('星期四')
    case 5:
        print('星期五')
    case 6:
        print('星期六')
    case _:
        print('系統錯誤')

errorCode = 0

match errorCode:
    case 0:
        print('成功')
    case 1:
        print('資料型態錯誤')

match day:
    case 1|2|3|4|5 :
        print('上班')
    case 6|0:
        print('還是要上班')
    case _:
        print('系統錯誤')