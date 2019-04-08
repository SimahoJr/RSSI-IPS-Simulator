import tkinter
from dist import Distance
from numbers import Numbers
from position import Position

with open("copy1.txt", "w") as file:
    file.write("Actual          Estimated")
    file.write("\n")


def hi():
    tr1 = Distance(ref1.get(), entry4.get()).distance()
    tr2 = Distance(ref2.get(), entry4.get()).distance()
    tr3 = Distance(ref3.get(), entry4.get()).distance()
    tr4 = Distance(ref4.get(), entry4.get()).distance()

    tt1 = Distance(ref1.get(), entry5.get()).distance()
    tt2 = Distance(ref2.get(), entry5.get()).distance()
    tt3 = Distance(ref3.get(), entry5.get()).distance()
    tt4 = Distance(ref4.get(), entry5.get()).distance()

    # RX
    rx1 = Numbers(int(entry1.get())*1e6, int(entry.get()), 0, 1, int(entry3.get())*10, 1, tr1, 1)
    rx2 = Numbers(int(entry1.get())*1e6, int(entry.get()), 0, 1, int(entry3.get())*10, 1, tr2, 1)
    rx3 = Numbers(int(entry1.get())*1e6, int(entry.get()), 0, 1, int(entry3.get())*10, 1, tr3, 1)
    rx4 = Numbers(int(entry1.get())*1e6, int(entry.get()), 0, 1, int(entry3.get())*10, 1, tr4, 1)

    # Diff Actual - current
    diff1 = rx1.path_loss() - rx1.tag_tag(tt1)
    diff2 = rx2.path_loss() - rx2.tag_tag(tt2)
    diff3 = rx3.path_loss() - rx3.tag_tag(tt3)
    diff4 = rx4.path_loss() - rx4.tag_tag(tt4)


    # Diff Sum
    sum1 = diff1 + diff2 + diff3 + diff4+2

    # Weight
    w1 = diff1 / sum1
    w2 = diff2 / sum1
    w3 = diff3 / sum1
    w4 = diff4 / sum1

    # Position
    halo = Position(ref1.get(), ref2.get(), ref3.get(), ref4.get(), w1, w2, w3, w4).mahala()
    entry7.delete(0, tkinter.END)
    entry7.insert(0, halo)
    (x, y, z) = halo

    with open("copy1.txt", "a") as file:
        file.write("{}********{:04.4f},{:04.4},{:04.4}".format(entry5.get(), x, y, z))
        file.write("\n")


mainWindow = tkinter.Tk()
entry_text = tkinter.StringVar()

mainWindow.title("Indoor Positioning System")
mainWindow.geometry("800x250")   # Rows times Columns

label = tkinter.Label(mainWindow, text="Parameters")
label.grid(row=0, column=0, sticky="w")

# label = tkinter.Label(mainWindow, text="Name: MPINJ SPEEDWAY REVOLUTION R420 UHF RFID READER ")
# label.grid(row=2, column=0, sticky="n")

frame = tkinter.Frame(mainWindow)
frame.grid(row=2, column=0, sticky='w')

ref1 = tkinter.Variable(frame)
ref1.set(("00,00,00",))
reference1 = tkinter.Label(frame, text="Reference 1 Coordinate")
reference1.grid(row=3, column=2, sticky='w')
ref1 = tkinter.Entry(frame, textvariable=ref1)
ref1.grid(row=3, column=3, sticky="w")
a = ref1.get()

ref2 = tkinter.Variable(frame)
ref2.set(("40,00,00",))
reference2 = tkinter.Label(frame, text="Reference 2 Coordinate")
reference2.grid(row=4, column=2, sticky='w')
ref2 = tkinter.Entry(frame, textvariable=ref2)
ref2.grid(row=4, column=3, sticky="w")
b = ref2.get()

ref3 = tkinter.Variable(frame)
ref3.set(("00,45,00",))
reference3 = tkinter.Label(frame, text="Reference 3 Coordinate")
reference3.grid(row=5, column=2, sticky='w')
ref3 = tkinter.Entry(frame, textvariable=ref3)
ref3.grid(row=5, column=3, sticky="w")
c = ref3.get()

ref4 = tkinter.Variable(frame)
ref4.set(("40,45,00",))
reference4 = tkinter.Label(frame, text="Reference 4 Coordinate")
reference4.grid(row=6, column=2, sticky='w')
ref4 = tkinter.Entry(frame, textvariable=ref4)
ref4.grid(row=6, column=3, sticky="w")
d = ref4.get()


entry4 = tkinter.Variable(frame)
entry4.set(("20,23,00",))
label4 = tkinter.Label(frame, text="Reader's Position")     # The readers position
label4.grid(row=7, column=2, sticky='w')
entry4 = tkinter.Entry(frame, textvariable=entry4)
entry4.grid(row=7, column=3, sticky="w")
entry4.get()

entry5 = tkinter.Variable(frame)
entry5.set(("20,20,00",))
label5 = tkinter.Label(frame, text="Tags's Position")     # The readers position
label5.grid(row=8, column=2, sticky='w')
entry5 = tkinter.Entry(frame, textvariable=entry5)
entry5.grid(row=8, column=3, sticky="w")
entry5.get()

entry = tkinter.Variable(frame)
entry.set(("910",))
label = tkinter.Label(frame, text="Frequency (MHz)")
label.grid(row=3, column=0, sticky='w')
entry = tkinter.Entry(frame, textvariable=entry)
entry.grid(row=3, column=1, sticky="w")
entry.get()

entry1 = tkinter.Variable(frame)
entry1.set(("30",))
label1 = tkinter.Label(frame, text="Transmit Power (dBm)")    # The transmitting entry box
label1.grid(row=4, column=0, sticky='w')
entry1 = tkinter.Entry(frame, textvariable=entry1)
entry1.grid(row=4, column=1, sticky="w")
tx = entry1.get()

label2 = tkinter.Label(frame, text="Sensitivity")       # The sensitivity entry box
label2.grid(row=5, column=0, sticky='w')
entry2 = tkinter.Entry(frame)
entry2.grid(row=5, column=1, sticky="w")
se = entry2.get()

entry3 = tkinter.Variable(frame)
entry3.set(("1",))
label3 = tkinter.Label(frame, text="Alpha (/10)")             # The Alpha entry box
label3.grid(row=6, column=0, sticky='w')
entry3 = tkinter.Entry(frame, textvariable=entry3)
entry3.grid(row=6, column=1, sticky="w")
al = entry3.get()

label7 = tkinter.Label(frame, text="New Position")     # The readers position
label7.grid(row=12, column=2, sticky='w')
entry7 = tkinter.Entry(frame, textvariable=entry_text)
entry7.grid(row=12, column=3, sticky="w")


button = tkinter.Button(frame, text="Done")         # The done button
button.grid(row=13, column=1, sticky="we")

button1 = tkinter.Button(frame, text="Estimate", relief="sunken", command=hi)
button1.grid(row=12, column=1, sticky="we")


mainWindow.mainloop()


