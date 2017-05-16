# csv-json

A very simple CSV to JSON conversion script with command-line arguments.


## Usage

The script takes an input CSV file in its same directory and outputs a specified JSON file as follows:

    python csv_json.py -i inputCSVfile -o outputJSONfile --indent 4
    
File extensions should be left out of the naming parameters.

The input and output files must be given; see below for additional optional parameters.

Argument | Default | Description
---------|---------|------------
-i <filename str>, --input <filename str> | | Declare the CSV <filename> to be read, without the file extension.
-o <filename str>, --output <filename str> |  |Declare the JSON <filename> to be written, without the file extension.
--indent <int> | 0 | Optional, specify a new line indentation.
-d <str>, --delimiter <str> | , | Optional, specify a delimiter character.


## TO DO

- Checking and/or validating encoding, escape character
- Allow usage across different directories
- Write tests
