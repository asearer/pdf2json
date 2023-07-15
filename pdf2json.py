import PyPDF2
import json

def pdf_to_json(pdf_path, json_path):
    pdf_file = open(pdf_path, 'rb')
    pdf_reader = PyPDF2.PdfReader(pdf_file)

    content = ''
    for page in pdf_reader.pages:
        content += page.extract_text()

    pdf_file.close()

    # Convert text content to JSON
    json_data = {
        'content': content
    }

    with open(json_path, 'w') as json_file:
        json.dump(json_data, json_file, indent=4)

    print(f'Successfully converted PDF to JSON. JSON file saved at {json_path}.')

# Provide the path to the PDF file and the desired path for the JSON file
pdf_file_path = 'path/to/input.pdf'
json_file_path = 'path/to/output.json'

pdf_to_json(pdf_file_path, json_file_path)
