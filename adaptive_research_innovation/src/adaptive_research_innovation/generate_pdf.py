import markdown2
import pdfkit
import os

def convert_markdown_to_pdf(md_path='output/report.md', pdf_path='output/report.pdf'):
    if not os.path.exists(md_path):
        print(f"Markdown file {md_path} not found!")
        return

    with open(md_path, 'r', encoding='utf-8') as f:
        md_content = f.read()

    # Convert Markdown to HTML
    html_content = markdown2.markdown(md_content)

    # Wrap HTML in a styled layout
    full_html = f"""
    <html>
    <head>
        <meta charset="UTF-8">
        <style>
            body {{
                font-family: 'Arial', sans-serif;
                margin: 30px;
                background-color: #f9f9f9;
                color: #2c3e50;
            }}
            h1 {{
                color: #2c3e50;
                border-bottom: 2px solid #3498db;
                padding-bottom: 5px;
            }}
            h2 {{
                color: #3498db;
                margin-top: 30px;
            }}
            h3 {{
                color: #2980b9;
                margin-top: 20px;
            }}
            p {{
                line-height: 1.6;
                font-size: 14px;
            }}
            ul {{
                padding-left: 20px;
            }}
            li {{
                margin-bottom: 5px;
            }}
            .section {{
                background-color: #ffffff;
                padding: 20px;
                margin-bottom: 20px;
                border-radius: 8px;
                box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
            }}
            footer {{
                position: fixed;
                bottom: 20px;
                left: 30px;
                right: 30px;
                font-size: 12px;
                color: #999999;
                text-align: center;
                border-top: 1px solid #ccc;
                padding-top: 10px;
            }}
        </style>
    </head>
    <body>
        <div class="section">
            {html_content}
        </div>
        <footer>Adaptive Research Innovation Report • 2025</footer>
    </body>
    </html>
    """

    # PDF layout options
    options = {
        'page-size': 'A4',
        'encoding': "UTF-8",
        'margin-top': '15mm',
        'margin-bottom': '20mm',
        'margin-left': '20mm',
        'margin-right': '20mm',
    }

    # Try auto config first
    try:
        pdfkit.from_string(full_html, pdf_path, options=options)
        print(f"✅ Modern PDF report generated at {pdf_path}")
    except OSError:
        print("⚠️ Auto wkhtmltopdf not found. Trying manual path...")

        wkhtmltopdf_path = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'  # Edit if different
        if not os.path.exists(wkhtmltopdf_path):
            print(f"❌ wkhtmltopdf not found at {wkhtmltopdf_path}. Check your installation.")
            return

        config = pdfkit.configuration(wkhtmltopdf=wkhtmltopdf_path)
        try:
            pdfkit.from_string(full_html, pdf_path, options=options, configuration=config)
            print(f"✅ Modern PDF report generated at {pdf_path} (manual path)")
        except Exception as e:
            print(f"❌ PDF generation failed: {e}")
