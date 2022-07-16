# ASSIGNMENT-7



# QUESTION-1
# GST CALCULATOR

from tkinter import *

def find_gst(): # function to calculate GST rate
    org_cost=int(cost_val.get()) # getting input of original cost and net price
    net_price=int(price_val.get())
    rate=(net_price-org_cost)*100/org_cost
    rate_val.insert(10, str(rate) + "%") # inserting GST rate in answer value

gui=Tk()
gui.title("GST Calculator")
gui.geometry("250x150")

cost=Label(gui, text="Original Cost: ") # variable for original cost
cost.grid(row=1, column=1)
price=Label(gui, text="Net Price: ") # variable for net price
price.grid(row=2, column=1)
rate=Label(gui, text="GST Rate: ") # variable for GST rate
rate.grid(row=4, column=1)

find=Button(gui, text="Find GST", command=find_gst) # button to find GST rate
find.grid(row=3, column=2)

cost_val=Entry(gui) # value for original cost
cost_val.grid(row=1, column=2)
price_val=Entry(gui) # value of net price
price_val.grid(row=2, column=2)
rate_val=Entry(gui) # value of GST rate
rate_val.grid(row=4, column=2)

gui.mainloop()
