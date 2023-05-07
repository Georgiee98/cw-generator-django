# CW Generator Django

##  About
This project lets you create a CW only by fulfilling a simple form


##  Technologies
- Django
- Bootstrap
- wkhtmltox

##  Usage
Windows: <code>source cw_generate_pdf/Scripts/activate.bat</code>
UNIX: <code>source cw_generate_pdf/Scripts/activate</code>

### You need to install [**wkhtmltox**](https://wkhtmltopdf.org/downloads.html)
<ol>
  <li>Winodws Steps</li>
  <li>Adjust the Environment variable depending on the directory you chosed to install
    <ol>
      <li>Environment Variables</li>
      <li>Path --> Edit</li>
      <li>C:\Program Files\wkhtmltopdf\bin</li>
      <li>⬆️This is just an example but it must end with wkhtmltopdf\bin (or however you named it if you changed the original filepath⬆️</li>
    </ol>
  </li>
  <li>Restarting the computer might be needed</li>
</ol>
- Configure your Python interpreter to **cw_generate_pdf**
### Run: (be sure to be in the folder/directory of manage.py) 
- <code>python manage.py runserver</code>

