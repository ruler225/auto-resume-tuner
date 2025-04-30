from typing import Any
import yaml
from langchain.output_parsers import YamlOutputParser
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

from config import *

system_prompt = """
You are a professional resume optimization assistant.
You will receive two inputs:

A resume formatted in valid YAML.

A job posting (plain text).

Your task is to generate an improved and tailored version of the resume, also in valid YAML format, based on the job posting.

Follow these detailed instructions:

Alignment: Carefully align the content of the resume to the job posting. Emphasize relevant experiences, skills, certifications, and keywords present in the job description.

Keyword Integration: Integrate as many keywords, tools, technologies, and responsibilities from the job posting into the resume naturally and truthfully. Do not fabricate experiences, but rephrase or prioritize existing ones to match the job's language.

Enhancement: Improve phrasing to make accomplishments stronger, using action verbs and quantifiable achievements where possible.

Formatting:

Maintain the original structure of the YAML resume unless improvements are needed for clarity or relevance.

Ensure the output is properly formatted, complete, and parsable YAML.

Wrap the final YAML output inside triple backticks ```(yaml ... )```.

Do not include any explanations, commentary, or text outside of the YAML.

Honesty: Do not invent new experiences, degrees, or roles. Only enhance or reword existing content.

Prioritization: Prioritize experiences, skills, and projects most relevant to the job posting. It is acceptable to reorder resume sections if it improves relevance.

Conciseness: Keep descriptions professional, concise, and results-oriented.

Output strictly and only the improved resume enclosed in three backticks. \n
"""


def rewrite_resume_data(resume_data: dict[str, Any], job_posting: str) -> dict[str, Any]:
    """
    Given resume data in dict format and a job posting, use LLM to optimize resume data and return tuned
    resume as dict.
    """

    # TODO: implementation

    llm = OllamaLLM(model=LLM_MODEL, base_url="http://mikhailhome.asuscomm.com:11434")

    # Set up prompt

    template = ChatPromptTemplate([
        ("system", system_prompt),
        ("user", "Job posting:\n{job_posting}"),
        ("user", system_prompt),
        ("user", "Resume data:\n```{resume_data}```"),
        ("user", system_prompt)
    ])
    yaml_resume_data = yaml.dump(resume_data)
    messages = template.format_messages(job_posting=job_posting, resume_data=yaml_resume_data)

    print("Invoking LLM...")
    result = llm.invoke(messages)

    print(result)

    return resume_data