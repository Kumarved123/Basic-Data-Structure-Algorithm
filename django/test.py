from reportlab.pdfgen import canvas
c = canvas.Canvas('test.pdf')
c.drawString(20, 30, 'Placement is must')
c.showPage()
c.save()