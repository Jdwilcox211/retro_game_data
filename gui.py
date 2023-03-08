import tkinter as tk
import ttkbootstrap as tkb
from ttkbootstrap.constants import *


# b1 = tkb.Button(root, text="Button 1", bootstyle=SUCCESS)
# b1.pack(side=LEFT, padx=5, pady=10)

# b2 = tkb.Button(root, text="Button 2", bootstyle=(INFO, OUTLINE))
# b2.pack(side=LEFT, padx=5, pady=10)
def donothing():
   x = 0
#show_frame not working
def show_frame(frame_name):
        '''Show a frame for the given page name'''
        nb.select(frame_name)

    



root = tkb.Window(themename="pulse")
root.title('Retro Fab')
width_value=root.winfo_screenwidth()
height_value=root.winfo_screenheight()
root.geometry(f'{width_value}x{height_value}+0+0')

#root.attributes('-fullscreen', True) #fullscreen method


# b1 = tkb.Button(root, text='primary', bootstyle=PRIMARY)
# b1.pack(side=LEFT, padx=5, pady=5)

# b2 = tkb.Button(root, text='secondary', bootstyle=SECONDARY)
# b2.pack(side=LEFT, padx=5, pady=5)

# b3 = tkb.Button(root, text='success', bootstyle=SUCCESS)
# b3.pack(side=LEFT, padx=5, pady=5)

# b4 = tkb.Button(root, text='info', bootstyle=INFO)
# b4.pack(side=LEFT, padx=5, pady=5)

# b5 = tkb.Button(root, text='warning', bootstyle=WARNING)
# b5.pack(side=LEFT, padx=5, pady=5)

# b6 = tkb.Button(root, text='danger', bootstyle=DANGER)
# b6.pack(side=LEFT, padx=5, pady=5)

# b7 = tkb.Button(root, text='light', bootstyle=LIGHT)
# b7.pack(side=LEFT, padx=5, pady=5)

# b8 = tkb.Button(root, text='dark', bootstyle=DARK)
# b8.pack(side=LEFT, padx=5, pady=5)






nb=tkb.Notebook(root, bootstyle="primary")
nb.pack(pady=10, expand=True)



frame1 = tkb.Frame(nb, width=width_value, height=height_value)

label= tkb.Label(frame1, text="Hello World", font=('Arial',18))
label.pack(padx=20,pady=20)


frame2 = tkb.Frame(nb, width=width_value, height=height_value)


title= tkb.Label(frame2, text="Add Game", font=('Arial bold',18))
title.pack(padx=20,pady=20)

entryframe = tk.Frame(frame2)
entryframe.columnconfigure(0,weight=1)
entryframe.columnconfigure(1,weight=1)
entryframe.columnconfigure(2,weight=1)
entryframe.columnconfigure(3,weight=1)
entryframe.columnconfigure(4,weight=1)
entryframe.columnconfigure(5,weight=1)


#limit yGame Name to 70 characters
def limitSizegmname(*args):
    value = gmnameValue.get()
    if len(value) > 70: gmnameValue.set(value[:70])

gmnameValue = tkb.StringVar()
gmnameValue.trace('w', limitSizegmname)

gmnamelabel= tkb.Label(entryframe, text="Game Title (70 Character limit)", font=('Arial bold',12), justify=LEFT, anchor="w")
gmnamelabel.grid(sticky = W, row=0,column=1)

addgntb=tkb.Entry(entryframe, width=60, font=('Ariel',12), bootstyle="primary", textvariable=gmnameValue)
addgntb.grid(sticky = W, row=1,column=1, pady=(0, 20))



pflabel= tkb.Label(entryframe, text="Platform", font=('Arial bold',12), justify=LEFT, anchor="w")
pflabel.grid(sticky = W, row=0,column=2)

addpftb=tkb.Entry(entryframe, width=25, font=('Ariel',12), bootstyle="primary")
addpftb.grid(sticky = W, row=1,column=2, pady=(0, 20))



#limit year to 4 numbers
def limitSizeYear(*args):
    value = yearValue.get()
    if len(value) > 4: yearValue.set(value[:4])

yearValue = tkb.StringVar()
yearValue.trace('w', limitSizeYear)

ryearlabel= tkb.Label(entryframe, text="Release Year (4 digits)", font=('Arial bold',12), justify=LEFT, anchor="w")
ryearlabel.grid(sticky = W, row=2,column=1)

addrytb=tkb.Entry(entryframe, width=4, font=('Ariel',12), textvariable=yearValue, bootstyle="primary")
#addrytb.insert(0, "1995") #entry text example
addrytb.grid(sticky = W, row=3,column=1, pady=(0, 20))



publabel=tkb.Label(entryframe, text="Publisher", font=('Arial bold',12), justify=LEFT, anchor="w")
publabel.grid(sticky = W, row=2,column=2)

addpubtb=tkb.Entry(entryframe, width=25, font=('Ariel',12), bootstyle="primary")
addpubtb.grid(sticky = W, row=3,column=2, pady=(0, 20))



lclabel= tkb.Label(entryframe, text="Licensed", font=('Arial bold',12), justify=LEFT, anchor="w")
lclabel.grid(sticky = W, row=4,column=2)

#Menu Button option/example
# addlctb=tkb.Menubutton(entryframe, style='Outline.TMenubutton')
# addlctb.grid(sticky = W, row=5,column=1)
# # add options
# addlctbmenu=tkb.Menu(addlctb)
# addlctbmenu.configure(font=('Arial',12))
# option_addlctb = tkb.StringVar()
# for option in [' - ', 'No', 'Yes']:
#     addlctbmenu.add_radiobutton(label=option, value=option, variable=option_addlctb)
# # associate menu with menubutton
# addlctb['menu'] = addlctbmenu

addlctb= tk.StringVar()
dropaddlctb=tkb.OptionMenu(entryframe, addlctb, '','','No','Yes',style='Outline.TMenubutton')
# dropaddlctb.config(style='Outline.TMenubutton') # alternate way to add style
dropaddlctb.grid(sticky = W, row=5,column=2, pady=(0, 20))





addowntb=tkb.Checkbutton(entryframe, text="Owned", style='Outline.Toolbutton')
addowntb.grid(sticky = W, row=1,column=3, pady=(0, 5))



addplytb=tkb.Checkbutton(entryframe, text="Played", style='Outline.Toolbutton')
addplytb.grid(sticky = W, row=2,column=3, pady=(0, 5))
# addplytb.configure(font=('Helvetica', 12))

addbeattb=tkb.Checkbutton(entryframe, text="Completed", style='Outline.Toolbutton')
addbeattb.grid(sticky = W, row=3,column=3, pady=(0, 5))
# addbeattb.configure(font=('Helvetica', 12))



rtlabel= tkb.Label(entryframe, text="Rating", font=('Arial bold',12), justify=LEFT, anchor="w")
rtlabel.grid(sticky = W, row=4,column=1)

addrttb= tk.StringVar()
dropaddrttb=tkb.OptionMenu(entryframe, addrttb, '','','1 Star','2 Stars','3 Stars','4 Stars','5 Stars',style='Outline.TMenubutton')
# dropaddlctb.config(style='Outline.TMenubutton') # alternate way to add style
dropaddrttb.grid(sticky = W, row=5,column=1, pady=(0, 20))



diflabel= tkb.Label(entryframe, text="Difficulty", font=('Arial bold',12), justify=LEFT, anchor="w")
diflabel.grid(sticky = W, row=6,column=2)

adddiftb= tk.StringVar()
dropadddiftb=tkb.OptionMenu(entryframe, adddiftb, '','','Easy','Challenging','Insane',style='Outline.TMenubutton')
# dropaddlctb.config(style='Outline.TMenubutton') # alternate way to add style
dropadddiftb.grid(sticky = W, row=7,column=2, pady=(0, 20))



devlabel= tkb.Label(entryframe, text="Development", font=('Arial bold',12), justify=LEFT, anchor="w")
devlabel.grid(sticky = W, row=6,column=1)

adddevtb= tk.StringVar()
dropadddevtb=tkb.OptionMenu(entryframe, adddevtb, '','','Poor','Mediocre','Good','Extraordinary',style='Outline.TMenubutton')
# dropaddlctb.config(style='Outline.TMenubutton') # alternate way to add style
dropadddevtb.grid(sticky = W, row=7,column=1, pady=(0, 20))






















usnotelabel= tkb.Label(entryframe, text="User Notes", font=('Arial bold',12), justify=LEFT, anchor="w")
usnotelabel.grid(sticky = W, row=8,column=1)

addusnotetb=tkb.Text(entryframe, height= 10 ,width=60, font=('Ariel',12))
addusnotetb.grid(sticky = W, row=9,column=1, pady=(0, 20))


gmnotelabel= tkb.Label(entryframe, text="Additional Game Details", font=('Arial bold',12), justify=LEFT, anchor="w")
gmnotelabel.grid(sticky = W, row=8,column=2)

addgnotetb=tkb.Text(entryframe, height= 10 ,width=60, font=('Ariel',12))
addgnotetb.grid(sticky = W, row=9,column=2, pady=(0, 20))














entryframe.pack(fill='x')






frame3 = tkb.Frame(nb, width=width_value, height=height_value)
frame4 = tkb.Frame(nb, width=width_value, height=height_value)
frame5 = tkb.Frame(nb, width=width_value, height=height_value)
frame6 = tkb.Frame(nb, width=width_value, height=height_value)
frame7 = tkb.Frame(nb, width=width_value, height=height_value)


frame1.pack(fill='both', expand=True)
frame2.pack(fill='both', expand=True)
frame3.pack(fill='both', expand=True)
frame4.pack(fill='both', expand=True)
frame5.pack(fill='both', expand=True)
frame6.pack(fill='both', expand=True)
frame7.pack(fill='both', expand=True)



#tkb.Style.configure(tabposition='nw')
nb.add(frame1, text='Summary')
nb.add(frame2, text='Add Game')
nb.add(frame3, text='Search Game')
nb.add(frame4, text='Bulk Upload')
nb.add(frame5, text='Report')
nb.add(frame6, text='Settings')
nb.add(frame7, text='User Info')


















menubar = tkb.Menu(root)
filemenu = tkb.Menu(menubar, tearoff=0)
filemenu.add_command(label="Add User", command=donothing)
filemenu.add_command(label="Settings", command=donothing)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)

optionsmenu = tkb.Menu(menubar, tearoff=0)
optionsmenu.add_command(label="Summary", command=show_frame(frame1))
optionsmenu.add_command(label="Add Game", command=donothing)
optionsmenu.add_command(label="Search", command=donothing)
optionsmenu.add_command(label="Bulk Upload", command=donothing)
optionsmenu.add_command(label="Reports", command=donothing)
optionsmenu.add_command(label="Settings", command=donothing)
optionsmenu.add_command(label="User Info", command=donothing)
menubar.add_cascade(label="Options", menu=optionsmenu)

helpmenu = tkb.Menu(menubar, tearoff=0)
helpmenu.add_command(label="About...", command=donothing)
menubar.add_cascade(label="Help", menu=helpmenu)

root.config(menu=menubar)
root.mainloop()