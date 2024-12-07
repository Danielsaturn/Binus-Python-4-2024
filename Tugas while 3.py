tampungnilai = 0
tampunginput = 0

while (True):
    inputan = input("Masukan Nilai: ")
    if (inputan == ""):
        
        hasil = tampungnilai / tampunginput
        break
    
    else:
        if (inputan == "A"):
            
            tampungnilai = tampungnilai + 4.00
            tampunginput += 1
            
        elif (inputan == "A-"):
            
            tampungnilai = tampungnilai + 3.75
            tampunginput += 1
            
        elif (inputan == "B+"):
            
            tampungnilai = tampungnilai + 3.50
            tampunginput += 1
            
        elif (inputan == "B"):
            
            tampungnilai = tampungnilai + 3.00
            tampunginput += 1
            
        elif (inputan == "B-"):
            
            tampungnilai = tampungnilai + 2.75
            tampunginput += 1
            
        elif (inputan == "B-"):
            
            tampungnilai = tampungnilai + 2.75
            tampunginput += 1
            
        elif (inputan == "C+"):
            
            tampungnilai = tampungnilai + 2.50
            tampunginput += 1
            
        elif (inputan == "C"):
            
            tampungnilai = tampungnilai + 2.00
            tampunginput += 1
            
        elif (inputan == "C-"):
            
            tampungnilai = tampungnilai + 1.75
            tampunginput += 1
            
        elif (inputan == "D"):
            
            tampungnilai = tampungnilai + 1.50
            tampunginput += 1
            
        elif (inputan == "E"):
            
            tampungnilai = tampungnilai + 1.20
            tampunginput += 1
            
        else:
            
            print("please input the correct grade letter")
