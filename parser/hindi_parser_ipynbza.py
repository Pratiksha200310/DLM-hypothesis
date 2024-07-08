# -*- coding: utf-8 -*-
"""Hindi parser.ipynbza

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/19HToJGJtPoIfXCsgnpVorm2x2L2gznEk
"""

!pip install torch torchvision -f https://download.pytorch.org/whl/torch_stable.html
!pip install stanza

import stanza

!pip install python-docx

import stanza
from docx import Document
from docx.shared import Pt
from google.colab import files
import time

# Upload the file
uploaded = files.upload()

# Get the uploaded file name
filename = list(uploaded.keys())[0]

# Read the content of the uploaded file
with open(filename, 'r', encoding='utf-8') as file:
    text = file.read()

# Download Hindi model if not already downloaded
stanza.download('hi')

# Initialize Stanza pipeline for Hindi
nlp = stanza.Pipeline('hi')

# Process the text with Stanza
doc = nlp(text)

# Create a new Word document
docx_filename = 'parsed_data.docx'
document = Document()

# Add a title
document.add_heading('Parsed Data', level=1)

# in conll format
conll_format = ""
for sentence in doc.sentences:
    for word in sentence.words:
        conll_format += "{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(
            word.id,       # ID
            word.text,     # Text
            word.lemma,    # Lemma
            word.upos,     # UPOS
            word.xpos,     # XPOS
            word.head,     # Head
            word.deprel,   # Deprel
            word.start_char,  # Start Char
            word.end_char,    # End Char
            abs(word.id - word.head)  # Dependency Length
        )
    conll_format += "\n"

# Save the CoNLL format text to a file
conll_filename = 'parsed_data.conll'
with open(conll_filename, 'w', encoding='utf-8') as file:
    file.write(conll_format)

# Download the file
files.download(conll_filename)