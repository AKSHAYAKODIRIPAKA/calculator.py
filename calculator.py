import tkinter as tk

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")

        # Entry widget for the expression
        self.expression = tk.StringVar()
        self.entry = tk.Entry(root, textvariable=self.expression, font=('Arial', 20), bd=10, insertwidth=4, width=14, justify='right')
        self.entry.grid(row=0, column=0, columnspan=4)

        # Button layout
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            'C', '0', '=', '+'
        ]

        row_val = 1
        col_val = 0

        for button in buttons:
            tk.Button(root, text=button, padx=20, pady=20, font=('Arial', 15), command=lambda b=button: self.on_button_click(b)).grid(row=row_val, column=col_val)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

    def on_button_click(self, button):
        current_text = self.expression.get()

        if button == 'C':
            self.expression.set('')
        elif button == '=':
            try:
                result = eval(current_text)
                self.expression.set(result)
            except Exception as e:
                self.expression.set('Error')
        else:
            new_text = current_text + button
            self.expression.set(new_text)

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
