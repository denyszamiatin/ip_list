from Tkinter import *
from get_ip_list import parse_ip, get_content
import ipdb
import get_whois

URL = 'https://www.colocall.net/uaix/prefixes.txt'


# commands
def _c_clean_output():
  out_text.configure(state=NORMAL)
  out_text.delete('1.0', END)
  out_text.configure(state=DISABLED)


def _text_output(text, lin_pos=END):
  out_text.configure(state=NORMAL)
  out_text.insert(lin_pos, text)
  out_text.configure(state=DISABLED)


def _c_updb():
  filename = ipdb.update_db(parse_ip(get_content(URL))[0:20])
  text = 'DB updated. File: ' + filename + '\n'
  _text_output(text)


def _c_search():
  entry = entry_str.get()
  if any(char.isdigit() for char in entry) or '.' in entry:
    lst = ipdb.search_in_db(entry)
    text = ipdb._get_latest_db_file() + '\n' + '\n'.join(lst) + '\n'
  else:
    text = 'Enter valid ip \n'
  _text_output(text, END)


def _c_getdb():
  lst = ipdb.search_in_db()
  text = 'Contents of: ' + ipdb._get_latest_db_file() + '\n' + ', '.join(lst) + '\n'
  _text_output(text)


def _c_whois():
  entry = entry_str.get()
  #text = '\n'.join(get_whois.get_whois_ip_data_list(entry))
  text = ''
  for i in get_whois.get_whois_ip_data_list(entry):
    text += i[0] + '\t' + i[1] + '\n'
  _text_output(text)

win = Tk()
# Root window conf
win.title("ipdb GUI")
win.resizable(height=FALSE, width=TRUE)
winbg = '#E3DCA8'
win.configure(bg=winbg)
win.geometry("900x700")

# Upper Frame
up_fr = Frame(win, bg=winbg)
entry_str = StringVar()
search_entry = Entry(up_fr, borderwidth=1, width=25, textvariable=entry_str).pack(side=LEFT, padx=(0, 5))
oksearch_bt = Button(up_fr, text="search ip", command=_c_search).pack(side=LEFT, padx=1)
whois_bt = Button(up_fr, text="whois", command=_c_whois).pack(side=LEFT, padx=1)

# Middle Frame Text Output
mid_fr = Frame(win, bg=winbg)
scroll = Scrollbar(mid_fr)
out_text = Text(mid_fr, yscrollcommand=scroll.set, bg='grey', spacing1=1, wrap=WORD, state=DISABLED)
out_text.bind("<Enter>", lambda e: out_text.focus())
scroll.configure(command=out_text.yview)
scroll.pack(side=RIGHT, anchor=CENTER, fill=Y)
out_text.pack(side=RIGHT, anchor=CENTER, fill=BOTH, expand=1, ipadx=5)

# Bottom Frame
bot_fr = Frame(win, relief=SUNKEN, bg=winbg)
exit_bt = Button(bot_fr, text="Exit", command=win.quit).pack(anchor=S, side=RIGHT, padx=(10, 0))
clean_bt = Button(bot_fr, text="Clean", command=_c_clean_output).pack(anchor=S, side=RIGHT, padx=1)
getdb_bt = Button(bot_fr, text="getdb", command=_c_getdb).pack(anchor=S, side=RIGHT, padx=1)
updb_bt = Button(bot_fr, text="update db", command=_c_updb).pack(anchor=S, side=RIGHT, padx=1)

# Frames layout
up_fr.pack(anchor=NW, fill=X, padx=10, pady=10)
mid_fr.pack(anchor=CENTER, fill=BOTH, padx=10, pady=(2, 5), expand=1)
bot_fr.pack(anchor=SE, fill=BOTH, padx=10, pady=5)

win.mainloop()

