#Program do sprawdzania pogody na podstawie wpisanego miasta lub państwa

from tkinter import *
from Weather import *



window = Tk()
window.geometry('400x200')
window.title("Pogoda")
window.resizable(False, False)

lbl = Label(window, text="Pogoda w (miasto/państwo):")
lbl.grid(column=0, row=0)

txt_city = Entry(window,width=10)
txt_city.grid(column=1, row=0)
txt_city.focus()

#W lbl_data będą wyświetlane dane nt wyszukiwaniej pogody/miasta
lbl_data = Label(window, relief="solid")
lbl_data.place(relx=0.5, rely=0.25, relwidth=0.7, relheight=0.6, anchor=N)
#lbl_data.grid(column=0, row=1)

def showWeather():
    try:
        data_weather = checkWeather(city=txt_city.get())
        lbl_data.configure(text=txt_city.get()+"\n"+
        "Dł. geograficzna: " + str(data_weather[0]) + "\n"+
        "Szer. geograficzna:" + str(data_weather[1]) + "\n"+
        "ID Kraju: " + str(data_weather[2]) + "\n"+
        "Temperatura: " + str(data_weather[3]) + "st. C")
    except:
        lbl_data.configure(text="Błąd. Możliwe przyczyny:\n *Błędna nazwa miasta \n *Brak połączenia z internetem \n *Klucz API wygasł")

btn = Button(window, text="Sprawdź pogodę", command=showWeather)
btn.grid(column=2, row=0)

window.mainloop()