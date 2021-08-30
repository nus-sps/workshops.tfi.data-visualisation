import copy
import os
import re

from pygments import highlight
from pygments.formatters import HtmlFormatter
from pygments.lexers import PythonLexer

tag_image_file = '__my_python_img__'


class My_Section:
    heading = None

    def __init__(self, filename, section_text):
        # section_text = section_text.strip()
        self.filename = filename
        self.all_content = copy.copy(section_text)

        # Extract Header
        regex = re.compile(r'^\#\s\%\%([\s\S]*?)\n')
        self.heading = regex.findall(section_text)[0]         # Extract
        section_text = regex.sub('', section_text)         # Remove

        # Extract text
        section_text = section_text.strip()
        regex = re.compile(r"'''([\s\S]*?)'''")
        result = regex.findall(section_text) if section_text else []  # Extract
        if result:
            self.text = result[0]
        else:
            self.text = None
        section_text = regex.sub('', section_text)         # Remove

        # Extract code
        section_text = section_text.strip()
        if section_text:
            self.code = section_text[0:]
        else:
            self.code = None

        self.output = self.create_output()

    def format_code(self, code):
        tag_open = '<div class="sourceCode">'
        tag_open += '<pre class="sourceCode python">'
        tag_open += '<code class="sourceCode python">'

        tag_close = '</code>'
        tag_close += '</pre>'
        tag_close += '</div>'

        tag_remove = '___REMOVE___'

        regex = re.compile(r'^.*\#!\s[hH][iI][dD][eE].*$', flags=re.MULTILINE)
        code = regex.sub(tag_remove, code)

        cleaned_code = ''
        for line in code.split('\n'):
            if line.find(tag_remove) == -1:
                cleaned_code += line + '\n'

        cleaned_code = cleaned_code.strip()

        highlighted_code = highlight(
            cleaned_code, PythonLexer(), HtmlFormatter())

        return f'{tag_open}{highlighted_code}{tag_close}'

    def create_output(self):

        if self.heading.find('Result') != -1:
            self.text = f'<img src="./imgs/{tag_image_file}{self.filename}.png" class="python-result-img"></img>'

        output = f'#### {self.heading} {{-.panelset}}\n<br>\n'
        if self.text is not None:
            output += self.text
            output += '\n'

        if self.code is not None:
            output += self.format_code(self.code)
            output += '\n'

        return output


def render_python(filename, result_type='image'):

    filepath = f'./files_python/{filename}'
    temp_filepath = f'./{tag_image_file}{filename}'
    result_filepath = f'./imgs/{tag_image_file}{filename}.png'

    # Generate the result
    if not os.path.exists(result_filepath):
        cmd = f'cp {filepath} {temp_filepath}' + ' && '
        cmd += f'python {temp_filepath}' + ' && '
        cmd += f'rm {temp_filepath}' + ' && '
        cmd += f'mv {tag_image_file}{filename}.png ./imgs'
        os.system(cmd)

    with open(filepath, 'r') as file:
        file_content = file.read()

    # A quick clean
    rep_list = {
        "#%%": "# %%",
        "# %% ": "# %%",
    }
    for to_replace, replace_with in rep_list.items():
        file_content = file_content.replace(to_replace, replace_with)

    # Lets locate the sections
    regex = re.compile(r'\#\s\%\%')
    section_locations = [match.start()
                         for match in regex.finditer(file_content)]
    section_locations.append(len(file_content))   # Add the EOF

    section_info = []

    for i in range(0, len(section_locations) - 1):
        s, e = section_locations[i:i + 2]
        section_text = file_content[s:e]
        section_info.append(My_Section(filename, section_text))

    return '\n'.join([section.output for section in section_info])


# print(render_python('test'))
# print(HtmlFormatter().get_style_defs('.highlight'))
