from tkinter import *
from tkinter import ttk
####

class Calculator():

    #store value
    current_value = 0.0
    solution = 0.0
    entered_value = 0.0

    #Booleans to store last clicked operation
    add_bool = False
    sub_bool = False
    mul_bool = False
    div_bool = False

    eq_bool = False

    #Functions
    def button_press(self, value):
        #get current(old) value
        self.entered_value = self.number_entry.get()
        #append the entered number
        self.entered_value += value
        #delete old value
        self.number_entry.delete(0, END)
        #post new value 
        self.number_entry.insert(0, self.entered_value)


    #check if string is float
    def isfloat(self, str_value):
        try:
            float(str_value)
            return True
        except ValueError:
            return False

    def math_button_press(self, operation):
        if self.isfloat(str(self.number_entry.get())):
            self.add_bool = False
            self.sub_bool = False
            self.mul_bool = False
            self.div_bool = False
            self.eq_bool = False
            
            self.current_value = float(self.entry_value.get())
            
            if operation == '/':
                self.div_bool = True

            elif operation == '*':
                self.mul_bool = True

            elif operation == '+':
                self.add_bool = True

            elif operation == '-':
                self.sub_bool = True

            self.number_entry.delete(0, END)

    def equal_button_press(self):
        if self.eq_bool == True:
            if self.add_bool:
                self.solution += float(self.entered_value)
            elif self.sub_bool:
                self.solution -= float(self.entered_value)
            elif self.div_bool:
                self.solution = (self.solution/float(self.entered_value))
            elif self.mul_bool:    
                self.solution = (self.solution*float(self.entered_value))          
            
            self.number_entry.delete(0, END)
            self.number_entry.insert(0, self.solution)

        elif self.div_bool or self.mul_bool or self.add_bool or self.sub_bool == True:
            if self.add_bool:
                self.solution = self.current_value + float(self.entry_value.get())
                self.eq_bool = True
            elif self.sub_bool:
                self.solution = self.current_value - float(self.entry_value.get())
                self.eq_bool = True
            elif self.div_bool:
                self.solution = self.current_value / float(self.entry_value.get())
                self.eq_bool = True
            elif self.mul_bool:    
                self.solution = self.current_value * float(self.entry_value.get())
                self.eq_bool = True

            self.number_entry.delete(0, END)
            self.number_entry.insert(0, self.solution)

    
    def clear_button_press(self):
        self.current_value = 0.0
        self.solution = 0.0
        self.entered_value = 0.0
        self.number_entry.delete(0, END)

    #GUI
    def __init__(self, root):

        self.entry_value = StringVar(root, value='')

        root.title = 'Pocket Calculator'
        root.geometry("332x152")
        root.resizable(
            width=False, 
            height=False
            )
        style = ttk.Style()
        style.configure(
            'TButton',
            font='Verdana 12',
            )
        style.configure(
            'TEntry',
            font='Serif 18',
            ) 
        #Entry/Display Window  
        self.number_entry = ttk.Entry(
            root,
            textvariable=self.entry_value, width='35'
            )
        self.number_entry.grid(row=0, columnspan=4)

        #Integer Buttons
        self.button_1 = ttk.Button(
            root, text='1', command=lambda: self.button_press('1')
        ).grid(row=4, column=0)
        self.button_2 = ttk.Button(
            root, text='2', command=lambda: self.button_press('2')
        ).grid(row=4, column=1)
        self.button_3 = ttk.Button(
            root, text='3', command=lambda: self.button_press('3')
        ).grid(row=4, column=2)

        self.button_4 = ttk.Button(
            root, text='4', command=lambda: self.button_press('4')
        ).grid(row=3, column=0)
        self.button_5 = ttk.Button(
            root, text='5', command=lambda: self.button_press('5')
        ).grid(row=3, column=1)
        self.button_6 = ttk.Button(
            root, text='6', command=lambda: self.button_press('6')
        ).grid(row=3, column=2)

        self.button_7 = ttk.Button(
            root, text='7', command=lambda: self.button_press('7')
        ).grid(row=2, column=0)
        self.button_8 = ttk.Button(
            root, text='8', command=lambda: self.button_press('8')
        ).grid(row=2, column=1)
        self.button_9 = ttk.Button(
            root, text='9', command=lambda: self.button_press('9')
        ).grid(row=2, column=2)

        self.button_0 = ttk.Button(
            root, text='0', command=lambda: self.button_press('0')
        ).grid(row=5, column=0, columnspan=2)

        #Operations Buttons
        self.button_div = ttk.Button(
            root, text='÷', command=lambda: self.math_button_press('/')
        ).grid(row=1, column=3)        
        self.button_mul = ttk.Button(
            root, text='x', command=lambda: self.math_button_press('*')
        ).grid(row=2, column=3)   
        self.button_sub = ttk.Button(
            root, text='-', command=lambda: self.math_button_press('-')
        ).grid(row=3, column=3)
        self.button_add = ttk.Button(
            root, text='+', command=lambda: self.math_button_press('+')
        ).grid(row=4, column=3)
        
        self.button_eq = ttk.Button(
            root, text='=', command=lambda: self.equal_button_press()
        ).grid(row=5, column=3)
        
        self.button_ac = ttk.Button(
            root, text='AC', command=lambda: self.clear_button_press(),
        ).grid(row=1, column=0)                                           


root = Tk()
calculator = Calculator(root)
root = mainloop()
