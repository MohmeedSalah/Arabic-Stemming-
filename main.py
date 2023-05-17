import nltk
import pyarabic.araby as araby
import pyarabic.number as number
nltk.download("stopwords")
from nltk import word_tokenize
from nltk.corpus import stopwords
from tkinter import *
import re
root = Tk()
root.geometry("800x500")
root.title("steamer")
img = PhotoImage(file="img.png")
canvas = Canvas (root,width=800,height=500)
canvas.pack(fill="both",expand=True)
canvas.create_image(0,0,image = img,anchor= "nw");
# back = Label(root,image=img)
arabieeee=[ 'ا' , 'أ' , 'ب' , 'ت' , 'ث' , 'ج' , 'ح' , 'خ' , 'د' , 'ذ' , 'ر' , 'ز' , 'س' , 'ش' , 'ص' ,  'ض', 'ط' , 'ظ' , 'ع' , 'غ' , 'ف' , 'ق' , 'ك' , 'ل' , 'م' , 'ن' , 'ه' , 'و' , 'ي' , 'ة' , 'ؤ' ,'ئ']

prefixes = ['وكال', 'وبال', 'فبال', 'وال', 'فال', 'كال', 'بال', 'ولل', 'فلل', 'ال', 'لل', 'لي', 'لت', 'لن', 'لا', 'فل',
            'فس', 'في', 'فت', 'فن', 'فا', 'سي', 'ست', 'سن', 'سا', 'ول', 'وس', 'وي', 'وت', 'ون', 'وا', 'ل', 'ب', 'ف',
            'س', 'و', 'ي', 'ت', 'ن', 'ا']
suffixes = [  'وهم', 'وك','هم', 'ها', 'كم', 'هن', 'هما', 'ون', 'ما', 'تم', 'ني', 'وا', 'كن', 'يا', 'نا', 'ين', 'ات', 'ان', 'ة', 'و',
            'ك', 'ه', 'ي', 'ن']
# reversed(suffixes)

def steaming_arabic():
    cnt=0
    List_steam.delete(0,List_steam.size())
    words = 'الأيمان وأثرة علي الصحة النفسية كان علم النفس دائما فخور  كعلم بالجامعات بتقاليده الدنيوية ( غير الدينية ) الملتزمة بالتنوير . وكان -علي الدوام- من ضمن هذه التقاليد وجود شك واضح بكل اشكال التدين ,كما يصف بيرنارد غرور .'
    words = txt_steam.get("1.0","end")
    words = araby.strip_tashkeel(words)
    for i in range(0,len(words)):
        check1 = 0
        for j in range(0,len(arabieeee)):
            # print(words[i]  + "        " + arabieeee[j])
            if words[i] == arabieeee[j]:
                check1 = 1

        if check1 == 0:
            words = words.replace(words[i], ' ')
    m = word_tokenize(words);
    stopwordsssss = set(stopwords.words("arabic"));
    filterd = [word for word in m  if word.casefold() not in stopwordsssss]
    # filterd2 = [word for word in filterd if word.casefold() not in arabieeee]
    for a in filterd:
        check = 1;
        for pref in prefixes:
            count = 0
            if len(a) > 2:
                for index in pref:
                    if a[count] != pref[count]:

                        break;
                    count += 1
                if count == len(pref):
                    a = a[len(pref):len(a)]
                    break;
            else :
                check=0;
        for suff in suffixes:
            count2 = 0
            if len(a) > 2:
                for index in suff:
                    #            print(index + " : " + a[len(a)-count2-1])
                    if count2 > len(a) or a[len(a) - count2 - 1] != suff[len(suff) - count2 - 1]:
                        break;
                    count2 += 1
                if count2 == len(suff):
                    a = a[0:len(a) - len(suff)]
                    break;
        cnt+=1
        if check:
            List_steam.insert(cnt,a);
            print(a)

             
Text1 = Label(root,text="Steamer Arabic")
Text1.pack()
Text1.place(x=350,y=10)
btn_steam = Button(root,command=steaming_arabic,text="steaming",width=10,height=2)
txt_steam = Text(root,width=50,height=2)
List_steam = Listbox(root)
btn_steam.pack()
btn_steam.place(x=350,y=50);
txt_steam.pack(pady=3)
txt_steam.place(x=200,y=100)
List_steam.pack(pady=4)
List_steam.place(x=330,y=140)
root.mainloop()