from reportlab.lib import colors
from reportlab.lib.pagesizes import A6
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.units import cm  # Sử dụng đơn vị cm

# Đăng ký font DejaVu Sans
pdfmetrics.registerFont(TTFont('DejaVuSans', 'DejaVuSans.ttf'))

# Hàm tạo PDF với Platypus
def create_pdf_with_platypus(output_file):
    styles = getSampleStyleSheet()
    
    # Sử dụng font DejaVu Sans cho kiểu chữ 'Normal' và 'Title'
    styles['Normal'].fontName = 'DejaVuSans'
    styles['Title'].fontName = 'DejaVuSans'
    
    # Tạo tài liệu với margin nhỏ (0.5 cm)
    margin = 0.5 * cm
    doc = SimpleDocTemplate(output_file, pagesize=A6, 
                            leftMargin=margin, rightMargin=margin, 
                            topMargin=margin, bottomMargin=margin)
    story = []

    # Thêm tiêu đề
    title = Paragraph("Tiêu Đề PDF", styles['Title'])
    story.append(title)
    story.append(Spacer(1, 12))

    # Tạo dữ liệu cho bảng
    data = [
        [Paragraph("Cột 1", styles['Normal']), Paragraph("Cột 2", styles['Normal']), Paragraph("Cột 3", styles['Normal'])],  # Dòng 1
        [Paragraph("Cột 1 - Dòng 2, gộp 3 cột", styles['Normal']), '', ''],  # Dòng 2 gộp 3 cột
    ]

    # Dữ liệu từ dòng 3 tới dòng 8
    for i in range(3, 9):
        data.append([
            Paragraph(f"Nội dung ô {i} - Chiếm 2/3 chiều rộng", styles['Normal']),
            Paragraph(f"Nội dung ô {i} - Chiếm 1/3 chiều rộng", styles['Normal'])
        ])

    # Tính toán chiều rộng của bảng
    total_width = A6[0] - 2 * margin  # Tổng chiều rộng
    num_columns = 3  # Số cột cho dòng 1

    # Chiều rộng mỗi cột cho dòng 1
    col_widths = [total_width / num_columns] * num_columns

    # Gộp cột cho dòng 2 (sử dụng colspan = 3)
    data[1] = [Paragraph("Cột 1 - Dòng 2, gộp 3 cột", styles['Normal']), '', '']  # Gán nội dung cho ô gộp
    print(data)
    # Tạo bảng
    
    table = Table(data, colWidths=col_widths)

    # Định dạng bảng
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('SIZE', (0, 0), (-1, 0), 14),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('LEFTPADDING', (0, 0), (-1, -1), 5),  # Padding bên trái
        ('RIGHTPADDING', (0, 0), (-1, -1), 5),  # Padding bên phải
        ('TOPPADDING', (0, 0), (-1, -1), 5),  # Padding bên trên
        ('BOTTOMPADDING', (0, 0), (-1, -1), 5),  # Padding bên dưới
    ]))

    # Cập nhật dữ liệu cho dòng 2
    # Để gộp 3 cột trong dòng 2, hãy chỉ định nội dung cho ô gộp
    data[1] = [Paragraph("Cột 1 - Dòng 2, gộp 3 cột", styles['Normal']), '', '']  # Dòng 2 gộp 3 cột

    # Cập nhật lại bảng với dữ liệu đã gộp
    table = Table(data, colWidths=col_widths)

    # Cập nhật lại định dạng cho bảng sau khi gộp
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('SIZE', (0, 0), (-1, 0), 14),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('LEFTPADDING', (0, 0), (-1, -1), 5),  # Padding bên trái
        ('RIGHTPADDING', (0, 0), (-1, -1), 5),  # Padding bên phải
        ('TOPPADDING', (0, 0), (-1, -1), 5),  # Padding bên trên
        ('BOTTOMPADDING', (0, 0), (-1, -1), 5),  # Padding bên dưới
    ]))

    # Thêm bảng vào câu chuyện
    story.append(table)

    # Lưu tài liệu
    doc.build(story)

# Gọi hàm để tạo PDF
output_file = "output_platypus_merged_column.pdf"
create_pdf_with_platypus(output_file)
