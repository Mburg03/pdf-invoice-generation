# try to create it with a GUI! This is a really good example of how I can get 
# better at python.
#! C:\Users\Mario\Desktop\python\pdf-invoice-generation\venv\Scripts\python.exe
import pandas as pd
import glob 
from fpdf import FPDF
from pathlib import Path

filepaths = glob.glob("invoices/*.xlsx")

for filepath in filepaths: 
    df = pd.read_excel(filepath, sheet_name="Sheet 1")
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    # one way to find these information butsecond way is more efficient
    # invoice_number = filepath[9:14] 
    # invoice_date = filepath[15:24]
    filename = Path(filepath).stem
    invoice_number = filename.split("-")[0]
    invoice_date = filename.split("-")[1]
    
    pdf.add_page()
    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=0, h=12, txt=f"Invoice nr. {invoice_number}", align="L", ln=1)
    pdf.cell(w=0, h=12, txt=f"Date {invoice_date}", align="L", ln=1)
    pdf.output(f"PDFs/{filename}.pdf")
    