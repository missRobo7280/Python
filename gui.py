##import tkinter as tk
##a=tk.Tk()
##b=tk.Button(a,text='hello',fg='maroon')
###b.grid(row=0,column=0)
##b.place(x=40,y=60)
##c=tk.Button(a,text='hi',fg='green')
###b.pack(side='right')
##c.grid(row=0,column=1)#fixed positions
###c.pack(side='top')
###we can give the customized coordinates
##c.place(x=10,y=60)
##a.mainloop()
##
##import tkinter as tk
##a=tk.Tk()
##b=tk.Checkbutton(a,text='hello',fg='green')
##b.pack(side='left')
##c=tk.Checkbutton(a,text='hi',fg='red')
##c.pack(side='left')
##a.mainloop()

##import tkinter as tk
##a=tk.Tk()
##l=tk.Label(a,text='name')
##l.pack()
##a.mainloop()
##import tkinter as tk
##a=tk.Tk()
##l1=tk.Label(a,text=' first name').grid(row=0,column=0)
##l1=tk.Label(a,text='last name').grid(row=1,column=0)
##e1=tk.Entry(a).grid(row=0,column=1)
##e2=tk.Entry(a).grid(row=1,column=1)
##a.mainloop()
##
##import tkinter as tk
##a=tk.Tk()
##f=tk.Frame(a)
##f.pack()
##f1=tk.Frame(a)
##f1.pack(side='bottom')
##b=tk.Button(f,text='c',fg='red)

import tkinter as tk
a=tk.Tk()
l=tk.Listbox(a)
l.insert(1,'c')
l.insert(2,'cpp')
l.insert(3,'java')
l.insert(4,'python')
l.pack()
a.mainloop


            
