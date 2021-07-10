from tkinter import *
from scraper import news
import webbrowser


def callback(url):
    webbrowser.open_new(url)

fgcolor = 'grey'
bgcolor = 'black'

root = Tk()
root.title("Hacker News Top Ten")
root.configure(background=bgcolor)
i = 0
font = ('Arial', 20)

for article in news:
    lbl = Label(root, text="Title: ", font=font, fg=fgcolor, bg=bgcolor)
    lbl.grid(row=i, column=0, sticky=W)
    lbl = Label(root, text=article['title'], fg="blue", cursor="hand2", font=font, bg=bgcolor)
    lbl.grid(row=i, column=1, sticky=W)
    lbl.bind("<Button-1>", lambda e, url=article['link']: callback(url))
    lbl = Label(root, text="Votes: " + str(article['votes']), font=font, fg=fgcolor, bg=bgcolor)
    lbl.grid(row=i + 1, column=0)
    i += 2

lbl.config(bg="black", fg="grey")
root.mainloop()