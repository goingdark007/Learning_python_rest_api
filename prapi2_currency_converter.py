import requests
# imports tkinter gui
import tkinter as tk

# .Tk class creates a root window
window = tk.Tk()


# configures the row & column when its expanded and minimum size is 50 pixel
window.rowconfigure(0, weight= 1, minsize= 50)
window.columnconfigure([0, 1, 2], weight= 1, minsize = 50)

url = "https://api.fastforex.io/fetch-one"
query_params = {
    'api_key' : 'b92b0ae420-a151890833-t53fpj',
    'from'  : 'USD',
    'to' : 'BDT'
}

# Global variable to remember which entry was last typed in
last_edited = None

#This function runs whenever a key is pressed inside an Entry. It stores the entry widget
# (entry or entry_c) in last_edited
def set_last_edited(event):
    # global means modifying the global var not creating a local one for function
    global last_edited
    # event.widget tells us which widget triggered the event (either entry or entry_c)
    last_edited = event.widget

def convert(value):

    global last_edited

    if last_edited == entry_usd:

        usd_value = entry_usd.get()

        if usd_value:

            try:

                # float() converts the string to decimal number
                bdt_value = float(usd_value) * value
                # clears the entry widgets previous texts
                entry_bdt.delete(0, tk.END)
                # inserts the new value or updated value in the widget
                entry_bdt.insert(0, f"{bdt_value:.2f}")  # using f string :.2f takes two decimal value
                # if string is entered then ValueError happens and this code runs
            except ValueError:
                entry_bdt.delete(0, tk.END)
                # Clears previous text in the entry widget and inserts Error
                entry_bdt.insert(0, "Error")

    elif last_edited == entry_bdt:

        bdt_value = entry_bdt.get()

        if bdt_value:

            try:

                usd_value = float(bdt_value) / value
                entry_usd.delete(0, tk.END)
                entry_usd.insert(0, f"{usd_value:.2f}")
                # if string is entered then ValueError happens and this code runs
            except ValueError:
                entry_usd.delete(0, tk.END)
                # Clears previous text in the entry widget and inserts Error
                entry_usd.insert(0, "Error")
    

def get_convertion_rate():

    try:

        response = requests.get(url, params=query_params, timeout= 5)
        response.raise_for_status() # Raises an HTTPError for bad codes
        data = response.json()
        convertion_rate = data['result']['BDT']
        convert(convertion_rate)


    except requests.exceptions.HTTPError as errh:
        print("HTTP Error:", errh)

    except requests.exceptions.ConnectionError as errc:
        print("Connection Error:", errc)

    except requests.exceptions.Timeout as errt:
        print("Timeout Error:", errt)

    except requests.exceptions.RequestException as err:
        print("Error:", err)


# Creating a list to store the frames
frmList = []

# Creating a nested loop where i iterates 1 time and j iterates 3 times
for i in range(1):
    for j in range(3):
        #Creating a frame for each iteration of j, in total four frames created
        frame = tk.Frame(master=window,relief= "ridge", borderwidth=1)
        # Creating a 1 row/3 column grid and placing the frames in 0,0/0,1/0,2 cells
        frame.grid(row=i, column=j)
        # Adding each frames individually in the list
        frmList.append(frame)

# Creating an entry widget to take the input from user
entry_usd = tk.Entry(
    # master= means this widgets parent container is frmList[0] 0th index frame
    master= frmList[0],
    width= 10,
    font= ('Arial', 25),
    borderwidth= 1
)


# Creating a label widget to show the text `F
lbl_f = tk.Label(
    master= frmList[0],
    text= 'USD',
    height = 5,
    width = 3
)


# Creating a button widget to tap and start the program
btn_convert = tk.Button(
    master= frmList[1],
    text= '<-->',
    height = 4,
    width = 10,
    command= get_convertion_rate
)

entry_bdt = tk.Entry(
    master= frmList[2],
    width= 10,
    font= ('Arial', 25),
    borderwidth= 1
)

# Creating another label widget to show the output
lbl_c = tk.Label(
    master = frmList[2],
    text = 'BDT',
    height = 5,
    width = 3
)

# Binds the widgets to event function. <Key> = keyboard sensor: goes off whenever we type
# something inside the widget and <FocusIn> = attention sensor: goes off when the widget
# gains the user’s focus (clicked or tabbed into) & lastly it calls the event function which updates the last_edited
entry_usd.bind("<Key>", set_last_edited)
entry_bdt.bind("<Key>", set_last_edited)
entry_usd.bind("<FocusIn>", set_last_edited)
entry_bdt.bind("<FocusIn>", set_last_edited)

# Placing the widgets in the frame to show up
# side= tk.LEFT / "left" parameter is used to stack widgets in a frame at the left side by default it stacks at top
entry_usd.pack(side= "left")
lbl_f.pack()
# padx= and pady= to give a lil bit of space between button widget and frame border both horizontally & vertically
btn_convert.pack(padx= 5, pady= 5)
entry_bdt.pack(side= 'left')
lbl_c.pack()


# .mainloop() runs the gui
window.mainloop()
