# auto-resume-tuner
A Python tool that uses AI to tailor resumes written in Latex for specific job postings

## Setup Instructions

### Setting up Python Prerequisites

It is recommended that you use a virtual environment, however this is not a requirement.
To set up a virtual environment, run the following command

```
$ python -m venv env/
```
This will create a new virtual environment in the env/ directory.

At the beginning of any session in your command line, you will need to activate your virtual environment by running the following command

```
$ source env/Scripts/activate
```

Or if you are using PowerShell, like a pleb, you can run this:

```
> .\env\Scripts\activate
```

### Installing Required Python Packages

All the necessary Python packages are stored in `requirements.txt`. To install all the requirements, simply run:
```
$ pip install -r requirements.txt
```

This will install all the necessary Python packages.

### Setting up LaTeX

To run the PDF generation portion of the script, you will need to download and install a LaTeX distribution on your system. It doesn't really matter which one, you can either download [MikTeX](https://miktex.org/) or [TeX Live](https://www.tug.org/texlive/).

### Ollama Set-up

If you want to run an LLM locally (which you will need to do if you wanna test), you'll need to download [Ollama](https://ollama.com/) set up. Once you have done this, you'll need to download a model. This is generally pretty simple, you just search for the model you want on [Ollama's search page](https://ollama.com/search). Once you see a model you want (e.g. gemma3), you can pull the model by running the following:
```
$ ollama pull <model-name>
```
You can set the model you want to use in the `config.py` file by modifying the `LLM_MODEL` variable. Make sure that the model set in this variable has been installed on your machine.

You may notice that the `base_url` argument is used in `llm_utils.py` to connect remotely to another computer running Ollama. This is an option if you can't run your model locally, but if you want to run your model locally and use it, simply remove the `base_url` parameter from the initialization of the Ollama client and all models will be run locally.

## How to Use Everything

Once everything has been set up, you can run the script by running the `main.py` file:
```
$ python main.py
```

This will run the script, invoke the LLM and generate the PDF file.

If you wanna get some actual use out of this though, you're gonna need to customize the included resume data and templates

### Setting up your Resume Data and Templates

Raw resume data is stored in the `resume-content.yaml` file. You can customize this to include as much raw data of your own as you'd like. You can treat it as your master resume. The optimizer should include the most relevant content for you and trim it down.

### Customizing your Resume Template

There is a Jinja2 resume template is located in `templates/resume.tex`. This template defines the formatting for the resume. You can customize this so that the generated resume is formatted however you please. Refer to the [Jinja2 documentation](https://jinja.palletsprojects.com/en/stable/templates/) for help on how to format this.