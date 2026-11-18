from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation='p' , unit='mm',format='A4')
df = pd.read_csv('topics.csv')

for index,row in df.iterrows():
    pdf.add_page()
    pdf.set_font(family='Times', size=15)
    pdf.cell(w=0, h=20, txt=row['Topic'], align='c',ln=1,border=1)
    pdf.line(10,25,200,25)
    for i in range(row['Pages']-1):
        pdf.add_page()

pdf.output('output_pdf_file.pdf')
