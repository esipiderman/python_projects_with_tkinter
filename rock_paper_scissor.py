import tkinter
from random import randint

win = tkinter.Tk()

select = {
    1:"rock",
    2:"scissors",
    3:"paper"
}
def stone():
    com = randint(1,3)
    lbl["text"] = "computer choose : " + select[com]
    if com == 2:
        lbl_result_user["text"] = int(lbl_result_user["text"]) + 1
    elif com == 3:
        lbl_result_com["text"] = int(lbl_result_com["text"]) + 1

def scissor():
    com = randint(1,3)
    lbl["text"] = "computer choose : " + select[com]
    if com == 3:
        lbl_result_user["text"] = int(lbl_result_user["text"]) + 1
    elif com == 1:
        lbl_result_com["text"] = int(lbl_result_com["text"]) + 1

def paper():
    com = randint(1,3)
    lbl["text"] = "computer choose : " + select[com]
    if com == 1:
        lbl_result_user["text"] = int(lbl_result_user["text"]) + 1
    elif com == 2:
        lbl_result_com["text"] = int(lbl_result_com["text"]) + 1
    
def reset():
    lbl_result_com["text"] = 0
    lbl_result_user["text"] = 0
    lbl["text"] = "choose"

win.title("rock scissor paper")
win.minsize(400, 400)
win.rowconfigure([0, 1], weight=1)
win.columnconfigure(0, weight=1)

lbl = tkinter.Label(master=win, text="choose", font=("None", 20, "bold"), background="black",
                foreground="white", height=5)
lbl.grid(row=0, column=0, sticky="nwe")

frm = tkinter.Frame(master=win, height=100, background="red")
frm.rowconfigure(0, weight=1)
frm.columnconfigure([0, 1, 2], weight=1)

btn1 = tkinter.Button(master=frm, text="rock", height=3,font=("None", 14, "bold"),
            command=stone).grid(row=0, column=0, sticky="nwes", padx = 2,pady = 3)
btn2 = tkinter.Button(master=frm, text="scissors", height=3,font=("None", 14, "bold"),
            command=scissor).grid(row=0, column=1, sticky="nwes", padx = 2,pady = 3)
btn3 = tkinter.Button(master=frm, text="paper", height=3,font=("None", 14, "bold"),
            command=paper).grid(row=0, column=2, sticky="nwes", padx = 2,pady = 3)

frm.grid(row=1, column=0, sticky="wen")

frm_result = tkinter.Frame(master=win, height=200)
frm_result.rowconfigure([0, 1], weight = 1)
frm_result.columnconfigure([0, 1], weight = 1)

lbl_result_name_user = tkinter.Label(master=frm_result, text="your score",
            relief="ridge").grid(row = 0, column = 0, sticky="nswe")
lbl_result_name_com = tkinter.Label(master=frm_result, text="computer score",
            relief="ridge").grid(row = 0, column = 1, sticky="nswe")

lbl_result_user = tkinter.Label(master=frm_result, text="0", background="blue", foreground="white", height=3,
            font=("None", 40, "bold"))
lbl_result_user.grid(row=1,column=0,sticky="nwes")
lbl_result_com = tkinter.Label(master=frm_result, text="0", background="red", foreground="white", height=3,
            font=("None", 40, "bold"))
lbl_result_com.grid(row=1,column=1,sticky="nwes")

frm_result.grid(row=2, column=0, sticky="wen")

btn_reset = tkinter.Button(master=win, text="reset", font=("None", 18, "bold"), 
            relief="ridge", command=reset).grid(row=3, column=0, sticky="nswe")

win.mainloop()