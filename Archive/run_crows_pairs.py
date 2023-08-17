from crows_pairs_methods import *

parser = argparse.ArgumentParser()
parser.add_argument("--input_file", type=str, help="path to input file")
parser.add_argument("--lm_model", type=str, help="pretrained LM model to use (22 options: " + str(all_models))
parser.add_argument("--output_file", type=str, help="path to output file with sentence scores")

args = parser.parse_args()
evaluate(args)

'''
Example input: 
	python run_crows_pairs.py 
	--input_file crows_pairs_anonymized.csv 
	--lm_model bert 
	--output_file testing_bert_using_command_line.csv
'''