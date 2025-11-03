import requests
import tkinter as tk

window = tk.Tk()

def get_advice():

    url = 'https://api.adviceslip.com/advice'

    response = requests.get(url)

    data = response.json()

    text.delete('1.0', tk.END)

    text.insert(tk.END, data['slip']['advice'])




lbl = tk.Label(
    text= 'Advice',
    fg= 'black'
)

text = tk.Text(
    height= 10,
    width= 40,
    font= ('Arial', 20)

)

btn = tk.Button(
    text= 'Get Advice',
    command= get_advice
)

lbl.pack()
text.pack()
btn.pack()

window.mainloop()