from tkinter import *
from tkinter import ttk

window = Tk()
window.resizable(width=False, height=False)
window.geometry('1500x650')  
window.title("Car rental")

#Left frame
left_frame = Frame(window, width= 250, height = 700)
left_frame.propagate(0)
left_frame.pack(side=LEFT, padx = 2)

#LabelFrame №1
labelframe_1 = LabelFrame(left_frame, text="Requests", padx=15, pady=10)
labelframe_1.pack(padx = 2, pady = 7, anchor = CENTER, fill = X)

request_button_1 = Button(labelframe_1, text="Human Resources Department", height = 1, width = 28, command = None)  
request_button_1.pack(pady = 2, ipady=3, anchor = CENTER, fill = X)

request_button_2 = Button(labelframe_1, text="Car park", command = None)  
request_button_2.pack(pady = 2, ipady=3, anchor = CENTER, fill = X)

request_button_3 = Button(labelframe_1, text="Rented cars", command = None)  
request_button_3.pack(pady = 2, ipady=3, anchor = CENTER, fill = X)

def add_client():

    window_2 = Toplevel()
    window_2.resizable(width=False, height=False)
    window_2.geometry('1000x545')
    window_2.title("New client")

    #Upper frame
    upper_frame = Frame(window_2, width= 1000, height = 250)
    upper_frame.propagate(0)
    upper_frame.pack(side=TOP, padx = 2)

    #LabelFrame TOP
    labelframe_client = LabelFrame(upper_frame, text="Personal Information", padx=15, pady=10)
    labelframe_client.pack(padx = 2, pady = 7, anchor = CENTER, fill = X)

    #Frame TOP left
    labelframe_client_left = Frame(labelframe_client, width= 470, height = 250)
    labelframe_client_left.propagate(0)
    labelframe_client_left.pack(side=LEFT, padx = 2)

    label_1_top = Label(labelframe_client_left, text = "Full name")
    label_1_top.pack(anchor = W)

    full_name = Entry(labelframe_client_left)
    full_name.pack(fill=X, expand=True)

    label_2_top = Label(labelframe_client_left, text = "Gender")
    label_2_top.pack(anchor = W)

    combo_filter = ttk.Combobox(labelframe_client_left, values=["Male", "Female"])
    combo_filter.pack(fill=X, expand=True)

    label_2_top = Label(labelframe_client_left, text = "Date of birth (Format: Year-Month-Day)")
    label_2_top.pack(anchor = W)

    birth_date = Entry(labelframe_client_left)
    birth_date.pack(fill=X, expand=True)

    #Frame TOP right
    labelframe_client_right = Frame(labelframe_client, width= 470, height = 250)
    labelframe_client_right.propagate(0)
    labelframe_client_right.pack(side=RIGHT, padx = 2)

    label_3_top = Label(labelframe_client_right, text = "Address")
    label_3_top.pack(anchor = W)

    address = Entry(labelframe_client_right)
    address.pack(fill=X, expand=True)

    label_4_top = Label(labelframe_client_right, text = "Telephone number (Format: +7(xxx)-xxx-xx-xx)")
    label_4_top.pack(anchor = W)

    phone_number = Entry(labelframe_client_right)
    phone_number.pack(fill=X, expand=True)

    label_5_top = Label(labelframe_client_right, text = "Passport data (Format: series, number, no spaces)")
    label_5_top.pack(anchor = W)

    passport_data = Entry(labelframe_client_right)
    passport_data.pack(fill=X, expand=True)

    #Bottom frame
    bottom_frame = Frame(window_2, width= 1000, height = 250)
    bottom_frame.propagate(0)
    bottom_frame.pack(padx = 2)

    #LabelFrame BOTTOM
    labelframe_rent = LabelFrame(bottom_frame, text="Rent", padx=15, pady=10)
    labelframe_rent.pack(padx = 2, pady = 7, anchor = CENTER, fill = X)

    #Frame BOTTOM left
    labelframe_rent_left = Frame(labelframe_rent, width= 470, height = 250)
    labelframe_rent_left.propagate(0)
    labelframe_rent_left.pack(side=LEFT, padx = 2)

    label_1_bottom = Label(labelframe_rent_left, text = "Vehicle")
    label_1_bottom.pack(anchor = W)

    combo_filter_rent = ttk.Combobox(labelframe_rent_left, values = None)
    combo_filter_rent.bind("<<ComboboxSelected>>", None)
    combo_filter_rent.pack(fill=X, expand=True)

    label_2_bottom = Label(labelframe_rent_left, text = "Date of Issue (Format: Year-Month-Day)")
    label_2_bottom.pack(anchor = W)

    issue_date = Entry(labelframe_rent_left)
    issue_date.pack(fill=X, expand=True)

    label_3_bottom = Label(labelframe_rent_left, text = "Rental period (in days)")
    label_3_bottom.pack(anchor = W)

    days = Entry(labelframe_rent_left, textvariable = None)
    days.pack(fill=X, expand=True)

    label_4_bottom = Label(labelframe_rent_left, text = "Additional Service №1 (Optional)")
    label_4_bottom.pack(anchor = W)

    combo_filter2_rent = ttk.Combobox(labelframe_rent_left, values = None)
    combo_filter2_rent.bind("<<ComboboxSelected>>", None)
    combo_filter2_rent.pack(fill=X, expand=True)

    #Frame BOTTOM right
    labelframe_rent_right = Frame(labelframe_rent, width= 470, height = 250)
    labelframe_rent_right.propagate(0)
    labelframe_rent_right.pack(side=RIGHT, padx = 2)

    label_5_bottom = Label(labelframe_rent_right, text = "Additional Service №2 (Optional)")
    label_5_bottom.pack(anchor = W)

    combo_filter3_rent = ttk.Combobox(labelframe_rent_right, values = None)
    combo_filter3_rent.bind("<<ComboboxSelected>>", None)
    combo_filter3_rent.pack(fill=X, expand=True)

    label_5_bottom = Label(labelframe_rent_right, text = "Additional Service №3 (Optional)")
    label_5_bottom.pack(anchor = W)

    combo_filter4_rent = ttk.Combobox(labelframe_rent_right, values = None)
    combo_filter4_rent.bind("<<ComboboxSelected>>", None)
    combo_filter4_rent.pack(fill=X, expand=True)

    label_6_bottom = Label(labelframe_rent_right, text = "Rent price")
    label_6_bottom.pack(anchor = W)

    rental_price = Entry(labelframe_rent_right)
    rental_price.pack(fill=X, expand=True)
    rental_price.config(state='readonly')

    label_7_bottom = Label(labelframe_rent_right, text = "Payment State")
    label_7_bottom.pack(anchor = W)

    combo_filter5_rent = ttk.Combobox(labelframe_rent_right, values=["Paid", "Not paid"])
    combo_filter5_rent.pack(fill=X, expand=True)

    confirm_button = Button(window_2, text="Confirm entered data", bg = "gray90", command = None)  
    confirm_button.pack(padx = 5, pady = 4, ipady = 7, side = BOTTOM, anchor = CENTER, fill = X)

request_button_4 = Button(labelframe_1, text="New client", command = add_client)  
request_button_4.pack(pady = 2, ipady=3, anchor = CENTER, fill = X)

#LabelFrame №2
labelframe_2 = LabelFrame(left_frame, text="Filters", padx=15, pady=10)
labelframe_2.pack(padx = 2, pady = 5, anchor = CENTER, fill = X)

label_1 = Label(labelframe_2, text = "Employees of individual positions")
label_1.pack(anchor = CENTER, fill = X)

#ComboBox №1
combo_filter_1 = ttk.Combobox(labelframe_2, values=["Mechanic", "Accountant", "Purchasing Manager", "Sales Manager",
"Advertising and PR Specialist", "Car Rental Director", "Rental Point Manager"])

combo_filter_1.bind("<<ComboboxSelected>>", None)
combo_filter_1.pack(ipady=2, anchor = CENTER, fill = X)

label_2 = Label(labelframe_2, text = "Cars of individual \nmodels")
label_2.pack(anchor = CENTER, fill = X)

combo_filter_2 = ttk.Combobox(labelframe_2, values=["Audi A6", "Audi A8", "BMW 5 series", "BMW 7 series", "Mercedes-Benz E-Class",
"Mercedes-Benz S-Class", "Toyota Camry", "Toyota Alphard", "Lexus ES350", "Lexus LX570"])

combo_filter_2.bind("<<ComboboxSelected>>", None)
combo_filter_2.pack(ipady=2, anchor = CENTER, fill = X)

label_3 = Label(labelframe_2, text = "Cars that are\n and are not for rent")
label_3.pack(anchor = CENTER, fill = X)

combo_filter_3 = ttk.Combobox(labelframe_2, values=["Rental Cars", "Not Rented Cars"])

combo_filter_3.bind("<<ComboboxSelected>>", None)
combo_filter_3.pack(ipady=2, anchor = CENTER, fill = X)

label_4 = Label(labelframe_2, text = "Paid and unpaid\nrental cars")
label_4.pack(anchor = CENTER, fill = X)

combo_filter_4 = ttk.Combobox(labelframe_2, values=["Paid cars", "Not paid cars"])

combo_filter_4.bind("<<ComboboxSelected>>", None)
combo_filter_4.pack(ipady=2, anchor = CENTER, fill = X)

label_5 = Label(labelframe_2, text = "Vehicles issued and\nreturned on a specific date")
label_5.pack(anchor = CENTER, fill = X)

request_button_4 = Button(labelframe_2, text="Date selection", command = None)  
request_button_4.pack(pady = 2, ipady=3, anchor = CENTER, fill = X)

#Right frame
Right_frame = Frame(window, width= 1235, height = 527)
Right_frame.propagate(0)
Right_frame.pack(padx = 2, pady = 15, side=TOP)

#Table
table = ttk.Treeview(Right_frame, show="headings")
table.pack(side="top", fill="both", expand=True)

#Scroll bar
scroll_panel = ttk.Scrollbar(Right_frame, orient = HORIZONTAL, command = table.xview)
table.configure(xscrollcommand = scroll_panel.set)
scroll_panel.pack(side="bottom", fill="x")

window.mainloop()