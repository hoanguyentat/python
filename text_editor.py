import Tkinter
from Tkinter import Menu
import tkFileDialog
import tkMessageBox
import ScrolledText # Because Tkinter textarea does not provide scrolling
#  abilities, we use this additional library
root = Tkinter.Tk(className=" Just another Text Editor")

textPad = ScrolledText.ScrolledText(root, width=100, height=80)
textPad.pack()
def dummy():
    print "I am a Dummy Command, I will be removed in the next step"

def open_command():
	file = tkFileDialog.askopenfile(parent=root, mode='rb', title="select a file")
	if file != None:
		contents = file.read()
		textPad.insert('1.0', contents)

def save_command():
	file = tkFileDialog.asksaveasfile(mode="w")
	if file != None:
		data = self.textPad.get('1.0', END + '-1c')
		file.write(data)
		file.close()

def exit_command():
	if tkMessageBox.askokcancel("Quit", "Ban thuc su muon thoat?"):
		root.destroy()

def about_command():
	label = tkMessageBox.showinfo("About", "Text editor made by Hola!")

def help_command():
	pass

#create a menu
menu = Menu(root)
root.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="new", command=dummy)
filemenu.add_command(label="open", command=open_command)
filemenu.add_command(label="save", command=save_command)
filemenu.add_separator()
filemenu.add_command(label="exit", command=exit_command)
helpmenu = Menu(menu)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="Help", command=dummy)
helpmenu.add_command(label="About", command=about_command)
root.mainloop()

