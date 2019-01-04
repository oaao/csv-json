import csv
import json

import argparse


def convert(csv_name, csv_delim, json_name, json_indent):
    
    with open('{}.csv'.format(csv_name), newline='') as f_input:
        csv_read = csv.DictReader(f_input, delimiter=csv_delim)
        data     = list(csv_read)
        
    with open('{}.json'.format(json_name), 'w') as f_output:
        json.dump(data, f_output, indent=json_indent)


def parse_args():
    
    p_arg = argparse.ArgumentParser()
    
    p_arg.add_argument('-i', '--input', help='input filename, no extension', dest='csv', required=True, type=str)
    p_arg.add_argument('-o', '--output', help='output filename, no extension', dest='json', required=True, type=str)
    p_arg.add_argument('--indent', help='optional indentation for JSON', dest='indent', type=int, default=0)
    p_arg.add_argument('-d', '--delimiter', help='delimiter character', dest='delimiter', type=str, default=',')
    
    parsed_args = p_arg.parse_args()
    
    return parsed_args

if __name__ == "__main__":
    args = parse_args()
    convert(args.csv, args.delimiter, args.json, args.indent)
