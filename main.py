import yaml
import jinja2
import os
from pdflatex import PDFLaTeX

from config import *
from util import escape_latex
from llm_utils import rewrite_resume_data

## Load YAML file with resume content
resume_data = {}
with open(RESUME_DATA_PATH, 'r') as yaml_file:
    resume_data = yaml.safe_load(yaml_file)
if not resume_data:
    print("Error: No resume data was loaded!")
    quit(1)
print(f"Loaded resume data from {RESUME_DATA_PATH}")

## Load the LaTeX template
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(RESUME_TEMPLATE_DIR),
                               block_start_string='(%',
                               block_end_string='%)',
                               variable_start_string='((',
                               variable_end_string='))',
                               finalize=escape_latex,
                               keep_trailing_newline=False
                               )
template = jinja_env.get_template(RESUME_TEMPLATE_FILE_NAME)
print(f"Loaded LaTeX template at {RESUME_TEMPLATE_FILE_NAME}")

## Load/take as input job description

job_posting = ""
with open(JOB_POSTING_FILE, 'r') as job_file:
    job_posting = job_file.read()
if not job_posting:
    print("Warning: job posting file is empty")


## TODO: Establish connections to ollama model

## TODO: Create queries and get responses

## TODO: Substitute LLM responses in YAML data

new_resume_data = rewrite_resume_data(resume_data, job_posting)



## Render LaTeX file
rendered_latex = template.render(new_resume_data)
generated_latex_path = os.path.join(OUTPUT_DIR, "output.tex")
if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)
with open(generated_latex_path, 'w') as output_file:
    output_file.write(rendered_latex)
print(f"Wrote generated LaTeX file to {generated_latex_path}")

## Generate PDF
print("Generating final PDF file...")
destination_pdf_path = os.path.join(OUTPUT_DIR, "output.pdf")
pdfl = PDFLaTeX.from_texfile(generated_latex_path)
pdfl.set_output_directory(OUTPUT_DIR)
pdfl.create_pdf(keep_pdf_file=True, keep_log_file=True)
print(f"Done! PDF file created at {destination_pdf_path}")