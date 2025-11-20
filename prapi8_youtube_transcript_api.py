import requests
import tkinter as tk

url = 'https://www.youtube-transcript.io/api/transcripts'

headers = {
    "Authorization" : "Basic 691eebf81cd96631354e00c9",
    "Content-Type" : "application/json"
}

body = {
    "ids" : ['2t6Bt04EyLw']
}

def call_api():

    try:

        response = requests.post(url, headers=headers, json=body)
        if response.status_code == 200:
            data = response.json()
            transcript = data[0]["text"]
            text.insert(tk.END, transcript)
        else:
            print('Error Status-code', response.status_code)

    except requests.exceptions.RequestException as err:

        print('Error', err)

def save_transcript():

    top = tk.Toplevel(master=window)

    top.title('Save Transcript')


window = tk.Tk()

lbl  = tk.Label(
    master= window,
    text= 'Youtube Transcript',
    bg= 'white',
    fg= 'black',
)

text = tk.Text(master= window,)

btn = tk.Button(
    master= window,
    text= 'Get Transcript',
    command= call_api
)

save_btn = tk.Button(
    master= window,
    text = 'Save',
    command= save_transcript
)

lbl.pack()
text.pack()
btn.pack()
save_btn.pack()


window.mainloop()
