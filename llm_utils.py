from typing import Any
import yaml
from langchain.output_parsers import YamlOutputParser
from langchain_ollama import OllamaLLM
from langchain_core.prompts import PromptTemplate

from config import *


prompt_template = """
You will be given a resume in YAML format and a job posting. Fine-tune the given resume and optimize it for the given job posting. Make sure to include as many keywords in the resume 
as possible while keeping it honest. Output the new resume in YAML format enclosed in three back-ticks. Do not output anything else. \n
Job posting: \n
{job_posting}\n\n
Resume data: \n
```
{resume_data}
```
"""

def rewrite_resume_data(resume_data: dict[str, Any], job_posting: str) -> dict[str, Any]:
    """
    Given resume data in dict format and a job posting, use LLM to optimize resume data and return tuned
    resume as dict.
    """

    # TODO: implementation

    llm = OllamaLLM(model=LLM_MODEL)

    # Set up prompt

    template = PromptTemplate.from_template(prompt_template)

    prompt = template.invoke({
        "job_posting": job_posting,
        "resume_data": yaml.dump(resume_data)
    })

    print("Invoking LLM...")
    result = llm.invoke(prompt)

    print(result)

    return resume_data