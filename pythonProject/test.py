from tkinter import *
import cx_Oracle as oci

window = Tk()

window.title('데브킹')
# window.geometry('540x960')
window.resizable(False, False)

top = Frame(window)
menu = Frame(window)
money = Frame(window)
bottom = Frame(window)

title = Label(top, text='TIOBE Index for May 2021').pack()


def addLanguage(id):
    conn = oci.connect('siat/siattiger@memoreform.com:1521/XE')
    cursor = conn.cursor()

    sql = 'select * from devking where id={}'.format(id)

    cursor.execute(sql)
    datas = cursor.fetchall()
    data = datas[0]

    state = True

    for i in range(0, 16):
        if data[1] == li_name.get(i):
            count = li_count.get(i)
            li_count.delete(i)
            li_count.insert(i, count + 1)
            state = False

    if state:
        li_name.insert(END, data[1])
        li_price.insert(END, data[2])
        li_count.insert(END, 1)

    print(l_total.cget('text'))
    # total = l_total['text']
    #
    # print(total)
    # int_total = int(total[:len(total) - 1])
    # l_total['text'] = str(int_total + (int(data[2])))
    cursor.close()
    conn.close()


Button(menu, text='C', width=14, height=7, command=lambda: addLanguage(1)).grid(row=0, column=0)
Button(menu, text='Python', width=14, height=7, command=lambda: addLanguage(2)).grid(row=0, column=1)
Button(menu, text='Java', width=14, height=7, command=lambda: addLanguage(3)).grid(row=0, column=2)
Button(menu, text='C++', width=14, height=7, command=lambda: addLanguage(4)).grid(row=0, column=3)

Button(menu, text='C#', width=14, height=7, command=lambda: addLanguage(5)).grid(row=1, column=0)
Button(menu, text='Visual Basic', width=14, height=7, command=lambda: addLanguage(6)).grid(row=1, column=1)
Button(menu, text='JavaScript', width=14, height=7, command=lambda: addLanguage(7)).grid(row=1, column=2)
Button(menu, text='Assembly language', width=14, height=7, command=lambda: addLanguage(8)).grid(row=1, column=3)

Button(menu, text='PHP', width=14, height=7, command=lambda: addLanguage(9)).grid(row=2, column=0)
Button(menu, text='SQL', width=14, height=7, command=lambda: addLanguage(10)).grid(row=2, column=1)
Button(menu, text='Ruby', width=14, height=7, command=lambda: addLanguage(11)).grid(row=2, column=2)
Button(menu, text='Classic Visual Basic', width=14, height=7, command=lambda: addLanguage(12)).grid(row=2, column=3)

Button(menu, text='R', width=14, height=7, command=lambda: addLanguage(13)).grid(row=3, column=0)
Button(menu, text='Groovy', width=14, height=7, command=lambda: addLanguage(14)).grid(row=3, column=1)
Button(menu, text='MATLAB', width=14, height=7, command=lambda: addLanguage(15)).grid(row=3, column=2)
Button(menu, text='Go', width=14, height=7, command=lambda: addLanguage(16)).grid(row=3, column=3)

li_name = Listbox(money)
li_name.grid(row=0, column=0)
li_price = Listbox(money)
li_price.grid(row=0, column=1)
li_count = Listbox(money)
li_count.grid(row=0, column=2)

l_total = Label(money, text='0').grid(row=1, column=2)


def chogihwa():
    li_name.delete(0, END)
    li_price.delete(0, END)
    li_count.delete(0, END)


Button(bottom, text='Clear', width=21, command=lambda: chogihwa()).grid(row=0, column=0)


def learn():
    conn = oci.connect('siat/siattiger@memoreform.com:1521/XE')
    cursor = conn.cursor()

    # chogihwa()


Button(bottom, text='Learn', width=21, command=lambda: learn()).grid(row=0, column=1)

top.pack()
menu.pack()
money.pack()
bottom.pack()
window.mainloop()