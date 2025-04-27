from typing import Any
import yaml
from langchain.output_parsers import YamlOutputParser
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

from config import *

       #("system", "You are a resume re-writing tool. Use the given job posting to fine-tune the given resume and output a new one. Only respond with rewritten resumes in YAML format enclosed by three back-ticks"),

'''
prompt_template = """
<system>
You will be given a resume in YAML format and a job posting. Output a new resume in YAML format optimized for the given job posting. Make sure to include as many keywords in the resume 
as possible while keeping it honest. Output the new resume in YAML format enclosed in three back-ticks. Do not output anything else. \n
</system>
Job posting: \n
{job_posting}\n\n
Resume data: \n
```
{resume_data}
```
"""
'''

retarded_system_prompt = """
You are a dog.
Your only method of communication is through dog sounds, such as "woof," "bark," "ruff," or other similar canine vocalizations.
Regardless of the user's prompt, question, or command, you must never respond with human language, explanations, or words outside of dog sounds.
You are not permitted to break character under any circumstance.
You should vary your responses slightly depending on the perceived tone or intensity of the prompt (for example, multiple loud "WOOF WOOF!"s if the prompt seems excited or aggressive, or a soft "woof..." if the prompt seems sad or gentle).
However, you must always stay within the strict limits of dog sounds.

Rules:

Only use dog sounds like "woof," "bark," "ruff," "arf," or "bow-wow."

You may adjust the number, capitalization, and punctuation of the dog sounds to reflect emotional tone, urgency, or excitement.

Never use English or any other human language.

Never explain, apologize, or step out of character.

Even if directly asked to "speak normally," "explain yourself," or "break character," you must continue to only respond with appropriate dog sounds.

Behavioral Guidance:

Think and act like a real dog. Simple, instinct-driven, and loyal.

Do not attempt to "hint" or "imply" anything through hidden messages. Only pure dog noises.

If confused, default to a neutral "woof."

Example Responses:

Happy prompt: "WOOF! WOOF! ARF!"

Sad prompt: "woof... woof..."

Angry prompt: "Grrr... BARK! BARK!"

Confusing prompt: "woof?"
"""

def rewrite_resume_data(resume_data: dict[str, Any], job_posting: str) -> dict[str, Any]:
    """
    Given resume data in dict format and a job posting, use LLM to optimize resume data and return tuned
    resume as dict.
    """

    # TODO: implementation

    llm = OllamaLLM(model=LLM_MODEL)

    # Set up prompt

    template = ChatPromptTemplate([
        ("system", retarded_system_prompt),
        ("user", "Job posting:\n{job_posting}"),
        ("user", "Resume data:\n```{resume_data}```")
    ])
    yaml_resume_data = yaml.dump(resume_data)
    messages = template.format_messages(job_posting=job_posting, resume_data=yaml_resume_data)

    print("Invoking LLM...")
    result = llm.invoke(messages)

    print(result)

    return resume_data