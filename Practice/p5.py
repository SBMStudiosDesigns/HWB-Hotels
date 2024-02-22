import customtkinter

customtkinter.set_appearance_mode('dark')

root = customtkinter.CTk()
root.title("Fullscreen App")
root.geometry('300x300')

width = root.winfo_screenwidth()            
height = root.winfo_screenheight()

frame = customtkinter.CTkScrollableFrame(root, width=width, height=height)
frame.pack()

for i in range(1,18):
    label = customtkinter.CTkLabel(frame,text=f'This is sentence {i}')
    label.pack()

root.after(0, lambda:root.state('zoomed'))
root.mainloop()