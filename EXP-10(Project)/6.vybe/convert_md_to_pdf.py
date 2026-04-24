import re
import os
from fpdf import FPDF
from datetime import datetime

# File paths
md_file = r'docs\HLD.md'
pdf_file = r'docs\HLD.pdf'

# Read markdown file
with open(md_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Create PDF
class MarkdownPDF(FPDF):
    def __init__(self):
        super().__init__(orientation='P', unit='mm', format='A4')
        self.page_height = self.h - 20
        self.set_left_margin(15)
        self.set_right_margin(15)
        self.set_top_margin(15)
        self.set_auto_page_break(auto=True, margin=20)
        self.add_font('Arial', '', 'C:\\Windows\\Fonts\\arial.ttf')
        self.add_font('Arial', 'B', 'C:\\Windows\\Fonts\\arialbd.ttf')
        self.add_font('Arial', 'I', 'C:\\Windows\\Fonts\\ariali.ttf')
        self.add_page()
        
    def header(self):
        if self.page_no() > 1:
            self.set_font('Arial', '', 8)
            self.set_text_color(150)
            self.cell(0, 10, f'VYBE - High-Level Design Document | Page {self.page_no()}', 0, 1, 'C')
            self.ln(2)
    
    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', '', 8)
        self.set_text_color(150)
        self.cell(0, 10, f'Generated on {datetime.now().strftime("%B %d, %Y")}', 0, 0, 'C')
    
    def add_heading(self, text, level):
        if level == 1:
            self.set_font('Arial', 'B', 24)
            self.set_text_color(44, 62, 80)
            self.ln(5)
            self.multi_cell(0, 8, text)
            self.ln(2)
        elif level == 2:
            self.set_font('Arial', 'B', 16)
            self.set_text_color(52, 73, 94)
            self.ln(4)
            self.multi_cell(0, 7, text)
            self.ln(1)
        elif level == 3:
            self.set_font('Arial', 'B', 12)
            self.set_text_color(127, 140, 141)
            self.ln(2)
            self.multi_cell(0, 6, text)
            self.ln(1)
    
    def add_paragraph(self, text):
        if text.strip():
            self.set_font('Arial', '', 10)
            self.set_text_color(51, 51, 51)
            self.multi_cell(0, 5, text.strip())
            self.ln(2)
    
    def add_bullet_list(self, items):
        self.set_font('Arial', '', 10)
        self.set_text_color(51, 51, 51)
        for item in items:
            if item.strip():
                self.set_x(self.l_margin + 5)
                self.multi_cell(0, 5, '• ' + item.strip())
        self.ln(1)

try:
    pdf = MarkdownPDF()
    
    # Title page
    pdf.ln(30)
    pdf.set_font('Arial', 'B', 36)
    pdf.set_text_color(44, 62, 80)
    pdf.cell(0, 20, 'VYBE', 0, 1, 'C')
    
    pdf.set_font('Arial', '', 14)
    pdf.set_text_color(127, 140, 141)
    pdf.cell(0, 10, 'High-Level Design Document', 0, 1, 'C')
    pdf.cell(0, 10, 'Social Media Platform Architecture', 0, 1, 'C')
    
    pdf.ln(10)
    pdf.set_font('Arial', '', 11)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(0, 8, f'Version: 1.0.0', 0, 1, 'C')
    pdf.cell(0, 8, f'Date: April 24, 2026', 0, 1, 'C')
    
    pdf.add_page()
    
    # Parse content
    lines = content.split('\n')
    i = 0
    while i < len(lines):
        line = lines[i]
        
        # Headings
        if line.startswith('# '):
            pdf.add_heading(line[2:], 1)
        elif line.startswith('## '):
            pdf.add_heading(line[3:], 2)
        elif line.startswith('### '):
            pdf.add_heading(line[4:], 3)
        
        # Code blocks
        elif line.startswith('```'):
            i += 1
            code_lines = []
            while i < len(lines) and not lines[i].startswith('```'):
                code_lines.append(lines[i])
                i += 1
            pdf.set_font('Arial', '', 8)
            pdf.set_fill_color(240, 240, 240)
            pdf.multi_cell(0, 4, '\n'.join(code_lines), border=1, fill=True)
            pdf.ln(1)
        
        # Tables
        elif '|' in line and i + 1 < len(lines) and '|' in lines[i + 1]:
            table_data = [cell.strip() for cell in line.split('|')[1:-1]]
            pdf.set_font('Arial', 'B', 9)
            pdf.set_fill_color(52, 152, 219)
            pdf.set_text_color(255, 255, 255)
            for cell in table_data:
                pdf.cell(0, 6, cell[:20], 1, 0, 'C', fill=True)
            pdf.ln()
            pdf.set_text_color(51, 51, 51)
            
            i += 2  # Skip separator line
            while i < len(lines) and '|' in lines[i]:
                row_data = [cell.strip() for cell in lines[i].split('|')[1:-1]]
                pdf.set_font('Arial', '', 8)
                for cell in row_data:
                    pdf.cell(0, 5, cell[:20], 1, 0)
                pdf.ln()
                i += 1
            i -= 1
        
        # Bullet lists
        elif line.strip().startswith('- ') or line.strip().startswith('* '):
            items = []
            while i < len(lines) and (lines[i].strip().startswith('- ') or lines[i].strip().startswith('* ')):
                items.append(lines[i].strip()[2:])
                i += 1
            pdf.add_bullet_list(items)
            i -= 1
        
        # Paragraphs
        elif line.strip() and not line.startswith('---'):
            pdf.add_paragraph(line)
        
        # Horizontal rules
        elif line.startswith('---'):
            pdf.set_draw_color(200, 200, 200)
            pdf.line(pdf.l_margin, pdf.get_y(), pdf.w - pdf.r_margin, pdf.get_y())
            pdf.ln(4)
        
        i += 1
    
    # Output PDF
    pdf.output(pdf_file)
    print(f"✓ PDF successfully created: {os.path.abspath(pdf_file)}")
    print(f"✓ File size: {os.path.getsize(pdf_file) / 1024:.2f} KB")
    
except Exception as e:
    print(f"✗ Error creating PDF: {str(e)}")
    import traceback
    traceback.print_exc()
