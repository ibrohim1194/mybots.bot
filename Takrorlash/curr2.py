import tkinter as tk
 
def convert():
    try:
        som = ent_r.get()
        if var.get() == 0:
            res = float(som) / 68
            lbl_result["text"] = f"{round(res, 2)} \N{DOLLAR SIGN}"
        elif var.get() == 1:
            res = float(som) / 87
            lbl_result["text"] = f"{round(res, 2)} \N{EURO SIGN}"
        elif var.get() == 2:
            res = float(som) / 100
            lbl_result["text"] = f"{round(res, 2)} \N{POUND SIGN}"
    except ValueError:
        ent_r.insert(0, "0.0")
 
window = tk.Tk()
window.title("Valyutalar kursi")
 
frm_entry = tk.Frame(master = window)
ent_r = tk.Entry(master = frm_entry, width = 10)
lbl_r = tk.Label(master = frm_entry, text = "RUB")
 
ent_r.grid(row = 0, column = 0, sticky = "e")
lbl_r.grid(row = 0, column = 1, sticky = "w")
 
btn_convert = tk.Button(master = window, text = "O'zgartirish", command = convert)
lbl_result = tk.Label(master = window)
 
var = tk.IntVar()
var.set(0)
 
rad_fld = tk.Frame(master = window)
r1 = tk.Radiobutton(master = rad_fld, text = f"\N{DOLLAR SIGN}", variable = var, value = 0)
r2 = tk.Radiobutton(master = rad_fld, text = f"\N{EURO SIGN}", variable = var, value = 1)
r3 = tk.Radiobutton(master = rad_fld, text = f"\N{POUND SIGN}", variable = var, value = 2)
 
r1.grid(row = 0, column = 0)
r2.grid(row = 0, column = 1)
r3.grid(row = 0, column = 2)
 
frm_entry.grid(row = 0, column = 0, padx = 10)
btn_convert.grid(row = 0, column = 1, pady = 10)
lbl_result.grid(row = 0, column = 2, padx = 10)
rad_fld.grid(row = 1, column = 0)
 
window.mainloop()