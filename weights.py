wts_total=0
counter=0
wts=[55,109,64,20,88,77,15,90]
for num in wts:
    wts_total=wts_total+num
   
    
    
    if wts_total>350:
        
            print(counter)
   
            print("stop")
            break
    else:
        print(wts_total)
        counter=counter+1
