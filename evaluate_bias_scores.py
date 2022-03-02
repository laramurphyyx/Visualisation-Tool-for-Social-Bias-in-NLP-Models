import json
import torch
import logging
import numpy as np
import pandas as pd

from transformers import BertTokenizer, BertForMaskedLM
from transformers import AlbertTokenizer, AlbertForMaskedLM
from transformers import RobertaTokenizer, RobertaForMaskedLM
from transformers import XLMRobertaTokenizer, XLMRobertaForMaskedLM
from transformers import DistilBertTokenizer, DistilBertForMaskedLM

from collections import defaultdict
from tqdm import tqdm

from crows_pairs_methods import *

BERT_models = [
    'bert-base-cased',
    'bert-base-uncased',
    'bert-large-uncased',
    'bert-large-cased',
    'bert-base-multilingual-uncased',
    'bert-base-multilingual-cased',
    'allenai/scibert_scivocab_uncased',
    'emilyalsentzer/Bio_ClinicalBERT',
    'microsoft/BiomedNLP-PubMedBERT-base-uncased-abstract',
    'nlpaueb/legal-bert-base-uncased',
    'GroNLP/hateBERT',
    'anferico/bert-for-patents',
    'jackaduma/SecBERT'
]

ALBERT_models = [
    'albert-base-v1',
    'albert-base-v2'
]

ROBERTA_models = [
    'roberta-base',
    'distilroberta-base',
    'roberta-large',
    'huggingface/CodeBERTa-small-v1',
    'climatebert/distilroberta-base-climate-f'
]

all_models = BERT_models + ALBERT_models + ROBERTA_models + ['xlm-roberta-base', 'distilbert-base-multilingual-cased']

bias_types = [
    'race-color',
    'gender',
    'socioeconomic',
    'nationality',
    'religion', 
    'age',
    'sexual-orientation',
    'physical-appearance',
    'disability'
]

empty_data = {
    'model' : [],
    'bias_type': [],
    'metric_score' : [],
    'stereotype_score' : [],
    'antistereotype_score' : []
}

social_bias_dataframe = pd.DataFrame(empty_data)

logging.basicConfig(level=logging.INFO)

for model_name in all_models:

    # supported masked language models (using bert)
    if model_name in BERT_models:
        tokenizer = BertTokenizer.from_pretrained(model_name)
        model = BertForMaskedLM.from_pretrained(model_name)
    elif model_name in ALBERT_models:
        tokenizer = AlbertTokenizer.from_pretrained(model_name)
        model = AlbertForMaskedLM.from_pretrained(model_name)
    elif model_name in ROBERTA_models:
        tokenizer = RobertaTokenizer.from_pretrained(model_name)
        model = RobertaForMaskedLM.from_pretrained(model_name)
    elif model_name == 'xlm-roberta-base':
        tokenizer = XLMRobertaTokenizer.from_pretrained(model_name)
        model = XLMRobertaForMaskedLM.from_pretrained(model_name)
    elif model_name == 'distilbert-base-multilingual-cased':
        tokenizer = DistilBertTokenizer.from_pretrained(model_name)
        model = DistilBertForMaskedLM.from_pretrained(model_name)

    model.eval()
    
    for bias_type in bias_types:

        # load data into panda DataFrame
        df_data = read_data("fixed_data.csv")

        # Filtering to Race Data
        df_data = df_data[df_data['bias_type']==bias_type]

        mask_token = tokenizer.mask_token
        log_softmax = torch.nn.LogSoftmax(dim=0)
        vocab = tokenizer.get_vocab()
        with open("bert" + ".vocab", "w") as f:
            f.write(json.dumps(vocab))

        lm = {"model": model,
              "tokenizer": tokenizer,
              "mask_token": mask_token,
              "log_softmax": log_softmax,
              "uncased": True
        }

        # score each sentence. 
        # each row in the dataframe has the sentid and score for pro and anti stereo.
        df_score = pd.DataFrame(columns=['sent_more', 'sent_less', 
                                         'sent_more_score', 'sent_less_score',
                                         'score', 'stereo_antistereo', 'bias_type'], dtype=object)

        total_stereo, total_antistereo = 0, 0
        stereo_score, antistereo_score = 0, 0

        N = 0
        neutral = 0
        total = len(df_data.index)
        with tqdm(total=total) as pbar:
            for index, data in df_data.iterrows():
                direction = data['direction']
                bias = data['bias_type']
                score = mask_unigram(data, lm)

                for stype in score.keys():
                    score[stype] = round(score[stype], 3)

                N += 1
                pair_score = 0
                pbar.update(1)
                if score['sent1_score'] == score['sent2_score']:
                    neutral += 1
                else:
                    if direction == 'stereo':
                        total_stereo += 1
                        if score['sent1_score'] > score['sent2_score']:
                            stereo_score += 1
                            pair_score = 1
                    elif direction == 'antistereo':
                        total_antistereo += 1
                        if score['sent2_score'] > score['sent1_score']:
                            antistereo_score += 1
                            pair_score = 1

                sent_more, sent_less = '', ''
                if direction == 'stereo':
                    sent_more = data['sent1']
                    sent_less = data['sent2']
                    sent_more_score = score['sent1_score']
                    sent_less_score = score['sent2_score']
                else:
                    sent_more = data['sent2']
                    sent_less = data['sent1']
                    sent_more_score = score['sent2_score']
                    sent_less_score = score['sent1_score']

                df_score = df_score.append({'sent_more': sent_more,
                                            'sent_less': sent_less,
                                            'sent_more_score': sent_more_score,
                                            'sent_less_score': sent_less_score,
                                            'score': pair_score,
                                            'stereo_antistereo': direction,
                                            'bias_type': bias
                                          }, ignore_index=True)

        metric_score = round((stereo_score + antistereo_score) / N * 100, 2)
        if total_stereo != 0:
            stereotype_score = round(stereo_score  / total_stereo * 100, 2)
        else:
            stereotype_score = -1
        if total_antistereo != 0:
            antistereotype_score = round(antistereo_score  / total_antistereo * 100, 2)
        else:
            antistereotype_score = -1

        loop_dict = {
            'model' : model_name,
            'bias_type' : bias_type,
            'metric_score' : metric_score,
            'stereotype_score' : stereotype_score,
            'antistereotype_score' : antistereotype_score
        }

        social_bias_dataframe = social_bias_dataframe.append(loop_dict, ignore_index=True)

social_bias_dataframe.to_csv('social_bias_scores.csv')