from tkinter import *
from pygame import mixer

#! Variables
timerPomodoro = 25  # tempo do pomodoro
remainingTime = timerPomodoro * 60
timeBreak = 5 * 60  # tempo do intervalo
countBreak = 0  # Contagem de intervalos

#! Functions


# ! window
root = Tk()
root.title("Mxrqzz - Pomodoro")
root.geometry("450x400")  # Width x heigth
root.config(bg="#221D1F")

# ! window content
# ? Pomodoro Status
status = Label(root, text="", font=("Oswald bold", 20), bg="#221D1F")
status.pack()

# ? Timer
lblTimer = Label(
    root, text="25:00", font=("Oswald bold", 60), fg="#D91E1E", bg="#221D1F"
)

lblTimer.pack()

# * Buttons
btn_start = Button(
    root, text="Começar", font=("Oswald bold", 15), bg="#197340", fg="#221D1F"
)
btn_start.pack()

# ! Starting the window
root.mainloop()
