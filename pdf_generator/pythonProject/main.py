from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation='p' , unit='mm',format='A4')
df = pd.read_csv('topics.csv')
# A4 has 294 lines , 210 is width

for index,row in df.iterrows():
    pdf.add_page()
    pdf.set_font(family='Times', size=15)
    pdf.set_text_color(250, 180, 20)
    pdf.cell(w=0, h=20, txt=row['Topic'], align='l',ln=1)
    pdf.line(10,25,200,25)

    # adding footer
    pdf.ln(240)
    pdf.set_font(family='Times',size=8)
    pdf.set_text_color(180,180,180)
    pdf.line(10, 270, 200, 270)
    pdf.cell(w=0,h=5,txt=row['Topic'],align='R')
    for i in range(row['Pages']-1):
        pdf.add_page()
        pdf.ln(260)
        pdf.set_font(family='Times', size=8)
        pdf.set_text_color(180, 180, 180)
        pdf.line(10, 270, 200, 270)
        pdf.cell(w=0, h=5, txt=row['Topic'], align='R')

pdf.output('output_pdf_file.pdf')
