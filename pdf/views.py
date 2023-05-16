from django.shortcuts import render
from .models import Profile
import pdfkit
from django.http import HttpResponse
from django.template import loader
import io
from fpdf import FPDF


# Create your views here.

from django.http import HttpResponse
from django.template.loader import render_to_string
from weasyprint import HTML, CSS

from django.shortcuts import render
import pdfkit

from io import BytesIO
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from django.template.loader import get_template

import pdfcrowd

def accept(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        summary = request.POST.get('summary', '')
        degree = request.POST.get('degree', '')
        school = request.POST.get('school', '')
        university = request.POST.get('university', '')
        previous_work = request.POST.get('previous_work', '')
        skills = request.POST.get('skills', '')

        profile = Profile(
            name=name,
            email=email,
            phone=phone,
            summary=summary,
            degree=degree,
            school=school,
            university=university,
            previous_work=previous_work,
            skills=skills,
        )
        profile.save()

    return render(request, 'pdf/accept.html')

def resume(request, pk):
    profile = Profile.objects.get(pk=pk)
    template = loader.get_template('pdf/resume.html')
    # pass dynamic data (user data)
    html = template.render({'profile': profile})
    options = {
        'page-size': 'Letter',
        'encoding': 'UTF-8',
    }
    # takes html string and converts to pdf
    pdf = pdfkit.from_string(html, False, options)
    response = HttpResponse(pdf,content_type='application/pdf')
    response['Content-Disposition'] = 'attachment'
    filename = 'resume.pdf'
    return response


def list(request):
    profiles = Profile.objects.all()
    return render(request, 'pdf/list.html', {"profiles": profiles})


from django.shortcuts import render
from django.http import HttpResponse
from weasyprint import HTML


def convert_to_pdf2(request):
    # Path to the HTML file
    html_file = 'pdf/templates/pdf/alex2.html'

    # Generate the PDF from HTML
    pdf = HTML(filename=html_file).write_pdf()

    # Set the response content type
    response = HttpResponse(content_type='application/pdf')

    # Set the PDF file as the response content
    response['Content-Disposition'] = 'attachment; filename="alex.pdf"'
    response.write(pdf)

    return response



import subprocess

def convert_to_pdf(request):
    # Path to the HTML file
    html_file = 'pdf/templates/pdf/alex.html'

    # Path to the output PDF file
    pdf_file = 'alex.pdf'

    # Command to execute
    command = f'wkhtmltopdf --disable-smart-shrinking --print-media-type {html_file} {pdf_file}'

    try:
        # Execute the command
        subprocess.run(command, shell=True, check=True)

        # Read the PDF file
        with open(pdf_file, 'rb') as f:
            pdf_content = f.read()

        # Set the response content type
        response = HttpResponse(content_type='application/pdf')

        # Set the PDF file as the response content
        response['Content-Disposition'] = 'attachment; filename="alex.pdf"'
        response.write(pdf_content)

        return response
    except subprocess.CalledProcessError:
        # Handle the error if the command execution fails
        return HttpResponse('Error converting HTML to PDF')



def bedjo2(request):
    # Path to the HTML file
    html_file = 'pdf/templates/pdf/alex.html'

    # Read the HTML file
    with open(html_file, 'r') as f:
        html_content = f.read()

    # Create a PDFCrowd client instance
    client = pdfcrowd.HtmlToPdfClient('georgi98', '8a93a8a11acc536da81d19caf3c9bb8b')  # Replace with your PDFCrowd username and API key

    # Convert HTML to PDF
    pdf = client.convertString(html_content)

    # Set the response content type
    response = HttpResponse(content_type='application/pdf')

    # Set the PDF file as the response content
    response['Content-Disposition'] = 'attachment; filename="alex.pdf"'

    # Write the PDF to the response
    response.write(pdf)

    return response




from django.http import HttpResponse
from fpdf import FPDF
from bs4 import BeautifulSoup

def bedjo3(request):
    # Path to the HTML file
    html_file = 'pdf/templates/pdf/alex.html'

    # Read the HTML file
    with open(html_file, 'r') as f:
        html_content = f.read()

    # Create a new PDF document
    pdf = FPDF()
    pdf.add_page()

    # Set the font and size for the content
    pdf.set_font('Arial', '', 10)

    # Convert HTML to PDF
    pdf.write_html(html_content)

    # Set the response content type
    response = HttpResponse(content_type='application/pdf')

    # Set the PDF file as the response content
    response['Content-Disposition'] = 'attachment; filename="alex.pdf"'

    # Save the PDF to the response
    pdf.output(response, 'F')

    return response

from pdfkit import from_file
from django.http import HttpResponse


def bedjo4(request):
    # Path to the HTML file
    html_file = 'pdf/templates/pdf/alex.html'

    # Set options for PDF generation
    options = {
        'page-size': 'A4',
        'margin-top': '0mm',
        'margin-right': '0mm',
        'margin-bottom': '0mm',
        'margin-left': '0mm',
    }

    # Generate the PDF from HTML
    pdf = from_file(html_file, False, options=options)

    # Set the response content type
    response = HttpResponse(content_type='application/pdf')

    # Set the PDF file as the response content
    response['Content-Disposition'] = 'attachment; filename="alex.pdf"'
    response.write(pdf)

    return response


from django.http import HttpResponse
from django.template.loader import get_template
from django.core.files.storage import FileSystemStorage
from wsgiref.util import FileWrapper

from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from bs4 import BeautifulSoup
from wsgiref.util import FileWrapper

def bedjo5(request):
    # Path to the HTML file
    html_file = 'pdf/templates/pdf/alex.html'

    # Read the HTML file
    with open(html_file, 'r') as f:
        html_content = f.read()

    # Create a temporary file storage for ReportLab
    fs = FileSystemStorage()
    temp_pdf = fs.open('temp.pdf', 'wb')  # Open in binary mode

    # Create a PDF document
    doc = SimpleDocTemplate(temp_pdf, pagesize=letter)

    # Define styles for different HTML tags
    styles = getSampleStyleSheet()
    style_paragraph = styles["Normal"]
    style_header = styles["Heading1"]

    # Create a story (content) for the PDF
    story = []

    # Parse HTML content and convert it to ReportLab elements
    soup = BeautifulSoup(html_content, 'html.parser')
    elements = []

    # Process each HTML tag and convert it to the corresponding ReportLab element
    for tag in soup.recursiveChildGenerator():
        if tag.name == 'p':
            text = tag.get_text(strip=True)
            paragraph = Paragraph(text, style_paragraph)
            elements.append(paragraph)

    # Add the elements to the story
    story.extend(elements)

    # Build the PDF document
    doc.build(story)

    # Set the response content type
    response = HttpResponse(content_type='application/pdf')

    # Set the PDF file as the response content
    response['Content-Disposition'] = 'attachment; filename="alex.pdf"'

    # Rewind the PDF file
    temp_pdf.seek(0)

    # Create a FileWrapper for the PDF file
    file_wrapper = FileWrapper(temp_pdf)

    # Write the PDF content to the response using the FileWrapper
    response.write(file_wrapper)

    # Close and delete the temporary PDF file
    temp_pdf.close()
    fs.delete('temp.pdf')

    return response


def see(request):
    return render(request, 'pdf/alex.html')