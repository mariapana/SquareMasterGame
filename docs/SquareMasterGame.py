import tkinter as tk
import time

##LEVEL 1##
solution = 3
def check():
  user_guess = int(input_box.get())
  if solution == user_guess:
    msg = "Correct!"
    lvl2 = tk.Button(root, text ="Congrats! Let's go to the next level", command = next)
    lvl2.pack()
  else:
    msg = "Try again!"
  lbl_result = tk.Label(root, text = msg)
  lbl_result.pack()

def next():
  root.destroy()
   
root = tk.Tk()

#Level
lvl_txt = tk.Label(root, text = "Level 1")
lvl_txt.pack()

#Question
q = tk.Label(root, text = "How many squares are there?")
q.pack()

#Card Image
photo = tk.PhotoImage(file = "s1.gif")
img = tk.Label(root, image = photo)
img.pack()

#Timer   
def start(t):
  lab.config(text = str(t))
  if(t > 0):
    root.after(1000, start, t-1)
  if t == 0:
    global window
    window = tk.Toplevel(root)
    tim = tk.Message (window, text = "Out of time")
    tim.pack()
    restr = tk.Button (window, text = "Restart", command = ret)
    restr.pack()
def ret():
  start(30)
  window.destroy()    
lab = tk.Label(root)
lab.pack(side = "left")
start(30)

#Hint
def create_window():
    window = tk.Toplevel(root)
    hint = tk.Message(window, text = "Mom, Dad and Kid")
    hint.pack()
hint_butt = tk.Button(root, text = "Hint", command = create_window)
hint_butt.pack(side = "right")

#Input
input_box = tk.Entry(root, bd=5)
input_box.pack()

#Button for Checking
button = tk.Button(root, text = "Check", command = check)
button.pack()

root.mainloop()

##LEVEL2##
toor = tk.Tk()
solution = 7

def check():
  user_guess = int(input_box.get())
  if solution == user_guess:
    msg = "Correct!"
    lvl2 = tk.Button(toor, text ="Congrats! Let's go to the next level", command = next)
    lvl2.pack()
  else:
    msg = "Try again!"
  lbl_result = tk.Label(toor, text = msg)
  lbl_result.pack()

def next():
  toor.destroy()
#Level
lvl_txt = tk.Label(toor, text = "Level 2")
lvl_txt.pack()

#Question
q = tk.Label(toor, text = "How many squares are there?")
q.pack()

#Card Image
card = tk.PhotoImage(file = "s2.gif")
c_lbl = tk.Label(toor, image = card)
c_lbl.pack()

#Timer   
def start(t):
  lab.config(text = str(t))
  if(t > 0):
    toor.after(1000, start, t-1)
  if t == 0:
    global window
    window = tk.Toplevel(toor)
    tim = tk.Message (window, text = "Out of time")
    tim.pack()
    restr = tk.Button (window, text = "Restart", command = ret)
    restr.pack()
def ret():
  start(30)
  window.destroy()    
lab = tk.Label(toor)
lab.pack(side = "left")
start(30)


#Hint
def create_window():
    window = tk.Toplevel(toor)
    hint = tk.Message(window, text = "Crossroads")
    hint.pack()
hint_butt = tk.Button(toor, text = "Hint", command = create_window)
hint_butt.pack(side = "right")

#Input
input_box = tk.Entry(toor, bd=5)
input_box.pack()

#Button for Checking
button = tk.Button(toor, text = "Check", command = check)
button.pack()

toor.mainloop()

##LEVEL 3##
solution = 14
def check():
  user_guess = int(input_box.get())
  if solution == user_guess:
    msg = "Correct!"
    lvl2 = tk.Button(r3, text ="Congrats! Let's go to the next level", command = next)
    lvl2.pack()
  else:
    msg = "Try again!"
  lbl_result = tk.Label(r3, text = msg)
  lbl_result.pack()

def next():
  r3.destroy()
   
r3 = tk.Tk()

#Level
lvl_txt = tk.Label(r3, text = "Level 3")
lvl_txt.pack()

#Question
q = tk.Label(r3, text = "How many squares are there?")
q.pack()

#Card Image
photo = tk.PhotoImage(file = "s3.gif")
img = tk.Label(r3, image = photo)
img.pack()

#Timer   
def start(t):
  lab.config(text = str(t))
  if(t > 0):
    r3.after(1000, start, t-1)
  if t == 0:
    global window
    window = tk.Toplevel(r3)
    tim = tk.Message (window, text = "Out of time")
    tim.pack()
    restr = tk.Button (window, text = "Restart", command = ret)
    restr.pack()
def ret():
  start(30)
  window.destroy()    
lab = tk.Label(r3)
lab.pack(side = "left")
start(30)

#Hint
def create_window():
    window = tk.Toplevel(r3)
    hint = tk.Message(window, text = "Those squares are quite big, aren't they?")
    hint.pack()
hint_butt = tk.Button(r3, text = "Hint", command = create_window)
hint_butt.pack(side = "right")

#Input
input_box = tk.Entry(r3, bd=5)
input_box.pack()

#Button for Checking
button = tk.Button(r3, text = "Check", command = check)
button.pack()

r3.mainloop()

##LEVEL 4##
r4 = tk.Tk()
solution = 4

def check():
  user_guess = int(input_box.get())
  if solution == user_guess:
    msg = "Correct!"
    lvl2 = tk.Button(r4, text ="Congrats! Let's go to the next level", command = next)
    lvl2.pack()
  else:
    msg = "Try again!"
  lbl_result = tk.Label(r4, text = msg)
  lbl_result.pack()

def next():
  r4.destroy()
#Level
lvl_txt = tk.Label(r4, text = "Level 4")
lvl_txt.pack()

#Question
q = tk.Label(r4, text = "How many squares are there?")
q.pack()

#Card Image
card = tk.PhotoImage(file = "s4.gif")
c_lbl = tk.Label(r4, image = card)
c_lbl.pack()

#Timer   
def start(t):
  lab.config(text = str(t))
  if(t > 0):
    r4.after(1000, start, t-1)
  if t == 0:
    global window
    window = tk.Toplevel(r4)
    tim = tk.Message (window, text = "Out of time")
    tim.pack()
    restr = tk.Button (window, text = "Restart", command = ret)
    restr.pack()
def ret():
  start(30)
  window.destroy()    
lab = tk.Label(r4)
lab.pack(side = "left")
start(30)


#Hint
def create_window():
    window = tk.Toplevel(r4)
    hint = tk.Message(window, text = "Level 4...")
    hint.pack()
hint_butt = tk.Button(r4, text = "Hint", command = create_window)
hint_butt.pack(side = "right")

#Input
input_box = tk.Entry(r4, bd=5)
input_box.pack()

#Button for Checking
button = tk.Button(r4, text = "Check", command = check)
button.pack()

r4.mainloop()

##LEVEL 5##
solution = 14
def check():
  user_guess = int(input_box.get())
  if solution == user_guess:
    msg = "Correct!"
    lvl2 = tk.Button(r5, text ="Congrats! Let's go to the next level", command = next)
    lvl2.pack()
  else:
    msg = "Try again!"
  lbl_result = tk.Label(r5, text = msg)
  lbl_result.pack()

def next():
  r5.destroy()
   
r5 = tk.Tk()

#Level
lvl_txt = tk.Label(r5, text = "Level 5")
lvl_txt.pack()

#Question
q = tk.Label(r5, text = "How many squares are there?")
q.pack()

#Card Image
photo = tk.PhotoImage(file = "s5.gif")
img = tk.Label(r5, image = photo)
img.pack()

#Timer   
def start(t):
  lab.config(text = str(t))
  if(t > 0):
    r5.after(1000, start, t-1)
  if t == 0:
    global window
    window = tk.Toplevel(r5)
    tim = tk.Message (window, text = "Out of time")
    tim.pack()
    restr = tk.Button (window, text = "Restart", command = ret)
    restr.pack()
def ret():
  start(30)
  window.destroy()    
lab = tk.Label(r5)
lab.pack(side = "left")
start(30)

#Hint
def create_window():
    window = tk.Toplevel(r5)
    hint = tk.Message(window, text = "Teamwork makes the dream work")
    hint.pack()
hint_butt = tk.Button(r5, text = "Hint", command = create_window)
hint_butt.pack(side = "right")

#Input
input_box = tk.Entry(r5, bd=5)
input_box.pack()

#Button for Checking
button = tk.Button(r5, text = "Check", command = check)
button.pack()

r5.mainloop()

##LEVEL 6##
r6 = tk.Tk()
solution = 4

def check():
  user_guess = int(input_box.get())
  if solution == user_guess:
    msg = "Correct!"
    lvl2 = tk.Button(r6, text ="Congrats! Let's go to the next level", command = next)
    lvl2.pack()
  else:
    msg = "Try again!"
  lbl_result = tk.Label(r6, text = msg)
  lbl_result.pack()

def next():
  r6.destroy()
#Level
lvl_txt = tk.Label(r6, text = "Level 6")
lvl_txt.pack()

#Question
q = tk.Label(r6, text = "How many squares are there?")
q.pack()

#Card Image
card = tk.PhotoImage(file = "s6.gif")
c_lbl = tk.Label(r6, image = card)
c_lbl.pack()

#Timer   
def start(t):
  lab.config(text = str(t))
  if(t > 0):
    r6.after(1000, start, t-1)
  if t == 0:
    global window
    window = tk.Toplevel(r6)
    tim = tk.Message (window, text = "Out of time")
    tim.pack()
    restr = tk.Button (window, text = "Restart", command = ret)
    restr.pack()
def ret():
  start(30)
  window.destroy()    
lab = tk.Label(r6)
lab.pack(side = "left")
start(30)


#Hint
def create_window():
    window = tk.Toplevel(r6)
    hint = tk.Message(window, text = "Grouped Triangles... Hmmm... Interesting")
    hint.pack()
hint_butt = tk.Button(r6, text = "Hint", command = create_window)
hint_butt.pack(side = "right")

#Input
input_box = tk.Entry(r6, bd=5)
input_box.pack()

#Button for Checking
button = tk.Button(r6, text = "Check", command = check)
button.pack()

r6.mainloop()

##LEVEL 7##
solution = 18
def check():
  user_guess = int(input_box.get())
  if solution == user_guess:
    msg = "Correct!"
    lvl2 = tk.Button(r7, text ="Congrats! Let's go to the next level", command = next)
    lvl2.pack()
  else:
    msg = "Try again!"
  lbl_result = tk.Label(r7, text = msg)
  lbl_result.pack()

def next():
  r7.destroy()
   
r7 = tk.Tk()

#Level
lvl_txt = tk.Label(r7, text = "Level 7")
lvl_txt.pack()

#Question
q = tk.Label(r7, text = "How many squares are there?")
q.pack()

#Card Image
photo = tk.PhotoImage(file = "s7.gif")
img = tk.Label(r7, image = photo)
img.pack()

#Timer   
def start(t):
  lab.config(text = str(t))
  if(t > 0):
    r7.after(1000, start, t-1)
  if t == 0:
    global window
    window = tk.Toplevel(r7)
    tim = tk.Message (window, text = "Out of time")
    tim.pack()
    restr = tk.Button (window, text = "Restart", command = ret)
    restr.pack()
def ret():
  start(30)
  window.destroy()    
lab = tk.Label(r7)
lab.pack(side = "left")
start(30)

#Hint
def create_window():
    window = tk.Toplevel(r7)
    hint = tk.Message(window, text = "I said SQUARES, not RECTANGLES")
    hint.pack()
hint_butt = tk.Button(r7, text = "Hint", command = create_window)
hint_butt.pack(side = "right")

#Input
input_box = tk.Entry(r7, bd=5)
input_box.pack()

#Button for Checking
button = tk.Button(r7, text = "Check", command = check)
button.pack()

r7.mainloop()

##LEVEL 8##
r8 = tk.Tk()
solution = 11

def check():
  user_guess = int(input_box.get())
  if solution == user_guess:
    msg = "Correct!"
    lvl2 = tk.Button(r8, text ="Congrats! Let's go to the next level", command = next)
    lvl2.pack()
  else:
    msg = "Try again!"
  lbl_result = tk.Label(r8, text = msg)
  lbl_result.pack()

def next():
  r8.destroy()
#Level
lvl_txt = tk.Label(r8, text = "Level 8")
lvl_txt.pack()

#Question
q = tk.Label(r8, text = "How many squares are there?")
q.pack()

#Card Image
card = tk.PhotoImage(file = "s8.gif")
c_lbl = tk.Label(r8, image = card)
c_lbl.pack()

#Timer   
def start(t):
  lab.config(text = str(t))
  if(t > 0):
    r8.after(1000, start, t-1)
  if t == 0:
    global window
    window = tk.Toplevel(r8)
    tim = tk.Message (window, text = "Out of time")
    tim.pack()
    restr = tk.Button (window, text = "Restart", command = ret)
    restr.pack()
def ret():
  start(30)
  window.destroy()    
lab = tk.Label(r8)
lab.pack(side = "left")
start(30)


#Hint
def create_window():
    window = tk.Toplevel(r8)
    hint = tk.Message(window, text = "Step by step")
    hint.pack()
hint_butt = tk.Button(r8, text = "Hint", command = create_window)
hint_butt.pack(side = "right")

#Input
input_box = tk.Entry(r8, bd=5)
input_box.pack()

#Button for Checking
button = tk.Button(r8, text = "Check", command = check)
button.pack()

r8.mainloop()

##LEVEL 9##
solution = 15
def check():
  user_guess = int(input_box.get())
  if solution == user_guess:
    msg = "Correct!"
    lvl2 = tk.Button(r9, text ="Congrats! Let's go to the next level", command = next)
    lvl2.pack()
  else:
    msg = "Try again!"
  lbl_result = tk.Label(r9, text = msg)
  lbl_result.pack()

def next():
  r9.destroy()
   
r9 = tk.Tk()

#Level
lvl_txt = tk.Label(r9, text = "Level 9")
lvl_txt.pack()

#Question
q = tk.Label(r9, text = "How many squares are there?")
q.pack()

#Card Image
photo = tk.PhotoImage(file = "s9.gif")
img = tk.Label(r9, image = photo)
img.pack()

#Timer   
def start(t):
  lab.config(text = str(t))
  if(t > 0):
    r9.after(1000, start, t-1)
  if t == 0:
    global window
    window = tk.Toplevel(r9)
    tim = tk.Message (window, text = "Out of time")
    tim.pack()
    restr = tk.Button (window, text = "Restart", command = ret)
    restr.pack()
def ret():
  start(30)
  window.destroy()    
lab = tk.Label(r9)
lab.pack(side = "left")
start(30)

#Hint
def create_window():
    window = tk.Toplevel(r9)
    hint = tk.Message(window, text = "Happiness may come in DIFFERENT shapes and SIZES")
    hint.pack()
hint_butt = tk.Button(r9, text = "Hint", command = create_window)
hint_butt.pack(side = "right")

#Input
input_box = tk.Entry(r9, bd=5)
input_box.pack()

#Button for Checking
button = tk.Button(r9, text = "Check", command = check)
button.pack()

r9.mainloop()

##LEVEL 10##
r10 = tk.Tk()
solution = 40

def check():
  user_guess = int(input_box.get())
  if solution == user_guess:
    msg = "Correct!"
    lvl2 = tk.Button(r10, text ="Congrats! YOU WIN!!", command = next)
    lvl2.pack()
  else:
    msg = "Try again!"
  lbl_result = tk.Label(r10, text = msg)
  lbl_result.pack()

def next():
  r10.destroy()
#Level
lvl_txt = tk.Label(r10, text = "Level 10")
lvl_txt.pack()

#Question
q = tk.Label(r10, text = "How many squares are there?")
q.pack()

#Card Image
card = tk.PhotoImage(file = "s10.gif")
c_lbl = tk.Label(r10, image = card)
c_lbl.pack()

#Timer   
def start(t):
  lab.config(text = str(t))
  if(t > 0):
    r10.after(1000, start, t-1)
  if t == 0:
    global window
    window = tk.Toplevel(r10)
    tim = tk.Message (window, text = "Out of time")
    tim.pack()
    restr = tk.Button (window, text = "Restart", command = ret)
    restr.pack()
def ret():
  start(30)
  window.destroy()    
lab = tk.Label(r10)
lab.pack(side = "left")
start(30)


#Hint
def create_window():
    window = tk.Toplevel(r10)
    hint = tk.Message(window, text = "This is the boss")
    hint.pack()
hint_butt = tk.Button(r10, text = "Hint", command = create_window)
hint_butt.pack(side = "right")

#Input
input_box = tk.Entry(r10, bd=5)
input_box.pack()

#Button for Checking
button = tk.Button(r10, text = "Check", command = check)
button.pack()

r10.mainloop()
