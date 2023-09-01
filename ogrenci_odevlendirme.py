import tkinter as tk
import tkcalendar as tc
from tkinter import messagebox

def goster():
    secim = list.get(tk.ACTIVE)
    E1.delete("0", tk.END)  
    E2.delete("0",tk.END)
    E3.delete("0",tk.END)
    E4.delete("0",tk.END)
    E5.delete("0",tk.END)

    if secim == "Ayşe Kaya":
        E1.insert("0","Ayşe")
        E2.insert("0","Kaya")
        E3.insert("0","10C")
        E4.insert("0","1546")
        E5.insert("0","MF")
    elif secim == "Nilay Ünlü":
        E1.insert("0","Nilay")
        E2.insert("0","Ünlü")
        E3.insert("0","10D")
        E4.insert("0","1547")
        E5.insert("0","TM")
    elif secim == "Mehmet Boz":
        E1.insert("0","Mehmet")
        E2.insert("0","Boz")
        E3.insert("0","10A")
        E4.insert("0","1543")
        E5.insert("0","MF")
    elif secim == "Can Acar":
        E1.insert("0","Can")
        E2.insert("0","Acar")
        E3.insert("0","11B")
        E4.insert("0","1541")
        E5.insert("0","TS")
    elif secim == "Ertuğrul Turgut":
        E1.insert("0","Ertuğrul")
        E2.insert("0","Turgut")
        E3.insert("0","12A")
        E4.insert("0","1540")
        E5.insert("0","TS")
    elif secim == "Tuana gül":
        E1.insert("0","Tuana")
        E2.insert("0","Gül")
        E3.insert("0","11C")
        E4.insert("0","1549")
        E5.insert("0","TM")
    

def sil():
    E1.delete(0,tk.END)
    E2.delete(0,tk.END)
    E3.delete(0,tk.END)
    E4.delete(0,tk.END)
    E5.delete(0,tk.END)
    E6.delete(0,tk.END)
    E7.delete("1.0",tk.END)

    
def odev():
    with open("odevler.txt","w",encoding="utf-8") as file:
        file.write(
            "adı: {}\nsoyadı: {}\nnumarası: {}\nnumarası: {}\nbölümü: {}\n Yukarıda bilgileri verilen öğrenciye {} dersinden {} konulu ödev verilmiştir.\nÖdevin veriliş tarihi: {}\n Teslim tarihi: {}\nÖdevden alınan not: {}".format(
              E1.get(),E2.get(),E3.get(),E4.get(),E5.get(), menu_opsiyon.get(),E6.get(),takvim.get_date(),takvim2.get_date(),E7.get("1.0",tk.END)
            
               )
        )
        
    messagebox.showinfo("Başarılı","Bilgiler dosyaya başarıyla kaydedildi")
    

pencere = tk.Tk()
pencere.geometry("800x600")
pencere.tk_setPalette("#efefef")
baslik = pencere.title("Ödev Sistemi")

frame1 = tk.Frame(pencere,bg="#ffffaa")
frame1.place(relx=0.1,rely=0.1,relheight=0.5,relwidth=0.2)

frame2 = tk.Frame(pencere,bg="#ffffaa")
frame2.place(relx=0.31,rely=0.1,relheight=0.5,relwidth=0.3)

frame3 = tk.Frame(pencere,bg="#ffffaa")
frame3.place(relx=0.62,rely=0.1,relheight=0.5,relwidth=0.3)

frame4 = tk.Frame(pencere,bg="#ffffaa")
frame4.place(relx=0.1,rely=0.62,relheight=0.15,relwidth=0.83)



etiket1 = tk.Label(frame1,text="öğrenciler",font="Verdana 10 bold",bg="#ffffaa")
etiket1.pack(padx=10,pady=10)


ad = ["Ayşe Kaya","Nilay Ünlü", "Mehmet Boz","Can Acar","Ertuğrul Turgut","Tuana gül"]

list = tk.Listbox(frame1,bg="white")
list.place(relx=0.11,rely=0.1,relheight=0.4,relwidth=0.7)


L1 = tk.Label(frame2,text="Ad:",font="Verdana 10 bold",bg="#ffffaa")
L1.place(relx=0.1,rely=0.1)

L2 = tk.Label(frame2,text="Soyad:",font="Verdana 10 bold",bg="#ffffaa")
L2.place(relx=0.1,rely=0.2)

L3 = tk.Label(frame2,text="Sınıf:",font="Verdana 10 bold",bg="#ffffaa")
L3.place(relx=0.1,rely=0.3)

L4 = tk.Label(frame2,text="Numara:",font="Verdana 10 bold",bg="#ffffaa")
L4.place(relx=0.1,rely=0.4)

L5 = tk.Label(frame2,text="Alan:",font="Verdana 10 bold",bg="#ffffaa")
L5.place(relx=0.1,rely=0.5)

E1 = tk.Entry(frame2,bg="white")
E1.place(relx=0.38,rely=0.1,relheight=0.06,relwidth=0.5)

E2 = tk.Entry(frame2,bg="white")
E2.place(relx=0.38,rely=0.2,relheight=0.06,relwidth=0.5)

E3 = tk.Entry(frame2,bg="white")
E3.place(relx=0.38,rely=0.3,relheight=0.06,relwidth=0.5)

E4 = tk.Entry(frame2,bg="white")
E4.place(relx=0.38,rely=0.4,relheight=0.06,relwidth=0.5)

E5 = tk.Entry(frame2,bg="white")
E5.place(relx=0.38,rely=0.5,relheight=0.06,relwidth=0.5)

L6 = tk.Label(frame3,text="Ders:",font="Verdana 10 bold",bg="#ffffaa")
L6.place(relx=0.05,rely=0.1)

L7 = tk.Label(frame3,text="Konu:",font="Verdana 10 bold",bg="#ffffaa")
L7.place(relx=0.05,rely=0.2)

L8 = tk.Label(frame3,text="Veriliş Tarihi:",font="Verdana 10 bold",bg="#ffffaa")
L8.place(relx=0.05,rely=0.33)

L9 = tk.Label(frame3,text="Teslim Tarihi:",font="Verdana 10 bold",bg="#ffffaa")
L9.place(relx=0.05,rely=0.42)

L10 = tk.Label(frame3,text="Not:",font="Verdana 10 bold",bg="#ffffaa")
L10.place(relx=0.05,rely=0.5)

menu_opsiyon = tk.StringVar(frame3)
menu_opsiyon.set("\t")

menu = tk.OptionMenu(frame3,menu_opsiyon,"Matematik","Fizik","Felsefe","Edebiyat")
menu.config(bg="#e5e5e5")
menu.place(relx=0.38,rely=0.1,relheight=0.08,relwidth=0.5)

E6 = tk.Entry(frame3,bg="white")
E6.place(relx=0.38,rely=0.2,relheight=0.1,relwidth=0.5)

takvim = tc.DateEntry(frame3,width=12,background="orange",foreground="black",borderwidth=1,locale="de_DE")
takvim._top_cal.overrideredirect(False)
takvim.place(relx=0.47,rely=0.33,relheight=0.06,relwidth=0.5)

takvim2 = tc.DateEntry(frame3,width=12,background="orange",foreground="black",borderwidth=1,locale="de_DE")
takvim2._top_cal.overrideredirect(False)
takvim2.place(relx=0.47,rely=0.42,relheight=0.06,relwidth=0.5)

E7 = tk.Text(frame3,bg="white")
E7.place(relx=0.25,rely=0.5,relheight=0.08,relwidth=0.2)

for i in ad:
    list.insert(tk.END,i)


goster_dugme = tk.Button(frame1, text="Göster", command=goster,bg="#e5e5e5")
goster_dugme.place(relx=0.3, rely=0.6)
      
temizle = tk.Button(frame4,text="Temizle",bg="#ffff00",command=sil)
temizle.place(relx=0.28,rely=0.3,relheight=0.4,relwidth=0.1)

Kaydet = tk.Button(frame4,text="Kaydet",bg="#5fbf00",command=odev)
Kaydet.place(relx=0.4,rely=0.3,relheight=0.4,relwidth=0.1)

Kapat = tk.Button(frame4,text="Kapat",bg="#f74242",command=pencere.quit)
Kapat.place(relx=0.52,rely=0.3,relheight=0.4,relwidth=0.1)

pencere.mainloop()
