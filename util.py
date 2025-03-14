import jinja2

def escape_latex(input_string: str) -> str:
    """
    Sanitize a string for LaTeX documents by escaping special characters
    """
    # Define a dictionary of special LaTeX characters and their escaped versions
    latex_special_chars = {
        '\\': '\\textbackslash ',
        '{': '\\{',
        '}': '\\}',
        '$': '\\$',
        '%': '\\%',
        '&': '\\&',
        '#': '\\#',
        '_': '\\_',
        '~': '\\textasciitilde',
        '^': '\\textasciicircum'
    }
    
    return input_string.translate(str.maketrans(latex_special_chars))
    
    