se = [
    [" ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " "]
]
#نمايش صفحه:
def print_safhe(safhe):
    for row in safhe:
        print(f'{6 * "+---"}+\n|', end='')
        for cell in row:
            print(f" {cell} |", end='')
        print()
    print(f'{6 * "+---"}+')

#چرخش صفحه:
def charkhesh(se, khane, samt):
    i = (khane // 3) * 3
    j = (khane % 2) * 3
        
    if(samt == "r"):
        se[0+i][0+j],se[0+i][2+j],se[2+i][0+j],se[2+i][2+j] = se[2+i][0+j],se[0+i][0+j],se[2+i][2+j],se[0+i][2+j]
        se[0+i][1+j],se[1+i][0+j],se[2+i][1+j],se[1+i][2+j] = se[1+i][0+j],se[2+i][1+j],se[1+i][2+j],se[0+i][1+j]

    elif(samt == "l"):
        se[0+i][0+j],se[0+i][2+j],se[2+i][0+j],se[2+i][2+j] = se[0+i][2+j],se[2+i][2+j],se[0+i][0+j],se[2+i][0+j]
        se[0+i][1+j],se[1+i][0+j],se[2+i][1+j],se[1+i][2+j] = se[1+i][2+j],se[0+i][1+j],se[1+i][0+j],se[2+i][1+j]

#کمکي چک کردن برد:  
def check_list(inp_list):
    karakter = inp_list[0]
    for x in inp_list[1:]:
        if(karakter != x or karakter == " "):
            return False
        
    return True

#چک کردن برد:
def check_barande(table):
    #افقي:
    for row in table:
        if(row[2] != " "):
            if(check_list(row[0:5])):
               return f"{row[0]} barande shod !! :)"
            elif(check_list(row[1:6])):
                return f"{row[1]} barande shod !! :)"
    #عمودي:       
    for c in range(6):
        column = [table[i][0+c] for i in range(6)]
        if(column[2] != " "):
            if(check_list(column[0:5])):
                return f"{column[0]} barande shod !! :)"
            elif(check_list(column[1:6])):
                return f"{column[1]} barande shod !! :)"
    #اريب \:
    for i in range(2):
        for j in range(2):
            if(check_list([table[x+i][x+j] for x in range(5)])):
                return f"{orib_chap_be_rast[0]} barande shod !! :)"
    #اريب /:
    for i in range(2):
        for j in range(2):            
            if(check_list([table[x+i][(4-x)+j] for x in range(5)])):
                return f"{orib_chap_be_rast[0]} barande shod !! :)"

    return "hickas barande nashod :("

#گذاشتن مهره:
def radif_and_sotoon(safhe, fard):
    print(f"nobat ({fard}) ast")            
    while(True):
        try:
            row = int(input("رديف مورد نظر را وارد کنيد:")) - 1
            if row >= 0 or row <= 5:
                break
            else:
                continue
        except:
            print("خطا! تلاش مجدد")
            continue
    while(True):
        try:
            column = int(input("ستون مورد نظر را وارد کنيد:")) - 1
            if column >= 0 or column <= 5:
                break
            else:
                continue
        except:
            print("خطا! تلاش مجدد")
            continue
        
    if(safhe[row][column] == " "):
        safhe[row][column] = fard
            
    else:
        print("خانه پر است")
        print("hanooz ", end = '')
        radif_and_sotoon(safhe, fard)

#مشخص کردن خانه براي چرخش:
def moshakhas_khane():
    print("بالا سمت راست:1\nبالا سمت چم:2\nپايين سمت راست:3\nپايين سمت چپ:4")
    while(True):
        try:
            khane = int(input("خانه مورد نظر براي چرخش را وارد کنيد:"))
            break
        except:
            continue
            
    while(True):
        if(khane <= 4 and khane >= 1):
            break
        else:
            try:
                khane = int(input("خانه مورد نظر براي چرخش را وارد کنيد:"))
                break
            except:
                continue
    return khane

#مشخص کردن سمت براي پرخش:
def moshakhas_samt():
    samt = input(" l or r:")
    while(True):
        if(samt == "r" or samt == "l"):
            break
        else:
            samt = input(" l or r:")
    return samt


def start_game_pentago():
    nobat = "o"
        
    while(True):
        print_safhe(se)
            
        radif_and_sotoon(se, nobat)
        print_safhe(se)
            
        khane = moshakhas_khane()
            
        samt = moshakhas_samt()
                
        charkhesh(se, khane, samt)
            
        barande = check_barande(se)
        if(barande[0] == "o" or barande[0] == "x"):
            print(barande)
            break
        
        if(nobat == "o"):
            nobat = "x"
        else:
            nobat = "o"