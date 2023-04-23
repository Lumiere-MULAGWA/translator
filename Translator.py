from translate import Translator
from tkinter import *
#from PIL import Image, ImageTk
from tkinter import ttk
class ScrolledText(Frame):
    def __init__(self, boss):
        Frame.__init__(self)
        self.traduc =Text(self, width=50, height=10, cursor='xterm')
        scroll =Scrollbar(self, bd=1, command=self.traduc.yview)
        self.traduc.configure(yscrollcommand =scroll.set)
        self.traduc.pack(side =LEFT, expand=YES, fill=BOTH, padx=2, pady=2)
        scroll.pack(side =RIGHT, expand=NO, fill=Y, padx=2, pady=2)
print("*** Historique **")
def traduire():
    error.configure(text="")
    a = combo.get()
    if a == "Anglais-Français":
        print("Vous avez choisi Anglais-Français")
        if a != "":
            a = st.traduc.get("0.0", END)
            print(a)
            trad = Translator(from_lang="en", to_lang="fr")
            traduction.configure(text=trad.translate(a))
            print(trad.translate(a))
        else:
            error.configure(text="Vous n'avez rien entré")
    elif a == "Français-Anglais":
        print("Vous avez choisi " + a)
        if a != "":
            a = st.traduc.get("0.0", END)
            print(a)
            trad = Translator(from_lang="fr", to_lang="en")
            traduction.configure(text=trad.translate(a))
            print(trad.translate(a))
        else:
            error.configure(text="Vous n'avez rien entré")
    elif a == "Allemand-Français":
        print("Vous avez choisi " + a)
        if a != "":
            a = st.traduc.get("0.0", END)
            print(a)
            trad = Translator(from_lang="de", to_lang="fr")
            traduction.configure(text=trad.translate(a))
            print(trad.translate(a))
        else:
            error.configure(text="Vous n'avez rien entré")
    elif a == "Français-Allemand":
        print("Vous avez choisi " + a)
        if a != "":
            a = st.traduc.get("0.0", END)
            print(a)
            trad = Translator(from_lang="fr", to_lang="de")
            traduction.configure(text=trad.translate(a))
            print(trad.translate(a))
        else:
            error.configure(text="Vous n'avez rien entré")
    else:
        error.configure(text="Ce que vous avez entré n'est pas proposé !")
        print("Ce que vous avez entré n'est pas proposé !!")


width=200
height=150

t = Tk()
t.title("*** Espace esis translator***")
#t.iconbitmap("Trad.ico")
t.geometry("1080x720")

#Widgets 
Button(t, text="Traduire", height=2, width=10, bg="blue", fg="red", command=traduire).place(x=900, y=150)
Button(t, text="Quitter", height=2, width=10, bg='red', fg="blue", command=t.destroy).place(x=985, y=150)
choix = StringVar()
combo = ttk.Combobox(t, values=["Anglais-Français", "Français-Anglais", "Allemand-Français", "Français-Allemand"], cursor="dotbox")
combo.place(x=450, y=100)
combo.current(1)


traduction = Label(t)
traduction.place(x=350, y=350)


error = Label(t, fg="red", font=('Helvetica', 25))
error.place(x=500, y=600)

develop = Label(t, text="Developed by lmr lumiere", font=("Helvetica", 20), fg="blue")
develop.place(x=350, y=25)

st =ScrolledText(t)
st.place(x=350, y=150)

#image = Image.open("Tradu.gif")
#photo = ImageTk.PhotoImage(image)
#label = Label(image=photo)
#label.place(x=0, y=0)

t.mainloop()
