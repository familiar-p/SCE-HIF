import pandas as pd
import matplotlib.pyplot as plt
import pywt
import numpy as np
import time
import os
from tkinter import Tk, messagebox, filedialog
from tkinter.filedialog import askopenfilename

os.system('cls')

start_time=time.perf_counter()

cols=['Time (s)',
      'A59 DEALER 12KV GFN ZERO SEQ AMPS 500:5 FULL SCALE: 3 In',
      'A63 LOTTO 12KV GFN ZERO SEQ AMPS 500:5 FULL SCALE: 3 In',
      'A64 KENO 12KV GFN ZERO SEQ AMPS 500:5 FULL SCALE: 3 In',
      'A68 GAMBLER 12KV GFN ZERO SEQ AMPS 500:5 FULL SCALE: 3 In']


# Hide the root Tk window
Tk().withdraw()

# Open a file dialog to select the Excel file
input_file = askopenfilename(
    title="Select Excel file",
    filetypes=[("Excel files", "*.xlsx *.xls")]
)

if not input_file:
    print("No file selected. Exiting.")
    exit()
n_rows = len(pd.read_excel(input_file, usecols=[0]))  # counts total rows
rows=n_rows/2

df=pd.read_excel(input_file,usecols=cols,nrows=rows)
base_name = os.path.splitext(os.path.basename(input_file))[0]

timef=df['Time (s)']
A59=df['A59 DEALER 12KV GFN ZERO SEQ AMPS 500:5 FULL SCALE: 3 In']
A63=df['A63 LOTTO 12KV GFN ZERO SEQ AMPS 500:5 FULL SCALE: 3 In']
A64=df['A64 KENO 12KV GFN ZERO SEQ AMPS 500:5 FULL SCALE: 3 In']
A68=df['A68 GAMBLER 12KV GFN ZERO SEQ AMPS 500:5 FULL SCALE: 3 In']

plt.plot(timef,A59,label='A59 Dealer')
plt.plot(timef,A63,label='A63 Lotto')
plt.plot(timef,A64,label='A64 Keno')
plt.plot(timef,A68,label='A68 Gambler')
plt.axvline(x=0.09986, color='red', linestyle='--', linewidth=2)
plt.grid()
plt.legend()
plt.xlabel('Time(s)',fontsize=14)
plt.ylabel('Current(In)',fontsize=14)
plt.show()

end_time=time.perf_counter()
elapsed_time=end_time-start_time
print(f"\nScript Completed in {elapsed_time:.2f} seconds.")