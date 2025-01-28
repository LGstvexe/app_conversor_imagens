import os
from tkinter import filedialog
from tkinter import Tk, Button, Listbox, StringVar, OptionMenu, END
from PIL import Image


def add_files():
    files = filedialog.askopenfilenames(title='Escolha as imagens',
                                        filetypes=[('Imagens', '*.jpg;*.jpeg;*.png;*.bmp;*.jfif;*.webp')])
    for file in files:
        listbox.insert(END, file)


def convert_image(input_path, output_format, output_directory):
    im = Image.open(input_path)
    output_path = os.path.join(output_directory, os.path.splitext(os.path.basename(input_path))[0]
                               + '.' + output_format)
    if output_format == 'jpg' or 'jfif':
        rgb_im = im.convert('RGB')
        rgb_im.save(output_path)
        print("A imagem foi convertida com sucesso.")
    else:
        im.save(output_path)
        print("A imagem foi convertida com sucesso.")


def on_convert():
    output_format = format_var.get()
    output_directory = directory_var.get()
    for file in listbox.get(0, listbox.size() - 1):
        convert_image(file, output_format, output_directory)


def clear_listbox():
    listbox.delete(0, END)


def select_directory():
    directory = filedialog.askdirectory(title='Escolha a pasta de destino')
    if directory:
        directory_var.set(directory)


# Janela principal
main_window = Tk()
main_window.title('Conversor de Imagens')

listbox = Listbox(main_window, selectmode='multiple', width=50, height=15)
listbox.grid(row=0, column=0, padx=10, pady=10)

format_var = StringVar(main_window)
format_var.set('png')

formats = ["png", "jpg", "bmp", "gif", "jfif", "webp"]
format_menu = OptionMenu(main_window, format_var, *formats)
format_menu.grid(row=0, column=1, padx=10, pady=10)

add_button = Button(main_window, text='Adicionar imagens', command=add_files)
add_button.grid(row=1, column=0, padx=10, pady=5)

directory_var = StringVar(main_window)
directory_button = Button(main_window, text='Selecionar pasta de destino', command=select_directory)
directory_button.grid(row=1, column=1, padx=10, pady=5)

convert_button = Button(main_window, text='Converter', command=on_convert)
convert_button.grid(row=1, column=2, padx=10, pady=5)

clear_button = Button(main_window, text='Limpar', command=clear_listbox)
clear_button.grid(row=1, column=3, padx=10, pady=5)

main_window.mainloop()
