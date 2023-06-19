import tkinter
reps = 1
timer = None

def reset():
    global reps
    global timer
    global timer_text
    window.after_cancel(timer)
    reps = 1
    tomato_canvas.itemconfig(timer_text, text = '25:00')
    title['text'] = 'Pomodoro Timer'
    title['fg'] = '#9bdeac'
    checkmark_area['text'] = ''

def start_timer():
    global reps
    if reps % 8 == 0:
        title['text'] = 'Long Break Timer'
        title['fg'] = "#e2979c"
        checkmark_area['text'] += '✓'
        reps += 1
        countdown(1200)
    elif reps % 2 == 0:
        title['text'] = 'Short Break Timer'
        title['fg'] = "#e7305b"
        checkmark_area['text'] += '✓'
        reps += 1
        countdown(300)
    else:
        title['text'] = 'Work Timer'
        title['fg'] = "#9bdeac"
        reps += 1
        countdown(1500)

def countdown(total_seconds):
    timer_minutes = total_seconds // 60
    timer_seconds = total_seconds % 60
    tomato_canvas.itemconfig(timer_text, text = f'{timer_minutes}:{0 if timer_seconds < 10 else ""}{timer_seconds}')
    if total_seconds > 0:
        global timer
        timer = window.after(1, countdown, total_seconds - 1)
    else:
        start_timer()

window = tkinter.Tk()
window.title('Work-break timer')
window.config(padx = 50, pady = 50, bg = '#f7f5dd')

title = tkinter.Label(text='Pomodoro Timer', fg = '#9bdeac', bg = '#f7f5dd', font = ('Courier', 49, 'bold'), width = 20)
title.grid(row = 1, column = 2)

tomato_image = tkinter.PhotoImage(file = 'tomato.png')
tomato_canvas = tkinter.Canvas(width = 202, height = 224, bg = '#f7f5dd', highlightthickness=0)
tomato_canvas.create_image(100, 112, image = tomato_image)
timer_text = tomato_canvas.create_text(100, 130, text='25:00', fill='#ffffff', font=('Courier', 35, 'bold'))
tomato_canvas.grid(row=2, column = 2)

start_button = tkinter.Button(text = 'Start', highlightbackground = '#f7f5dd', command = start_timer)
start_button.grid(row = 3, column = 1)

reset_button = tkinter.Button(text = 'Reset', highlightbackground = '#f7f5dd', command = reset)
reset_button.grid(row = 3, column = 3)

checkmark_area = tkinter.Label(bg = '#f7f5dd', text = '', font=('Courier', 35, 'bold'), fg = '#9bdeac')
checkmark_area.grid(row = 4, column = 2)

window.mainloop()