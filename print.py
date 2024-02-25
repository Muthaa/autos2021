# text = 'ePIC'

# # print(f'{text:#<20}')
# # print(f'{text:_>20}')
# # print(f'{text:.^20}')
# print(f'{text:.^20}')

# print('ePIC'" "*20000)

text = 'ePIC'" "*373

# importing tkinter for gui
import tkinter
import customtkinter
customtkinter.set_appearance_mode("System")
# creating window
window = customtkinter.CTk()

# setting attribute
window.attributes('-fullscreen', True)
window.title(" ")

text_1 = customtkinter.CTkTextbox(master=window)
text_1.pack(fill="both", expand=True)
text_1.insert("1.0", text)
text_1.configure(font=(" ",30,"bold"))

window.mainloop()
