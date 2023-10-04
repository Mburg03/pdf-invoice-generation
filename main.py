# try to create it with a GUI! This is a really good example of how I can get 
# better at python.
#! C:\Users\Mario\Desktop\python\pdf-invoice-generation\venv\Scripts\python.exe
import pandas as pd
import glob 

filepaths = glob.glob("invoices/*.xlsx")
print(filepaths)

for filepath in filepaths: 
    df = pd.read_excel(filepath, sheet_name="Sheet 1")
    print(df)
    