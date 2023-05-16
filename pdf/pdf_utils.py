from weasyprint import HTML


def convert_html_to_pdf(html_content, output_file):
    # Create a WeasyPrint HTML object
    html = HTML(string=html_content)

    # Render the HTML to a PDF file
    html.write_pdf(output_file)
