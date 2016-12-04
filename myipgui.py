from Tkinter import *
from get_ip_list import parse_ip, get_content
import ipdb

URL = 'https://www.colocall.net/uaix/prefixes.txt'


# commands
def _c_output(text):
  out_text.insert(END, text)
  out_text.insert(END, '\n\n')


def _c_updb():
  filename = ipdb.update_db(parse_ip(get_content(URL))[0:20])
  text = 'DB updated. File: ' + filename + '\n'
  _c_output(text)


def _c_search():
  entry = entry_str.get()
  if any(char.isdigit() for char in entry) or '.' in entry:
    lst = ipdb.search_in_db(entry)
    text = ipdb._get_latest_db_file() + '\n' + '\n'.join(lst)
  else:
    text = 'Enter valid ip'
  _c_output(text)


def _c_getdb():
  lst = ipdb.search_in_db()
  text = ipdb._get_latest_db_file() + '\n' + '\n'.join(lst)
  _c_output(text)


def _clean_output():
  out_text.delete('1.0', END)


win = Tk()
# Root windows conf
win.title("ipdb GUI")
win.resizable(height=FALSE, width=TRUE)
winbg = '#E3DCA8'
win.configure(bg=winbg)
win.geometry("900x700")

# Upper Frame
up_fr = Frame(win, bg=winbg)
entry_str = StringVar()
search_entry = Entry(up_fr, borderwidth=1, width=15, textvariable=entry_str).pack(side=LEFT, padx=(0, 5))

oksearch_bt = Button(up_fr, text="Ok", command=_c_search).pack(side=LEFT, padx=1)
getdb_bt = Button(up_fr, text="getdb", command=_c_getdb).pack(side=LEFT, padx=1)
updb_bt = Button(up_fr, text="update db", command=_c_updb).pack(side=LEFT)

# Middle Frame Text Output
mid_fr = Frame(win, bg=winbg)
out_text = Text(mid_fr, bg='grey')
scroll = Scrollbar(out_text)
out_text.configure(yscrollcommand=scroll.set, state=NORMAL)
out_text.pack(anchor=CENTER, fill=BOTH, expand=1)
scroll.pack(side=RIGHT, fill=Y)

# Bottom Frame
bot_fr = Frame(win, relief=SUNKEN, bg='#EFFCA8')
exit_bt = Button(bot_fr, text="Exit", command=win.quit).pack(anchor=S, side=RIGHT)
clean_bt = Button(bot_fr, text="Clean", command=_clean_output).pack(anchor=S, side=RIGHT)

# Frames layout
up_fr.pack(anchor=NW, fill=X, padx=10, pady=10)
mid_fr.pack(anchor=CENTER, fill=BOTH, padx=10, pady=(2, 5), expand=1)
bot_fr.pack(anchor=SE, fill=BOTH, padx=10, pady=5)

win.mainloop()

