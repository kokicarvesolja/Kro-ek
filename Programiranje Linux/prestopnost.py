uporab_leto = int(input("Vnesi letnico:"))

if uporab_leto%4 == 0 and (uporab_leto%100 != 0 or uporab_leto%400 == 0):
    print("Februar ima 29 dni.")
else: 
    print ("Februar ima 28 dni. ")

if uporab_leto%4 == 0: 
    if uporab_leto%100 == 0 and uporab_leto%400 != 0: 
        print ("Februar ima 28 dni. ")
    else:
        print("Februar ima 29 dni.")
else: 
    print("Februar ima 29 dni.")

   
    