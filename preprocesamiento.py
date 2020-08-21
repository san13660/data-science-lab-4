import re
import sys

def process_line(line):
    processed = line.lower()
    processed = processed.replace('#','')
    processed = processed.replace('@','')
    processed = processed.replace("’re",' are')
    processed = processed.replace("n’t",' not')
    processed = processed.replace("’ve",' have')
    processed = processed.replace("’ll",'')
    processed = processed.replace("’s",'')
    processed = processed.replace("’d",'')
    
    processed = processed.replace('_',' ')
    processed = processed.replace('-',' ')
    processed = processed.replace('–',' ')
    processed = processed.replace('—',' ')
    processed = processed.replace("/",' ')

    processed = processed.replace(' a ',' ')
    processed = processed.replace(' of ',' ')
    processed = processed.replace(' to ',' ')
    processed = processed.replace(' the ',' ')
    processed = processed.replace(' and ',' ')
    processed = processed.replace(' for ',' ')
    processed = processed.replace(' but ',' ')
    processed = processed.replace(' or ',' ')
    processed = processed.replace(' yet ',' ')
    processed = processed.replace(' so ',' ')
    processed = processed.replace(' as ',' ')
    processed = processed.replace(' either ',' ')
    processed = processed.replace(' nor ',' ')
    processed = processed.replace(' until ',' ')
    processed = processed.replace(' that ',' ')
    processed = processed.replace(' which ',' ')
    processed = processed.replace(' where ',' ')
    processed = processed.replace(' while ',' ')

    whitelist = set('abcdefghijklmnopqrstuvwxyz ')
    processed = ''.join(filter(whitelist.__contains__, processed))

    processed = " ".join(processed.split())
    return processed

with open(sys.argv[1], 'r', encoding='utf-8') as infile:
    for line in infile:
        line = process_line(line)
        with open('preprocesado_'+sys.argv[1], 'a', encoding='utf-8') as the_file:
            the_file.write(line + '\n')