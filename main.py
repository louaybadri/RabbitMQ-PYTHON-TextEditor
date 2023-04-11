import tkinter as tk
import const as CONSTS
import read_logic
import send_logic


def update_state(master, text1, text2):
    print("updating")
    msg1 = read_logic.get_value(CONSTS.SECTION1Q)
    # msg2 = read_logic.get_value()
    text1.config(state=tk.NORMAL)
    text1.delete("1.0", tk.END)
    text1.insert("1.0", msg1)
    text1.config(state=tk.DISABLED)
    # master.after(1000,update_state)
    # text2.config(state=tk.NORMAL)
    # text2.delete("1.0", tk.END)
    # text2.insert("1.0", msg)
    # text2.config(state=tk.DISABLED)


def on_sub(msg, master, text_area):
    print(msg)
    print("TEXT " + read_logic.get_all_value(CONSTS.SECTION1TEXT))
    text_area.config(state=tk.NORMAL)
    text_area.delete("1.0", tk.END)
    text_area.insert("1.0", msg)
    text_area.config(state=tk.DISABLED)
    while not read_logic.is_empty(CONSTS.SECTION1TEXT):
        read_logic.read_ack(CONSTS.SECTION1TEXT)
    send_logic.send(CONSTS.SECTION1TEXT, msg)
    close(master)


def close(master):
    read_logic.read_ack(CONSTS.SECTION1Q)
    master.destroy()


def open_edit_section(text_area):
    edit = tk.Tk()
    edit.title("Edit Section")
    edit_label = tk.Label(edit, text="Edit section 1:")
    edit_label.grid(row=0, column=0)
    edit_text = tk.Text(edit, height=5, width=30)
    edit_text.grid(row=1, column=0)
    edit_text.insert(tk.END, read_logic.get_value(CONSTS.SECTION1TEXT))
    submit_button2 = tk.Button(edit, text="Submit",
                               command=lambda: on_sub(edit_text.get("1.0", tk.END), edit, text_area))
    submit_button2.grid(row=2, column=0)
    edit.protocol("WM_DELETE_WINDOW", lambda: close(edit))
    edit.mainloop()


def cant_access():
    ca = tk.Tk()
    ca.title("Error")
    ca_label = tk.Label(ca, text="This Section is reserved")
    ca_label.grid(row=0, column=0)
    exit_button = tk.Button(ca, text="Return", command=lambda: print("Hithere"))
    exit_button.grid(row=1, column=1)
    ca.mainloop()


def submit1():
    edit = tk.Tk()
    edit.title("Edit Section")
    edit_label = tk.Label(edit, text="Section 1:")
    edit_label.grid(row=0, column=0)
    edit_text = tk.Text(edit, height=5, width=30)
    edit_text.grid(row=0, column=1)
    edit.mainloop()


def section1_logic(text_area):
    if read_logic.is_empty(CONSTS.SECTION1Q):
        send_logic.send(CONSTS.SECTION1Q, "USED")
        open_edit_section(text_area)
    else:
        cant_access()


def submit2():
    print("submit2")


def main_screen():
    window = tk.Tk()
    window.title("Two Sections App")
    section1_label = tk.Label(window, text="Section 1:")
    section1_label.grid(row=0, column=0)
    section2_label = tk.Label(window, text="Section 2:")
    section2_label.grid(row=1, column=0)
    section1_text = tk.Text(window, height=5, width=30)
    section1_text.insert(tk.END, read_logic.get_all_value(CONSTS.SECTION1TEXT))
    section1_text.config(state=tk.DISABLED)
    section1_text.grid(row=0, column=1)
    section2_text = tk.Text(window, height=5, width=30)
    section2_text.config(state=tk.DISABLED)
    section2_text.grid(row=1, column=1)
    submit_button = tk.Button(window, text="Submit", command=lambda: section1_logic(section1_text))
    submit_button.grid(row=0, column=3)
    submit_button2 = tk.Button(window, text="Submit", command=submit2)
    submit_button2.grid(row=1, column=3)
    window.mainloop()


send_logic.declare_queue(CONSTS.SECTION1TEXT)
send_logic.declare_queue(CONSTS.SECTION1Q)
main_screen()
