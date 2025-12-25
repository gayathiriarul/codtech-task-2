import pandas as pd
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

data = pd.read_csv("data.csv")

total_students = len(data)
average_marks = data["Marks"].mean()
max_marks = data["Marks"].max()
min_marks = data["Marks"].min()

pdf = canvas.Canvas("Student_Report.pdf", pagesize=A4)
width, height = A4

pdf.setFont("Helvetica-Bold", 16)
pdf.drawString(180, height - 50, "Student Marks Report")

pdf.setFont("Helvetica", 12)
pdf.drawString(50, height - 100, f"Total Students : {total_students}")
pdf.drawString(50, height - 130, f"Average Marks : {average_marks:.2f}")
pdf.drawString(50, height - 160, f"Highest Marks : {max_marks}")
pdf.drawString(50, height - 190, f"Lowest Marks  : {min_marks}")

pdf.drawString(50, height - 240, "Name")
pdf.drawString(200, height - 240, "Marks")

y = height - 270
for index, row in data.iterrows():
    pdf.drawString(50, y, row["Name"])
    pdf.drawString(200, y, str(row["Marks"]))
    y -= 25

pdf.save()
print("PDF Report Generated Successfully!")