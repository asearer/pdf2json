import os
import PyPDF2
import json

def pdf_to_json(input_dir, output_dir):
    # Create output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Iterate over PDF files in the input directory
    for filename in os.listdir(input_dir):
        if filename.endswith('.pdf'):
            pdf_path = os.path.join(input_dir, filename)

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

            # Save JSON file in the output directory
            json_filename = os.path.splitext(filename)[0] + '.json'
            json_path = os.path.join(output_dir, json_filename)

            with open(json_path, 'w') as json_file:
                json.dump(json_data, json_file, indent=4)

            print(f'Successfully converted {filename} to JSON. JSON file saved at {json_path}.')

# Provide the input and output directories
input_directory = 'path/to/input_directory'
output_directory = 'path/to/output_directory'

pdf_to_json(input_directory, output_directory)

