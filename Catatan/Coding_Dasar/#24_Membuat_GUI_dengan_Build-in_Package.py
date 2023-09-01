import tkinter

main = tkinter.Tk()

def event():
    label1 = tkinter.Label(main, text = "Aku ditekan ^^")
    label1.pack()
    
label = tkinter.Label(main, text = "Halo, saya adalah\n GUI sederhana dengan \nmenggunakan python")
tombol = tkinter.Button(main, text = "Tekan aku", command = event)

label.pack()
tombol.pack()
main.mainloop()