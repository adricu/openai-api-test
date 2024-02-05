#  Basic PDF Summarization and Query System

Create a basic script that extracts text from a PDF by chapter, summarizes each chapter, stores these summaries in an SQLite database, and answers questions about these chapters using OpenAI's API.

## Running the script

You just need to create an `.env` file and place there the OPENAPI api key.

To run execute the script:

`python -m task`

## Approach

- I did the task in the simplest way possible by covering the functionality asked in the assignment
- Used [PyMuPDF](https://pypi.org/project/PyMuPDF/) library to read and process the PDF
- Used openai async client
- Used [Chat completions API](https://platform.openai.com/docs/guides/text-generation/chat-completions-api) to generate text summaries and ask questions about them

## Assumptions

- There is an "easy" way to split the pdf file in chapters by executing a regex expression [here](task/text_processing.py). It can be tweaked depending of the PDF structure.
- The PDF to work with is called `test.pdf`. It can be changed [here](task/__main__.py)
