from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
import os

root = Tk()
root.title("Image Editor")
root.geometry("500x500")
root.configure(background = "lightblue")

label_image = Label(root, text = "Open Image ", bg = "lightblue", highlightthickness=10)
label_image.place(relx = 0.5, rely = 0.4, anchor = CENTER)
img_path = ""

def openImg():
    global img_path
    img_path = filedialog.askopenfilename(title = "Open Image File", filetypes = [("Image Files", "*.jpg *.png *.gif *.jpeg *.jfif *.jpe")])
    print(img_path)
    im = Image.open(img_path)
    img = ImageTk.PhotoImage(im)

    label_image["image"] = img
    img.close()
    
def rotateImage():
        global img_path
        img2 = Image.open(img_path)
        rotated_image = img2.rotate(180)
        image = ImageTk.PhotoImage(rotated_image)
        label_image["image"] = image
        image.close()
        
rotate_button = Button(root, text = "Rotate Image", bg = "Grey", fg = "white", font = ("castellar", 15, "bold"), padx = 15, pady = 10, relief = SOLID, command = rotateImage)
rotate_button.place(relx = 0.5, rely = 0.7, anchor = CENTER)
        
open_btn = Button(root, text = "Open Image", bg = "Grey", fg = "white", font = ("castellar", 15, "bold"), padx = 15, pady = 10, relief = SOLID, command = openImg)
open_btn.place(relx = 0.5, rely = 0.1, anchor = CENTER)

Footer = Label(root, text = "Created by : Shreshth Shukla", fg="red")
Footer.place(relx = 0.5, rely = 1.0)

root.mainloop()