
## Here we create music
list_of_input=[]

import pygame
import datetime
import time
from tkinter import *

pygame.init()
root = Tk()
root.title("Quantum Music")
root.geometry('1352x7000+0+0') # open from the upper-left
root.configure(background='white') # background configuration

import numpy
import qiskit
from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit
from qiskit import IBMQ, Aer, execute
import numpy as np
from qiskit import(
  QuantumCircuit,
  execute,
  Aer)
from qiskit.visualization import plot_histogram
from qiskit.transpiler import PassManager
from qiskit.transpiler.passes import Unroller
import json
import matplotlib.pyplot as plt
# import pygame
# import datetime
# import time
# from tkinter import *
IBMQ.load_account()

#IBMQ stuff (initialize the IBM account)
IBMQ.load_account()
provider = IBMQ.get_provider(group='open')

######################### music definitions
def flat(i, iflat):
    melodyCirc.x(iflat)
    melodyCirc.cx(iflat, i)
    melodyCirc.x(iflat)
    
# sharp function that decrease the note in half-note
def sharp(i, isharp):
    melodyCirc.x(i)
    melodyCirc.cx(i,isharp)
    melodyCirc.x(i)
    
# double flat function that increase the note twice half-note
def dflat(i, iflat, j):
    melodyCirc.x()
    melodyCirc.cx()
    melodyCirc.x()
    
# double sharp function that increase the note twice half-note
def dsharp(i, isharp, j):
    melodyCirc.x(i)
    melodyCirc.cx(i, isharp)
    melodyCirc.x(i)  
    melodyCirc.cx(i, j)
    melodyCirc.x(i)

# initialize all the ntoes in quantum superposition
def Melinit(nrq):
    melodyCirc.H()

# apply a silence in all the notes (all the notes are in off-mode)
def silence(nrq):
    melodyCirc.I()
    

######################### pygame stuff definitions

# This code is going to impliment all the quantum Algorithms in qiskit and return the final value.
def frameProperties(root, frameTrue):
    if frameTrue:
        frame = Frame(root, bg="#f0c2e0", bd=15, relief=RIDGE)
        frame.grid()
    else:
        frame = Frame(root, bg="#f0c2e0", relief=RIDGE)
        frame.grid()
    return frame

def labelTitle(input_frame, input_text, color_bg, fontsize):
    Label(input_frame, text=input_text, font=('arial', fontsize, 'bold'), padx=8, pady=8, bd=34, bg=color_bg, fg="white", justify=CENTER).grid(row=0, column=0, columnspan=11)
    return

def textEntries(input_frame, input_text, color_bg, fontsize, i, j):
    Entry(input_frame, textvariable=input_text, font=('arial', fontsize, 'bold'), bd=34, bg=color_bg, fg="white", width=20, justify=CENTER).grid(row=i, column=j, columnspan=11)
    return

def textButtons(input_frame, input_text, color_bg, fontsize, i, j, k, l, font_color, command_name):
    butts=Button(input_frame,  height= j, width=i, text=input_text, font=('arial', fontsize, 'bold'), command=command_name, bd=4, bg=color_bg, fg=font_color)
    butts.grid(row=k, column=l, padx=5, pady=5)
    # return butts

def ValueC():
    Circuit_Runner('C')
    return

def ValueCs():
    Circuit_Runner('C#')
    return

def ValueD():
    Circuit_Runner('D')
    return

def ValueDs():
    Circuit_Runner('D#')
    return

def ValueE():
    Circuit_Runner('E')
    return
    
######################### qiskit definitions
def Circuit_stuff(qc,backend,number_of_keys,shots,q,c):
    qc.barrier(q[0:number_of_keys])
    qc.measure(q[0:number_of_keys], c[0:number_of_keys])
    plt.figure()
    qc.draw(output='mpl', filename='my_circuit.png')
    job = execute(qc, backend, shots=shots)
    result = job.result()
    count = result.get_counts()
    return count

def Circuit_Runner(note):
    # First define our circuit: 
    backend = Aer.get_backend('qasm_simulator')
    number_of_keys = 5
    shots = 10000
    q = QuantumRegister(number_of_keys)
    c = ClassicalRegister(number_of_keys)
    qc = QuantumCircuit(q,c)
    list_of_input.append(note)
    for input_var in list_of_input:
        print(input_var)
        if input_var == 'C':
            print('HEllo1')
            qc.x(q[0])
            count = Circuit_stuff(qc,backend,number_of_keys,shots, q,c)
        if input_var == 'C#':
            qc.x(q[1])
            count = Circuit_stuff(qc,backend,number_of_keys,shots,q,c )
        if input_var == 'D':
            qc.x(q[2])
            count = Circuit_stuff(qc,backend,number_of_keys,shots,q,c)
        if input_var == 'D#':
            qc.x(q[3])
            count = Circuit_stuff(qc,backend,number_of_keys,shots,q,c)
        if input_var == 'E':
            qc.x(q[4])
            count = Circuit_stuff(qc,backend,number_of_keys,shots,q,c)
    print('HEllo')
    #a = Volume_Calculations(count,number_of_keys,shots)
    #return a

def Volume_Calculations(count,number_of_keys,shots):
    key_results = np.zeros([number_of_keys])
    #print(count)
    states = list(count.keys())
    probabilities = list(count.values())
    #print('states',states)
    #print('probailities',probabilities)
    for i in range(len(states)): 
        state = states[i]
        #print(range(len(str(state))))
        for j in range(len(str(state))):
            #print('Qbit val', int(state[j]))
            if int(state[j]) == 1:
                #print(probabilities[i])
                key_results[j]+=probabilities[i]
    key_results=key_results/float(shots)
    return(key_results)

# main frame
main_frame = frameProperties(root, True)

# frame inside main frame
title_frame = frameProperties(main_frame, True)
body_frame = frameProperties(main_frame, False)

str1 = StringVar()
str1.set("Some text")
Date1 = StringVar()
Time1 = StringVar()
Date1.set(time.strftime("%d/%m/%Y"))
Time1.set(time.strftime("%H:%M:%S"))

labelTitle(title_frame, "Quantum Musical Piano", "#1a0033", 25)
textEntries(title_frame, str1, "#1a0033", 18, 1, 2)

# Buttons
keys_sharp = ["C#", "D#"]
keys = ["C", "D", "E"]

textButtons(body_frame, "C", "white", 18, 9, 2, 0, 0, "black", ValueC)
btnCs = textButtons(body_frame, "C#", "black", 18, 7, 1, 2, 0, "white", ValueCs)
bbtnD = textButtons(body_frame, "D", "white", 18, 9, 2, 4, 0, "black", ValueD)
btnDs = textButtons(body_frame, "D#", "black", 18, 7, 1, 6, 0, "white", ValueDs)
btnE = textButtons(body_frame, "E", "white", 18, 9, 2, 8, 0, "black", ValueE)

root.mainloop()



