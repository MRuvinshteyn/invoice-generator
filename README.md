# invoice-generator
Invoice generator for all your contract job needs

# Instructions
Go to the `python` folder and run `generator.py`. From there, enter all prompts (press enter if you wish to leave any prompt blank). The program will then create a file called `final.html` in the root folder of this repository. This file will be your completed invoice.

To convert the HTML file to a PDF, run `convert.py`. In order to make this work, you must have [PDFKit](https://pypi.org/project/pdfkit/) and [wkhtmltopdf](https://wkhtmltopdf.org/) installed for this program to work. If you do not wish to install PDFKit, you can install only wkhtmltopdf and run `wkhtmltopdf final.html <pdf-name>.pdf` in your operating system's terminal.
