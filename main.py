import yaml
import jinja2
import os
from pdflatex import PDFLaTeX

from config import *
from util import escape_latex

## Load YAML file with resume content
print(f"Loading resume data from {RESUME_DATA_PATH}")
resume_data = {}
with open(RESUME_DATA_PATH, 'r') as yaml_file:
    resume_data = yaml.safe_load(yaml_file)
if not resume_data:
    print("Error: No resume data was loaded!")
    quit(1)

## Load the LaTeX template

# TODO: configure Jinja2 environment to escape % signs, as this is problematic in LaTeX
print(f"Loading LaTeX template at {RESUME_TEMPLATE_FILE_NAME}")
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(RESUME_TEMPLATE_DIR),
                               block_start_string='(%',
                               block_end_string='%)',
                               variable_start_string='((',
                               variable_end_string='))',
                               finalize=escape_latex,
                               keep_trailing_newline=False
                               )
template = jinja_env.get_template(RESUME_TEMPLATE_FILE_NAME)

## TODO: Load/take as input job description

## TODO: Establish connections to ollama model

## TODO: Create queries and get responses

## TODO: Substitute LLM responses in YAML data

## Render LaTeX template
print("Rendering LaTeX file")
rendered_latex = template.render(resume_data)
generated_latex_path = os.path.join(OUTPUT_DIR, "output.tex")
if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)
with open(generated_latex_path, 'w') as output_file:
    output_file.write(rendered_latex)
print(f"Wrote generated LaTeX file to {generated_latex_path}")
## TODO: Generate PDF
print("Generating final PDF file...")
destination_pdf_path = os.path.join(OUTPUT_DIR, "output.pdf")
pdfl = PDFLaTeX.from_texfile(generated_latex_path)
pdfl.set_output_directory(OUTPUT_DIR)
pdfl.create_pdf(keep_pdf_file=True, keep_log_file=True)
print("Complete")