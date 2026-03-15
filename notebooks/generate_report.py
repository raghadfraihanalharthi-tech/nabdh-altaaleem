"""
Nabdh Al-Taaleem - PDF Report Generator
Author: Raghad Al-Blahdi
"""

from fpdf import FPDF
import os

charts_dir = os.path.join(os.path.dirname(__file__), '..', 'report', 'charts')
report_path = os.path.join(os.path.dirname(__file__), '..', 'report', 'findings_report.pdf')

class Report(FPDF):
    def header(self):
        self.set_fill_color(7, 17, 31)
        self.rect(0, 0, 210, 18, 'F')
        self.set_font('Helvetica', 'B', 10)
        self.set_text_color(16, 185, 129)
        self.set_y(5)
        self.cell(0, 8, 'NABDH AL-TAALEEM  |  Women in Saudi ICT - Case Study Report', align='C')
        self.ln(14)

    def footer(self):
        self.set_y(-14)
        self.set_fill_color(7, 17, 31)
        self.rect(0, self.get_y(), 210, 14, 'F')
        self.set_font('Helvetica', '', 8)
        self.set_text_color(61, 87, 119)
        self.cell(0, 10,
                  f'Page {self.page_no()}  |  Data: open.data.gov.sa  |  Author: Raghad Al-Blahdi',
                  align='C')

    def cover(self):
        self.set_fill_color(7, 17, 31)
        self.rect(0, 0, 210, 297, 'F')

        # Green accent bar
        self.set_fill_color(16, 185, 129)
        self.rect(0, 80, 6, 60, 'F')

        # Title
        self.set_y(88)
        self.set_font('Helvetica', 'B', 34)
        self.set_text_color(255, 255, 255)
        self.cell(0, 14, 'NABDH AL-TAALEEM', align='C')
        self.ln(16)

        self.set_font('Helvetica', '', 16)
        self.set_text_color(16, 185, 129)
        self.cell(0, 10, 'Women in Saudi ICT - Data Case Study', align='C')
        self.ln(22)

        # Divider
        self.set_draw_color(16, 185, 129)
        self.set_line_width(0.4)
        self.line(40, self.get_y(), 170, self.get_y())
        self.ln(14)

        # Subtitle
        self.set_font('Helvetica', '', 11)
        self.set_text_color(124, 163, 200)
        self.multi_cell(0, 7,
            'An analysis of women\'s participation in the Information and\n'
            'Communications Technology sector in Saudi Arabia (2020-2024),\n'
            'benchmarked against Vision 2030 targets and ITU global standards.',
            align='C')
        self.ln(20)

        # Metadata box
        self.set_fill_color(12, 29, 51)
        self.set_draw_color(30, 58, 90)
        self.set_line_width(0.3)
        self.rect(35, self.get_y(), 140, 52, 'FD')
        self.set_y(self.get_y() + 8)

        meta = [
            ('Author',    'Raghad Al-Blahdi'),
            ('Field',     'Computer Science - Data Analysis & UX Design'),
            ('Data',      'open.data.gov.sa  |  Vision 2030  |  ITU 2024'),
            ('Period',    '2020 - 2024'),
        ]
        for label, value in meta:
            self.set_x(42)
            self.set_font('Helvetica', 'B', 9)
            self.set_text_color(16, 185, 129)
            self.cell(34, 7, label + ':')
            self.set_font('Helvetica', '', 9)
            self.set_text_color(226, 232, 240)
            self.cell(0, 7, value)
            self.ln(8)

    def section_title(self, number, title):
        self.ln(6)
        self.set_fill_color(12, 29, 51)
        self.rect(10, self.get_y(), 190, 11, 'F')
        self.set_fill_color(16, 185, 129)
        self.rect(10, self.get_y(), 3, 11, 'F')
        self.set_y(self.get_y() + 1.5)
        self.set_x(16)
        self.set_font('Helvetica', 'B', 11)
        self.set_text_color(255, 255, 255)
        self.cell(0, 8, f'{number}.  {title}')
        self.ln(14)

    def body_text(self, text):
        self.set_font('Helvetica', '', 10)
        self.set_text_color(180, 196, 214)
        self.set_x(14)
        self.multi_cell(182, 6, text)
        self.ln(4)

    def key_stat(self, value, label, color=(16, 185, 129)):
        x = self.get_x()
        y = self.get_y()
        self.set_fill_color(12, 29, 51)
        self.set_draw_color(30, 58, 90)
        self.rect(x, y, 56, 22, 'FD')
        self.set_y(y + 3)
        self.set_x(x)
        self.set_font('Helvetica', 'B', 14)
        self.set_text_color(*color)
        self.cell(56, 8, value, align='C')
        self.ln(8)
        self.set_x(x)
        self.set_font('Helvetica', '', 7.5)
        self.set_text_color(124, 163, 200)
        self.cell(56, 5, label, align='C')
        self.ln(12)

    def finding_item(self, icon, title, body):
        self.set_x(14)
        self.set_font('Helvetica', 'B', 10)
        self.set_text_color(16, 185, 129)
        self.cell(8, 7, icon)
        self.set_font('Helvetica', 'B', 10)
        self.set_text_color(226, 232, 240)
        self.cell(0, 7, title)
        self.ln(7)
        self.set_x(22)
        self.set_font('Helvetica', '', 9.5)
        self.set_text_color(180, 196, 214)
        self.multi_cell(178, 5.5, body)
        self.ln(3)

    def source_row(self, data_point, value, source, source_type):
        colors = {'Government': (16, 185, 129), 'International': (6, 182, 212), 'Official': (245, 158, 11)}
        c = colors.get(source_type, (124, 163, 200))
        y = self.get_y()
        self.set_fill_color(12, 29, 51)
        self.rect(10, y, 190, 10, 'F')
        self.set_y(y + 1.5)
        self.set_x(12)
        self.set_font('Helvetica', '', 8.5)
        self.set_text_color(226, 232, 240)
        self.cell(84, 7, data_point)
        self.set_font('Helvetica', 'B', 8.5)
        self.set_text_color(*c)
        self.cell(24, 7, value, align='C')
        self.set_font('Helvetica', '', 8)
        self.set_text_color(124, 163, 200)
        self.cell(60, 7, source)
        self.set_font('Helvetica', 'B', 7.5)
        self.set_text_color(*c)
        self.cell(0, 7, f'[{source_type}]', align='R')
        self.ln(11)


pdf = Report()
pdf.set_auto_page_break(auto=True, margin=18)
pdf.set_margins(10, 20, 10)

# ── COVER PAGE ─────────────────────────────────────────
pdf.add_page()
pdf.cover()

# ── PAGE 2: EXECUTIVE SUMMARY ─────────────────────────
pdf.add_page()
pdf.set_fill_color(7, 17, 31)
pdf.rect(0, 0, 210, 297, 'F')

pdf.section_title('1', 'Executive Summary')
pdf.body_text(
    "This report analyzes the participation of women in Saudi Arabia's Information and "
    "Communications Technology (ICT) sector from 2020 to 2024, using official data published "
    "on the Saudi Open Data Platform (open.data.gov.sa). The findings are benchmarked against "
    "Vision 2030 national targets and ITU international standards to provide context and "
    "identify the remaining gap."
)

# Key stats row
pdf.set_x(14)
stats = [
    ('34.50%', 'Participation Rate 2024',  (16, 185, 129)),
    ('+10.42%', 'Growth Since 2020',       (6, 182, 212)),
    ('10%',    'Female Share of ICT Jobs', (245, 158, 11)),
    ('ACHIEVED','Vision 2030 Target',      (16, 185, 129)),
]
for val, lbl, col in stats:
    pdf.key_stat(val, lbl, col)
    pdf.set_xy(pdf.get_x() + 58, pdf.get_y() - 22)
pdf.ln(8)

pdf.section_title('2', 'Key Findings')
findings = [
    ('+', 'Consistent Growth',
     'Women\'s participation in ICT grew every single year from 24.08% in 2020 to 34.50% in '
     '2024 - an increase of 10.42 percentage points over four years, averaging +2.61% annually.'),
    ('>', 'Vision 2030 Target Surpassed',
     'Saudi Arabia has exceeded its Vision 2030 target of 30% women\'s participation in the '
     'labor market. The ICT sector specifically reached 34.50% - 4.5 points above the target.'),
    ('!', 'Workforce Gap Remains',
     'Despite the high participation rate, women represent only 10% of the total ICT workforce '
     'in 2024. This means that while women who are in ICT are well-represented proportionally, '
     'the absolute number of women entering the sector still requires acceleration.'),
    ('~', 'Above Global Benchmark',
     'Saudi Arabia\'s 34.50% rate in 2024 exceeds the ITU global benchmark of less than 33% '
     'for women in technology roles - placing the Kingdom ahead of the global average.'),
]
for icon, title, body in findings:
    pdf.finding_item(icon, title, body)

# ── PAGE 3: CHARTS ────────────────────────────────────
pdf.add_page()
pdf.set_fill_color(7, 17, 31)
pdf.rect(0, 0, 210, 297, 'F')

pdf.section_title('3', 'Data Visualizations')

chart1 = os.path.join(charts_dir, 'chart1_participation_trend.png')
chart2 = os.path.join(charts_dir, 'chart2_gender_ratio.png')
chart3 = os.path.join(charts_dir, 'chart3_comparison.png')

if os.path.exists(chart1):
    pdf.set_font('Helvetica', 'B', 9)
    pdf.set_text_color(124, 163, 200)
    pdf.set_x(14)
    pdf.cell(0, 6, 'Figure 1  -  Participation Trend 2020-2024 with Benchmarks')
    pdf.ln(7)
    pdf.image(chart1, x=12, w=186)
    pdf.ln(6)

if os.path.exists(chart2) and os.path.exists(chart3):
    pdf.set_font('Helvetica', 'B', 9)
    pdf.set_text_color(124, 163, 200)
    pdf.set_x(14)
    pdf.cell(90, 6, 'Figure 2  -  Gender Distribution 2024')
    pdf.cell(0, 6, 'Figure 3  -  Benchmark Comparison')
    pdf.ln(7)
    pdf.image(chart2, x=12, w=90)
    pdf.image(chart3, x=108, w=90, y=pdf.get_y() - 68)
    pdf.ln(6)

# ── PAGE 4: DATA SOURCES ──────────────────────────────
pdf.add_page()
pdf.set_fill_color(7, 17, 31)
pdf.rect(0, 0, 210, 297, 'F')

pdf.section_title('4', 'Data Sources - Full Transparency')
pdf.body_text(
    "Every data point in this report is cited below with its original source. "
    "No figures were estimated or assumed without explicit attribution."
)

pdf.set_x(12)
pdf.set_font('Helvetica', 'B', 8.5)
pdf.set_text_color(124, 163, 200)
pdf.cell(84, 8, 'Data Point')
pdf.cell(24, 8, 'Value', align='C')
pdf.cell(60, 8, 'Source')
pdf.cell(0,  8, 'Type', align='R')
pdf.ln(10)

sources = [
    ('Women\'s participation in ICT - 2020', '24.08%', 'open.data.gov.sa', 'Government'),
    ('Women\'s participation in ICT - 2021', '28.19%', 'open.data.gov.sa', 'Government'),
    ('Women\'s participation in ICT - 2022', '33.01%', 'open.data.gov.sa', 'Government'),
    ('Women\'s participation in ICT - 2023', '34.18%', 'open.data.gov.sa', 'Government'),
    ('Women\'s participation in ICT - 2024', '34.50%', 'open.data.gov.sa', 'Government'),
    ('Female share of ICT workforce - 2024', '10%',    'open.data.gov.sa', 'Government'),
    ('Male share of ICT workforce - 2024',   '90%',    'open.data.gov.sa', 'Government'),
    ('Vision 2030 labor market target',      '30%',    'vision2030.gov.sa', 'Official'),
    ('Women in global tech roles',           '<33%',   'ITU Digital Trends 2024', 'International'),
]
for row in sources:
    pdf.source_row(*row)

pdf.ln(8)
pdf.section_title('5', 'Recommendations')
recs = [
    ('R1', 'Increase Absolute Numbers',
     'While the participation rate is strong, targeted scholarships and hiring programs '
     'should focus on growing the absolute count of women in ICT roles beyond 10% of workforce.'),
    ('R2', 'Focus on Retention',
     'Track not only entry rates but retention rates of women in ICT beyond 3-5 years '
     'to ensure sustained workforce presence.'),
    ('R3', 'Regional Benchmarking',
     'Future research should compare Saudi performance against individual GCC countries '
     'and emerging markets using ITU regional datasets.'),
]
for code, title, body in recs:
    pdf.finding_item(code, title, body)

pdf.set_auto_page_break(False)
pdf.ln(2)
pdf.set_draw_color(16, 185, 129)
pdf.set_line_width(0.3)
pdf.line(14, pdf.get_y(), 196, pdf.get_y())
pdf.ln(3)
pdf.set_x(14)
pdf.set_font('Helvetica', 'I', 8.5)
pdf.set_text_color(61, 87, 119)
pdf.multi_cell(182, 5.5,
    'This report was produced as part of a personal data analysis initiative. '
    'All government data is used under the Saudi Open Data License (CC BY 4.0). '
    'ITU data is referenced for academic benchmarking purposes.')

pdf.output(report_path)
print(f"Report saved: {report_path}")
