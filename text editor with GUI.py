"""This script has text editor features, such as opening and saving files, cutting, deleting
and pasting, text alignment and font changes. It uses GUI tkinter"""

#import standar modules
from tkinter import *
import tkinter as tk 
from tkinter import font
from tkinter import filedialog 
from tkinter import ttk

#--- Create the window widget ---
frame = tk.Tk() 
#set the title
frame.title("TextBox Input") 
#set the dimensions
frame.geometry('800x400') 

# --- FONT ---
def bold(): 
    """This method gets the select text and adds or removes bold font"""
    # --- set the text configuration ---
    #gets the font from the text
    bold = font.Font(inputtxt, inputtxt.cget("font"))
    #gets the current tags from the select text    
    tags_font = inputtxt.tag_names('sel.first')
    #condition, check if any other font has been applied, in order to keep that font
    #if italic has been applied
    if 'italic' in tags_font:
        #if underline has been applied
        if 'underline' in tags_font:
            #change the current font to bold and stay italic and underline
            bold.configure(weight="bold", slant='italic', underline=True)
        else:
            #changes the current font to bold and stay italic 
            bold.configure(weight="bold", slant='italic', underline=False)
    #if underline has been applied
    elif 'underline' in tags_font:
        #if italic has been applied
        if 'italic' in tags_font:
            #changes the current font to bold and stay italic and underline
            bold.configure(weight="bold", slant='italic', underline=True)
        else:
            #changes the current font to bold and stay underline
            bold.configure(weight="bold", underline=True)
    else:
        #changes the current font to bold
        bold.configure(weight="bold")

    # --- TAG configure ---
    #creates a tag with the name "bold" and change the font using our text configuration
    inputtxt.tag_configure("bold", font=bold)
    #gets the current tags from the select text    
    tags = inputtxt.tag_names("sel.first")
    #condition, if the selected text is already bold
    if "bold" in tags:
        #removes bold from the select text
        inputtxt.tag_remove("bold", "sel.first", "sel.last")
    else: 
        #else, it adds the bold tag
        inputtxt.tag_add("bold", "sel.first", "sel.last")
    
def italic():
    """This method gets the select text and adds or removes italic font"""
    # --- set the text configuration ---
    #gets the font from the text
    italic = font.Font(inputtxt, inputtxt.cget("font"))
    #gets the current tags from the select text    
    tags_font2 = inputtxt.tag_names('sel.first')
    #condition, check if any other font has been applied, in order to keep that font
    #if bold has been applied
    if 'bold' in tags_font2:
        #if underline has been applied
        if 'underline' in tags_font2:
            #changes the current font to italic and stay bold and underline
            italic.configure(weight="bold", slant='italic', underline=True)
        else:
            #changes the current font to italic and stay bold
            italic.configure(weight="bold", slant='italic')
    #if underline has been applied
    elif 'underline' in tags_font2:
        #if bold has been applied
        if 'bold' in tags_font2:
            #changes the current font to italic and stay bold and underline
            italic.configure(weight="bold", slant='italic', underline=True)
        else:
            #changes the current font to italic and stay underline
            italic.configure(slant='italic', underline=True)
    else:
        #changes the current font to italic
        italic.configure(slant='italic')

    # --- TAG configure ---
    #creates a tag with the name "italic" and change the font using our text configuration
    inputtxt.tag_configure("italic",font=italic)
    #gets the current tags from the select text    
    italic_tags = inputtxt.tag_names("sel.first")
    #condition, if the selected text is already italics
    if "italic" in italic_tags:
        #removes italic from the select text
        inputtxt.tag_remove("italic", "sel.first", "sel.last")
    else: 
        #else, it adds the italic tag
        inputtxt.tag_add("italic", "sel.first", "sel.last")

def underline():
    """This method gets the select text and adds or removes underline font"""
    # --- set the text configuration ---
    #gets the font from the text
    font_underline = font.Font(inputtxt, inputtxt.cget("font"))
    #gets the current tags from the select text    
    tags_font3 = inputtxt.tag_names('sel.first')
    #condition, check if any other font has been applied, in order to keep that font
    #if bold has been applied
    if 'bold' in tags_font3:
        #if italic has been applied
        if 'italic' in tags_font3: 
            #changes the current font to underline and stay italic and bold
            font_underline.configure(weight="bold", slant='italic', underline=True)
        else:
            #changes the current font to underline and stay bold
            font_underline.configure(weight='bold', underline=True)
    #if italic has been applied
    elif 'italic' in tags_font3:
        #if bold has been applied
        if 'bold' in tags_font3:
            #changes the current font to underline and stay italic and underline
            font_underline.configure(weight="bold", slant='italic', underline=True)
        else:
            #changes the current font to underline and stay italic 
            font_underline.configure(slant='italic', underline=True)
    else:
        #change the current font to bold
        font_underline.configure(underline=True)

    # --- TAG configure ---
    #creates a tag with the name "underline" and change the font using our text configuration
    inputtxt.tag_configure("underline", font=font_underline)
    #gets the current tags from the select text    
    underline_tags = inputtxt.tag_names("sel.first")
    #condition, if the selected text is already underlined
    if "underline" in underline_tags:
        #removes underline from the select text
        inputtxt.tag_remove("underline", "sel.first", "sel.last")
    else: 
        #else, it adds the undeline tag
        inputtxt.tag_add("underline", "sel.first", "sel.last")

# --- CLIPBOARD ---
def delete_select():
    """This method delete the select text"""
    #calls the delete method and erase the selected text
    inputtxt.delete('sel.first', 'sel.last')

class CutPaste:
    def __init__(self) -> None:
        self.save_select = ''
        self.cursor_position = ''

    def cut(self):
        """This method saves the selected text before deleting it, in order to be able to paste it"""
        #gets the selected text and save it 
        self.save_select = inputtxt.get('sel.first', 'sel.last') 
        #calls the delete method and delete the selected text after saving it
        inputtxt.delete('sel.first', 'sel.last')

    def paste(self):
        """This method takes the saved text and pastes it where the user places the cursor"""
        #calls the insert method to paste
        self.cursor_position = inputtxt.index("insert")
        #takes the position where the user wants to paste
        if self.save_select:
            inputtxt.insert(self.cursor_position, self.save_select)
        elif self.copy_select:
            inputtxt.insert(self.cursor_position, self.copy_select)

    def copy(self):
        """This method saves the selected text, in order to be able to paste it"""
        #gets the selected text and save it 
        self.copy_select = inputtxt.get('sel.first', 'sel.last') 
        
# --- FILE MANAGER ---
def open():
    """This method uses the filedialog class from tkinter to opening files"""
    open_file = filedialog.askopenfile()
    #condition, if the user opens a file
    if open_file:
        #reads the file
        lines = open_file.read()
        #clear the current screen
        inputtxt.delete('0.1',END)
        #shows the file 
        inputtxt.insert('0.1', lines)

def save():
    """This method uses the filedialog class from tkinter to saving files"""
    #gets the content of the screen and saves it
    save_text = inputtxt.get(1.0, "end-1c") 
    #opens the directory window
    save_file = filedialog.asksaveasfile()
    #condition, if the user saves a file
    if save_file:
        #overwrite the new content
        save_file.write(save_text)

# --- PARAGRAPH ---
def justify_center():
    """This method alings the text to the screen's center"""
    #gets the cursor position
    cursor_position1 = inputtxt.index("insert")
    #extracts the row where the cursor is
    center_line = cursor_position1[0]+'.0'
    #gets the tags that the row has
    line_center = inputtxt.tag_names(center_line)
    #scrolls through the tuple 
    for tag in line_center:
        #condition, if tags "center, left and/or right"
        if tag == 'center' or tag == 'left' or tag == 'right':
            #remove tags 
            inputtxt.tag_remove(tag,"1.0","end")
    # --- Tag configure ---
    #creates a tag with the name "center" and use the justify parameter to center the text
    inputtxt.tag_configure("center", justify='center')
    #adds the tag to the line where the cursor is positioned
    inputtxt.tag_add("center", center_line, "end")

def justify_left():
    """This method alings the text to the screen's left"""
    #gets the cursor position
    cursor_position2 = inputtxt.index("insert")
    #extracts the row where the cursor is
    left_line = cursor_position2[0]+'.0'
    #gets the tags that the row has
    left_center = inputtxt.tag_names(left_line)
    #scrolls through the tuple 
    for tag in left_center:
        #condition, if tags "center, left and/or right"
        if tag == 'center' or tag == 'left' or tag == 'right':
            #remove tags 
            inputtxt.tag_remove(tag,"1.0","end")
    # --- Tag configure ---
    #creates a tag with the name "left" and use the justify parameter left
    inputtxt.tag_configure("left", justify='left')
    #adds the tag to the line where the cursor is positioned
    inputtxt.tag_add("left", left_line, "end")
    
def justify_right():
    """This method alings the text to the screen's right"""
    #gets the cursor position
    cursor_position3 = inputtxt.index("insert")
    #extracts the row where the cursor is
    line_right = cursor_position3[0]+'.0'
    #gets the tags that the row has
    right_center = inputtxt.tag_names(line_right)
    #scrolls through the tuple 
    for tag in right_center:
        #condition, if tags "center, left and/or right"
        if tag == 'center' or tag == 'left' or tag == 'right':
            #remove tags 
            inputtxt.tag_remove(tag,"1.0","end")
    # --- Tag configure ---
    #creates a tag with the name "right" and use the justify parameter to center the text
    inputtxt.tag_configure("right", justify='right')
    #adds the tag to the line where the cursor is positioned
    inputtxt.tag_add("right", line_right, "end")

def font_size():
    """This method allows to change the font size"""
    size_selection = combo.get()
    inputtxt.configure(font=('Arial', size_selection))

# --- font size dropdown ---
#creates the dropdown box
combo = ttk.Combobox(state='readonly', values=[10, 15, 20, 25, 30])
#positions the dropdown
combo.place(x=10, y=200)

# --- creates the dropdown's label ---
combo_label = tk.Label(frame, font=bold, text='Font Size')
#shows on screen
combo_label.pack()
#sets the position on screen 
combo_label.place(x=60, y=160)

# TextBox Creation 
#--- Create the text widget ---
inputtxt = tk.Text(frame,height = 30, width = 30 ) 
#confifure font
inputtxt.configure(font=('Arial', 15))
#shows on screen
inputtxt.pack() 
#focus the cursor on the textbox
inputtxt.focus()

#--- Font pad label ---
style_label = tk.Label(frame, font=bold, text='Font')
style_label.config(font=("Arial", 15))
#shoving it onto screen
style_label.pack()
style_label.place(x=70, y=60)

# --- Clipboard pad label ----
clip_label = tk.Label(frame, font=bold, text='Clipboard')
clip_label.config(font=("Arial", 15))
#shoving it onto screen
clip_label.pack()
clip_label.place(x=50, y=230)

# --- Paragraph pad label ----
par_label = tk.Label(frame, font=bold, text='Paragraph')
par_label.config(font=("Arial", 15))
#shoving it onto screen
par_label.pack()
par_label.place(x=50, y=300)

# Button Applied size creation
button = ttk.Button(text="Applied size", command=font_size)
button.place(x=155, y=200)

# Button Bold Creation
bold_button = tk.Button(frame, borderwidth=5, text = "Bold", bg='gray',command = bold) 
#Shows it on the screen
bold_button.pack() 
#Positions x y
bold_button.place(x=20, y=100)

#Button Italic Creation
italic_button = tk.Button(frame, borderwidth=5, text="Italic", bg='gray', command=italic)
italic_button.pack()
italic_button.place(x=70, y=100)

#Button underline Creation
underline_button = tk.Button(frame, borderwidth=5, bg='gray',text="Underline",  command=underline)
underline_button.pack()
underline_button.place(x=120, y=100)

#Button delete select Creation
delete_button = tk.Button(frame, borderwidth=5, bg='gray',text="Delete select", command=delete_select)
delete_button.pack()
delete_button.place(x=150, y=260)

#Button cut Creation
cut_paste = CutPaste()
cut_button = tk.Button(frame, borderwidth=5, bg='gray', text="Cut", command=cut_paste.cut)
cut_button.pack()
cut_button.place(x=10, y=260)

#Button paste Creation
paste_button = tk.Button(frame, borderwidth=5, bg='gray',text="Paste", command=cut_paste.paste)
paste_button.pack()
paste_button.place(x=50, y=260)

#Button copy Creation
copy_button = tk.Button(frame, borderwidth=5, bg='gray',text="Copy", command=cut_paste.copy)
copy_button.pack()
copy_button.place(x=100, y=260)

#Button open file Creation
open_button = tk.Button(frame, borderwidth=5, bg='sky blue',text="Open file", command=open)
open_button.pack()
open_button.place(x=20, y=10)

#Button save file Creation
save_button = tk.Button(frame, borderwidth=5, bg='sky blue', text="Save As", command=save)
save_button.pack()
save_button.place(x=100, y=10)

#Button justify center Creation
center_button = tk.Button(frame, borderwidth=5, bg='sky blue', text="Center", command=justify_center)
center_button.pack()
center_button.place(x=20, y=330)

#Button justify left Creation
left_button = tk.Button(frame, borderwidth=5, bg='sky blue', text="Left", command=justify_left)
left_button.pack()
left_button.place(x=80, y=330)

#Button justify right Creation
right_button = tk.Button(frame, borderwidth=5, bg='sky blue', text="Right", command=justify_right)
right_button.pack()
right_button.place(x=130, y=330)

#infinity loop to show the screen
frame.mainloop() 