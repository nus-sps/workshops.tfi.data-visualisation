import copy
import glob
import os
import re

from pygments import highlight
from pygments.formatters import HtmlFormatter
from pygments.lexers import PythonLexer

tag_output_file = '__my_python_output__'


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

        self.create_output()

    def format_code(self, code):
        tag_open = '<div class="sourceCode">'
        tag_open += '<pre class="sourceCode python">'
        tag_open += '<code class="sourceCode python">'

        tag_close = '</code>'
        tag_close += '</pre>'
        tag_close += '</div>'

        tag_remove = '___REMOVE___'

        regex = re.compile(r'^.*\#\s*[hH][iI][dD][eE].*$', flags=re.MULTILINE)
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

        # if self.heading.find('Result') != -1:
            # self.text = f'<img src="python_outputs/{tag_output_file}{self.filename}.png" class="python-result-img"></img>'

        output = f'#### {self.heading} {{-.panelset}}\n<br>\n'
        if self.text is not None:
            output += self.text
            output += '\n'

        if self.code is not None:
            output += self.format_code(self.code)
            output += '\n'

        self.output = output


def render_python(filename, result_type='image'):
    py_filepath = f'files_python/{filename}'
    with open(py_filepath, 'r',encoding='UTF-8') as file:
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

    # Analyse the sections
    for i in range(0, len(section_locations) - 1):
        s, e = section_locations[i:i + 2]
        section_text = file_content[s:e]
        section_info.append(My_Section(filename, section_text))

    # Is there a results section?
    for section in section_info:
        if section.heading.find('Result') != -1:
            section.text = create_result_output(filename)
            section.create_output()

    return '\n'.join([section.output for section in section_info])


def create_result_output(filename):
    py_filepath = f'files_python/{filename}'
    temp_py_filepath = f'{tag_output_file}{filename}'

    result_files = glob.glob(f'python_outputs/*{filename}*')

    if not result_files:
        cmd = f'cp {py_filepath} {temp_py_filepath}' + ' && '
        cmd += f'python {temp_py_filepath}' + ' && '
        cmd += f'rm {temp_py_filepath}' + ' && '
        cmd += f'mv {tag_output_file}{filename}.* python_outputs'
        os.system(cmd)
        result_files = glob.glob(f'python_outputs/*{filename}*')

    result_filename = result_files[0];
    result_fileext = result_filename.split('.')
    result_fileext = result_fileext[-1]

    if result_fileext == 'html':
        with open(result_filename,'r') as file:
            output = file.read()
    else:
        output =  f'<img src="{result_filename}" class="python-result-img"></img>'

    return output

#print(render_python('a-simple-plot.py'))
# print(render_python('covid-subset-asean.py'))
# print(HtmlFormatter().get_style_defs('.highlight'))
