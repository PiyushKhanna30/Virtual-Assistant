import tkinter
import wikipedia
import wolframalpha
import pyttsx3

engine = pyttsx3.init()

def result_window(event=None):
    def destroy_result_window(event=None):
        query_result_window.destroy()
    query_result_window=tkinter.Toplevel()
    query_result_window.minsize(400,400)
    query_result_window.maxsize(400,400)
    tkinter.Label(query_result_window,bg="#95a5a6",height=400,width=400).place(x=0,y=0)
    result = tkinter.Text(query_result_window,height=18,width=47,bg="#d0d3d4")
    result.place(x=10,y=40)
    user_input=query_input.get()
    try:
        try:
            app_id = "******-**********"            #Your app id
            client = wolframalpha.Client(app_id)
            res = client.query(user_input)
            speak_this = next(res.results).text
            answere=speak_this
            clear_text()
        except: 
            speak_this="here is what i found"
            answere = wikipedia.summary(user_input,sentences=2)
            clear_text()
    except:
        speak_this="""Some error occured. 
        Check if you have filled the field.
        Try to use less and meaningful words."""
    result.insert(tkinter.END, answere)
    engine.say(speak_this)  
    engine.runAndWait()
    tkinter.Button(query_result_window,text="Close",command=query_result_window.destroy,font=("Comic Sans MS", 10), width = 8,bg="#808b96").place(x=310,y=350)
    query_result_window.bind('<Escape>', destroy_result_window)

def destroy_root(event=None):
    root.destroy()
def clear_text():
    query_input.delete(0,'end')

root = tkinter.Tk()
root.title("Virtual Assistant")
logo=tkinter.PhotoImage(file="Virtual-Assistant.gif")
root.minsize(400,400)
root.maxsize(400,400)
root.geometry("400x400")
logo_va=tkinter.Label(root,image=logo,height=400,width=400,bg="#95a5a6").place(x=0,y=0)
query_label=tkinter.Label(root, text="Hey! How may I help you?",font=("Comic Sans MS", 12),bg="#d0d3d4")
query_label.place(x=0,y=100)
query_input=tkinter.Entry(root,font=("Comic Sans MS", 12),bg="#d0d3d4")
query_input.place(x=200,y=135)
tkinter.Button(root,text="Clear",command=clear_text,font=("Comic Sans MS", 10), width = 8,bg="#808b96").place(x=90,y=350)
tkinter.Button(root,text="Search",command=result_window,font=("Comic Sans MS", 10), width = 8,bg="#808b96").place(x=230,y=350)
root.bind('<Return>', result_window)
root.bind('<Escape>', destroy_root)
root.mainloop()
