from reportlab.lib import colors
from reportlab.lib.pagesizes import A6
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.units import cm

# Đăng ký font DejaVu Sans
pdfmetrics.registerFont(TTFont('DejaVuSans', 'DejaVuSans.ttf'))

# Tạo tài liệu PDF
output_file = "output_table_with_image.pdf"
margin = 0.5 * cm
doc = SimpleDocTemplate(output_file, pagesize=A6, 
                        leftMargin=margin, rightMargin=margin, 
                        topMargin=margin, bottomMargin=margin)

# Định nghĩa kiểu chữ với font DejaVu Sans
styles = getSampleStyleSheet()
styles['Normal'].fontName = 'DejaVuSans'

# Dữ liệu cho bảng
data = [
    [Image('tts.png', width=30, height=30),  # Ô (0,0) chứa ảnh
     Image('ghn.jpg', width=30, height=30), 
     Paragraph("Tiêu đề 3", styles['Normal'])],  # Dòng tiêu đề
    [Paragraph("Nội dung 1.1", styles['Normal']), 
     Paragraph("Nội dung 1.2", styles['Normal']), 
     Paragraph("Nội dung 1.3", styles['Normal'])],  # Dòng 2
    [Paragraph("Nội dung 2.1", styles['Normal']), 
     Paragraph("Nội dung 2.2", styles['Normal']), 
     Paragraph("Nội dung 2.3", styles['Normal'])],  # Dòng 3
    [Paragraph("Nội dung 3.1", styles['Normal']), 
     Paragraph("Nội dung 3.2", styles['Normal']), 
     Paragraph("Nội dung 3.3", styles['Normal'])],  # Dòng 4
    [Paragraph("Nội dung 4.1", styles['Normal']), 
     Paragraph("Nội dung 4.2", styles['Normal']), 
     Paragraph("Nội dung 4.3", styles['Normal'])],  # Dòng 5
    [Paragraph("Nội dung 5.1", styles['Normal']), 
     Paragraph("Nội dung 5.2", styles['Normal']), 
     Paragraph("Nội dung 5.3", styles['Normal'])],  # Dòng 6
    [Paragraph("Nội dung 6.1", styles['Normal']), 
     Paragraph("Nội dung 6.2", styles['Normal']), 
     Paragraph("Nội dung 6.3", styles['Normal'])],  # Dòng 7
    [Paragraph("Nội dung 7.1", styles['Normal']), 
     Paragraph("Nội dung 7.2", styles['Normal']), 
     Paragraph("Nội dung 7.3", styles['Normal'])]   # Dòng 8
]

# Tạo bảng
total_width = A6[0] - 2 * margin  # Tổng chiều rộng
num_columns = 3  # Số cột cho dòng 1

# Chiều rộng mỗi cột cho dòng 1
col_widths = [total_width / num_columns] * num_columns

table = Table(data, colWidths=col_widths)
table.setStyle(TableStyle([
    ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),  # Đường lưới cho bảng
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),  # Căn giữa cho tất cả ô
    ('SPAN', (0, 1), (2, 1)),
    ('SPAN', (0, 2), (2, 2)),
    ('SPAN', (0, 3), (1, 3)),
    ('SPAN', (0, 4), (1, 4)),
    ('SPAN', (0, 5), (1, 5)),
    ('SPAN', (0, 6), (1, 6)),
    ('SPAN', (0, 7), (1, 7)),
    ('SPAN', (2, 3), (2, 4)),
    ('SPAN', (2, 6), (2, 7))
]))

# Thêm bảng vào tài liệu
doc.build([table])

print("PDF đã được tạo thành công:", output_file)
