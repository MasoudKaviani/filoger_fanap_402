import tkinter
import random

LOWER = 1
UPPER = 100


def guessnumber():
    global te
    print(te.get())
    user_guess_label.set('شما عدد ' + te.get() + ' را وارد کردید')


window = tkinter.Tk()
window.geometry('800x600')
window.title('بازی بزرگ حدس اعداد')

exit_btn = tkinter.Button(window, text="خروج")
exit_btn.place(x=200, y=400)

label = tkinter.Label(window, justify=tkinter.RIGHT, text="لطفا یک عدد بین ۱ تا ۱۰۰ حدس بزنید:")
label.place(x=200, y=50)

guess = tkinter.Button(window, text="حدس بزن", command=guessnumber)
guess.place(x=150, y=300)

user_guess = tkinter.StringVar()
te = tkinter.Entry(window, textvariable=user_guess)
te.place(x=150, y=150)

user_guess_label = tkinter.StringVar()
label_user_guess = tkinter.Label(window, textvariable=user_guess_label)
label_user_guess.place(x=150, y=200)

window.mainloop()
