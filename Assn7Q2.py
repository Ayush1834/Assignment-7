# QUESTION-2
# CALENDAR

from tkinter import *
import calendar

def show_cal(): # function to display calendar
    cal=Tk()
    cal.title("CALENDAR")
    cal.geometry("500x600")

    fetch_year=int(year_val.get()) # gets input of year
    cal_content=calendar.calendar(fetch_year) # fetches calendar of input year
    cal_year=Label(cal, text=cal_content)
    cal_year.grid(row=5, column=1)

    cal.mainloop()


cal_year=Tk()
cal_year.title("Calendar")
cal_year.geometry("250x150")

year=Label(cal_year, text="Enter Year: ")
year.grid(row=1, column=1)
year_val=Entry(cal_year) # takes input of year from user
year_val.grid(row=2, column=1)

show=Button(cal_year, text="Show Calendar", command=show_cal) # button to show year
show.grid(row=3, column=1)

cal_year.mainloop()


