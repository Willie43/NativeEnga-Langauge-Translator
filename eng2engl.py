""" Translate in Enga """
#Dictionary (key value pair) enga word to english and pidgn
Eng2Eng={"come":"ipe", "eat":"nah","sleep":"pali"}
Pidgn2Eng={"kam":"ipe", "kaika2":"nah","slip":"pali"}

#menu
trans2=int(input("Menu\n(1)Enga to English\n(2)Enga to Pidgn\n>"))
#english_2_Enga
if trans2==1:
    eng2eng=input("Enter English Word\n>").lower()
    if eng2eng in Eng2Eng:
        print("Enga word for English word " + eng2eng + " is " + Eng2Eng[eng2eng])
    else:
        print ("No Enga word found for " + eng2eng)
#pidgn_2_enga
if trans2==2:
    eng2pidgn=input("Enter Pidgn Word\n>").lower()
    if eng2pidgn in Pidgn2Eng:
        print("Enga Word for Pidgn word " + eng2pidgn + " is " + Pidgn2Eng[eng2pidgn])
    else:
        print ("No Enga word found for  " + eng2pidgn)
#invaild_choice
if trans2<1 or trans2>2:
    print ("Incorrect Choice")
    
