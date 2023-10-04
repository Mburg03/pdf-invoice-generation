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
    titles = list(df.columns)
    # Another solution for titles is using list comprehension
    # titles = [title.replace("_", " ").title() for title in titles]
    
    pdf.add_page()
    pdf.set_font(family="Times", size=24, style="B")
    pdf.cell(w=0, h=12, txt=f"Invoice nr. {invoice_number}", align="L", ln=1)
    pdf.cell(w=0, h=12, txt=f"Date {invoice_date}", align="L", ln=1)
    pdf.ln()
    
    # Add header to the table
    pdf.set_font(family="Times", size=10, style="B")
    pdf.set_text_color(80,80,80)
    pdf.cell(w=30, h=8, txt=titles[0].replace("_", " ").title(), border=1)
    pdf.cell(w=65, h=8, txt=titles[1].replace("_", " ").title(), border=1)
    pdf.cell(w=35, h=8, txt=titles[2].replace("_", " ").title(), border=1)
    pdf.cell(w=30, h=8, txt=titles[3].replace("_", " ").title(), border=1)
    pdf.cell(w=30, h=8, txt=titles[4].replace("_", " ").title(), border=1, 
             ln=1)
    
    # Add rows to the table
    for index, row in df.iterrows():
        pdf.set_font(family="Times", size=10)
        pdf.set_text_color(80,80,80)
        pdf.cell(w=30, h=8, txt=str(row["product_id"]), border=1)
        pdf.cell(w=65, h=8, txt=row["product_name"], border=1)
        pdf.cell(w=35, h=8, txt=str(row["amount_purchased"]), border=1)
        pdf.cell(w=30, h=8, txt=str(row["price_per_unit"]), border=1)
        pdf.cell(w=30, h=8, txt=str(row["total_price"]), border=1, ln=1)

    pdf.output(f"PDFs/{filename}.pdf")
    