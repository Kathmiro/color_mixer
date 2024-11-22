import tkinter as tk
from tkinter import simpledialog, messagebox

def color_converter(color):
    """with help of this function, we convert the color from HEX or RGB to RGB-format, 
    this formula was taken from the forum: https://stackoverflow.com/questions/29643352/converting-hex-to-rgb-value-in-python """
    if color.startswith('#'):  # if HEX
        return tuple(int(color.lstrip('#')[i:i+2], 16) for i in (0, 2, 4))
    else:  # if RGB
        return tuple(map(int, color.split(',')))

def mix_colors(rgb1, rgb2):
    """this function helps us to mix two RGB-colors"""
    return tuple((c1 + c2) // 2 for c1, c2 in zip(rgb1, rgb2))

def rgb_to_hex(rgb):
    """convert RGB into HEX, 
    this formula was taken fron the site https://docs.bokeh.org/en/3.5.0/_modules/bokeh/colors/color.html"""
    return f"#{rgb[0]:02x}{rgb[1]:02x}{rgb[2]:02x}"

def main():
    # Creating a hidden Tkinter window
    root = tk.Tk()
    root.withdraw()

    while True:
        try:
    # User input colors
            color1 = simpledialog.askstring("1 цвет", "Введите первый цвет (RGB: 0,0,0 or HEX: #ff0000):")
            color2 = simpledialog.askstring("2 цвет", "Введите второй цвет (RGB: 0,0,0 or HEX: #FF0000):")

            rgb1 = color_converter(color1)
            rgb2 = color_converter(color2)

            mixed_color = mix_colors(rgb1, rgb2)
            mixed_color_hex = rgb_to_hex(mixed_color)
        except Exception:
            messagebox.showerror("ОШИБКА", "Неправильный формат цвета. Используйте RGB (255,0,0) или HEX (#ff0000).")
            continue

    # Window with final color
        display = tk.Toplevel()
        display.title("Смешанный цвет")
        display.geometry("400x400")
        display.configure(bg=mixed_color_hex)

    # Show information about the color
        tk.Label(
            display,
            text=f"Final color:\nRGB: {mixed_color}\nHEX: {mixed_color_hex}",
            bg=mixed_color_hex,
            fg="white" if sum(mixed_color) < 400 else "black",
            font=("cooper black", 16)
        ).pack(expand=True)

        display.mainloop()


if __name__ == "__main__":
    main()
