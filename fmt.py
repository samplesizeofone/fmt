#!/usr/bin/python
import argparse
import jinja2
import ast
import re

def fmt(template_file, kv):
    with open(arguments.template[0], 'r') as template_file:
        raw_template = template_file.read()

        raw_template = re.sub(r'\[\[\s*\{', '{', raw_template, flags=re.M)
        raw_template = re.sub(r'\}\s*\]\]', '}', raw_template, flags=re.M)
        raw_template = re.sub(r'\[\[\s*\]\]', '', raw_template, flags=re.M)

        raw_template = re.sub(r'\[\\(\\*)\[', '[\\1]', raw_template)
        raw_template = re.sub(r'\]\\(\\*)\]', '[\\1]', raw_template)

        template = jinja2.Template(raw_template)

    return template.render(**kv)

if __name__ == '__main__':
    argument_parser = argparse.ArgumentParser()
    argument_parser.add_argument('--template', metavar='T', nargs=1, help='The Jinja2 template to be rendered')
    argument_parser.add_argument('--kv', metavar='K', nargs=2, action='append', default=None, help='A key value pair defining a template variable')
    argument_parser.add_argument('--kf', metavar='F', nargs=2, action='append', default=None, help='A key file pair. The contents of the file will be used as the value of the template variable')
    argument_parser.add_argument('--dict-file', metavar='D', nargs=1, default=None, help='A file containing a Python style dictionary mapping template variables to Python values')
    argument_parser.add_argument('--stdin', default=None, action='store_true', help='Read a Python style dictionary mapping template variables to Python values from stdin')

    arguments = argument_parser.parse_args()

    kv = {}

    if arguments.stdin is not None:
        kv.update(ast.literal_eval(stdin.read()))
    else:
        if arguments.kv is not None:
            kv.update(dict(arguments.kv))

        if arguments.kf is not None:
            kf = {} 
            for (key, filename) in arguments.kf:
                with open(filename, 'r') as in_file:
                    kf[key] = in_file.read()

            kv.update(kf)

        if arguments.dict_file is not None:
            with open(arguments.dict_file[0], 'r') as dict_file:
                kv.update(ast.literal_eval(dict_file.read()))

    print fmt(arguments.template[0], kv)
