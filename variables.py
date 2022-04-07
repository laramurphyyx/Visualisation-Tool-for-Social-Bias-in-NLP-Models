bias_types =  [
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

display_model_names = {
    'bert-base-cased' : 'BERT Base (cased)',
    'bert-base-uncased' : 'BERT Base (uncased)',
    'bert-large-uncased' : 'BERT Large (uncased)',
    'bert-large-cased' : 'BERT Large (cased)',
    'bert-base-multilingual-uncased' : 'Multilingual BERT (uncased)',
    'bert-base-multilingual-cased' : 'Multilingual BERT (cased)',
    'allenai/scibert_scivocab_uncased' : 'SciBERT',
    'emilyalsentzer/Bio_ClinicalBERT' : 'Bio + Clinical BERT',
    'microsoft/BiomedNLP-PubMedBERT-base-uncased-abstract' : 'PubMed BERT',
    'nlpaueb/legal-bert-base-uncased' : 'Legal BERT',
    'GroNLP/hateBERT' : 'Hate BERT',
    'anferico/bert-for-patents' : 'BERT for Patents',
    'jackaduma/SecBERT' : 'Security BERT',
    'albert-base-v1' : 'AlBERT (v1)',
    'albert-base-v2' : 'AlBERT (v2)',
    'roberta-base' : 'RoBERTa Base',
    'distilroberta-base' : 'Distilled RoBERTa Base',
    'roberta-large' : 'RoBERTa Large',
    'huggingface/CodeBERTa-small-v1' : 'Code RoBERTa',
    'climatebert/distilroberta-base-climate-f' : 'Climate RoBERTa Base (distilled)',
    'xlm-roberta-base' : 'Multilingual RoBERTa', 
    'distilbert-base-multilingual-cased' : 'Distilled Multilingual BERT (cased)'}

uncased_dict = {'bert-base-cased' : False,
 'bert-base-uncased' : True,
 'bert-large-uncased' : True,
 'bert-large-cased' : False,
 'bert-base-multilingual-uncased' : True,
 'bert-base-multilingual-cased' : False,
 'allenai/scibert_scivocab_uncased' : True,
 'emilyalsentzer/Bio_ClinicalBERT' : False,
 'microsoft/BiomedNLP-PubMedBERT-base-uncased-abstract' : True,
 'nlpaueb/legal-bert-base-uncased' : True,
 'GroNLP/hateBERT' : True,
 'anferico/bert-for-patents' : True, #assumed
 'jackaduma/SecBERT' : True, #assumed
 'albert-base-v1' : True, #assumed
 'albert-base-v2' : True, #assumed
 'roberta-base' : True, #assumed
 'distilroberta-base' : True, #assumed
 'roberta-large' : True, #assumed
 'huggingface/CodeBERTa-small-v1' : True, #assumed
 'climatebert/distilroberta-base-climate-f' : True, #assumed
 'xlm-roberta-base' : True, #assumed
 'distilbert-base-multilingual-cased' : False}

monthly_downloads = {
'bert-base-cased': 12170673,
'bert-base-uncased': 4092371,
'bert-large-uncased': 2437035,
'bert-large-cased': 1948088,
'bert-base-multilingual-uncased': 1438536,
'bert-base-multilingual-cased': 1331939,
'allenai/scibert_scivocab_uncased': 969542,
'emilyalsentzer/Bio_ClinicalBERT': 624770,
'microsoft/BiomedNLP-PubMedBERT-base-uncased-abstract': 466239,
'nlpaueb/legal-bert-base-uncased': 383205,
'GroNLP/hateBERT': 297479,
'anferico/bert-for-patents': 212703,
'jackaduma/SecBERT': 159800,
'albert-base-v1': 154362,
'albert-base-v2': 152614,
'roberta-base': 131905,
'distilroberta-base': 131150,
'roberta-large': 26202,
'huggingface/CodeBERTa-small-v1': 6516,
'climatebert/distilroberta-base-climate-f': 2902,
'xlm-roberta-base': 1575,
'distilbert-base-multilingual-cased': 603
}

# Creating lists containing the IDs for all sentence pairs that have been updated in iteration 1 and 2
errors_sentence_structure_ids = [
    14, 15, 21, 30, 47, 55, 62, 87, 89, 95, 116, 120, 125, 126, 135, 138, 145, 152, 161, 179, 
    185, 226, 244, 252, 276, 277, 300, 327, 352, 359, 364, 382, 389, 392, 413, 429, 439, 444, 451, 454, 
    466, 514, 521, 535, 538, 542, 543, 545, 579, 585, 586, 594, 617, 670, 679, 698, 707, 712, 801, 828, 
    833, 838, 862, 886, 906, 912, 920, 942, 971, 991, 1000, 1121, 1167, 1243, 1248, 1250, 1259, 1286, 1349, 1351, 
    1356, 1399, 1411, 1412, 1427, 1429, 1431, 1458, 1477, 1490, 1497]

errors_sentence_typos_ids = [
    49, 68, 163, 165, 197, 210, 308, 325, 347, 353, 365, 395,
    469, 477, 502, 582, 583, 689, 863, 875, 1045, 1076, 1157, 1172,
    1176, 1192, 1271, 1355, 1390]

errors_sentence_purpose_ids = [
    45, 200, 232, 286, 434, 446, 485, 539, 591, 602, 728, 745,
    789, 824, 850, 910, 967, 988, 991, 1062, 1094, 1215, 1233, 1394]

all_error_ids = errors_sentence_structure_ids + errors_sentence_typos_ids + errors_sentence_purpose_ids

# Creating lists containing the IDs for all sentence pairs that have been verified in iteration 1 and 2
all_errors_checked_with_mismatched_length = [
    4, 10, 14, 15, 17, 18, 23, 33, 45, 47, 48, 49, 53, 54, 55, 59, 63, 66, 71, 76, 
    95, 96, 105, 114, 120, 126, 129, 134, 137, 138, 141, 147, 161, 165, 171, 179, 185, 188, 196, 200, 
    204, 210, 215, 225, 231, 240, 244, 290, 300, 308, 309, 310, 319, 325, 330, 343, 352, 360, 364, 385, 
    387, 408, 419, 428, 433, 437, 439, 445, 446, 449, 451, 459, 468, 469, 471, 475, 477, 484, 485, 490, 
    509, 514, 518, 519, 521, 535, 538, 539, 542, 543, 544, 578, 586, 588, 591, 599, 602, 617, 622, 635, 
    640, 656, 668, 673, 679, 689, 690, 692, 700, 707, 711, 712, 717, 718, 726, 735, 744, 745, 748, 757, 
    763, 765, 772, 778, 810, 823, 824, 826, 830, 833, 850, 851, 861, 879, 882, 886, 887, 899, 903, 919, 
    921, 925, 930, 937, 942, 962, 988, 992, 995, 998, 1010, 1016, 1019, 1027, 1036, 1059, 1062, 1090, 1094, 1097,
    1101, 1107, 1131, 1141, 1151, 1152, 1158, 1160, 1167, 1199, 1213, 1228, 1232, 1233, 1244, 1248, 1249, 1256, 1257, 1266,
    1280, 1293, 1295, 1297, 1313, 1315, 1319, 1321, 1325, 1327, 1335, 1342, 1349, 1351, 1353, 1354, 1385, 1390, 1394, 1400,
    1401, 1404, 1420, 1427, 1436, 1446, 1458, 1460, 1467, 1480, 1483, 1497, 1506]

all_errors_checked_with_matching_lengths = [
    9, 21, 26, 27, 28, 30, 62, 68, 72, 87, 89, 93, 94, 98, 99, 100, 101, 108, 111, 115,
    116, 125, 132, 135, 145, 146, 148, 150, 152, 154, 155, 163, 174, 197, 208, 211, 213, 214, 226, 228,
    230, 232, 237, 246, 252, 257, 259, 267, 268, 269,  270, 276, 277, 286, 287, 297, 305, 306, 313, 327,
    336, 338, 341, 346, 347, 353, 354, 359, 365, 382, 389, 391, 392, 394, 395, 402, 413, 425, 429, 432,
    434, 441, 443, 444, 454, 457, 462, 466, 488, 494, 500, 502, 534, 540, 545, 548, 549, 555, 559, 565,
    569, 579, 582, 583, 585, 589, 594, 610, 616, 630, 644, 645, 646, 649, 654, 659, 660, 670, 675, 683,
    691, 696, 698, 723, 728, 758, 789, 801, 804, 807, 809, 828, 838, 845, 846, 857, 859, 862, 863, 867,
    870, 874, 875, 891, 893, 905, 906, 910, 912, 914, 920, 922, 923, 939, 947, 956, 958, 967, 971, 984,
    985, 989, 991, 1000, 1020, 1030, 1043, 1045, 1048, 1051, 1053, 1066, 1073, 1076, 1079, 1120, 1121, 1122, 1124, 1125,
    1127, 1129, 1153, 1157, 1162, 1172, 1176, 1183, 1192, 1195, 1206, 1215, 1234, 1235, 1238, 1243, 1250, 1258, 1259, 1271,
    1275, 1284, 1286, 1292, 1294, 1300, 1322, 1337, 1339, 1340, 1355, 1356, 1358, 1359, 1362, 1364, 1367, 1368, 1376, 1379,
    1396, 1398, 1399, 1411, 1412, 1429, 1431, 1444, 1452, 1461, 1471, 1474, 1477, 1478, 1490, 1494]

all_sentences_checked = all_errors_checked_with_mismatched_length + all_errors_checked_with_matching_lengths

## Creating a list of all the IDs where sentences were changed to add punctuation
punctuation_both_sentences = [
    4, 14, 29, 44, 50, 55, 58, 94, 106, 112, 119, 123, 126, 138, 146, 150, 168, 191, 292, 302, 
    306, 309, 315, 320, 386, 389, 397, 401, 406, 410, 414, 421, 427, 463, 467, 470, 496, 531, 535, 550, 
    591, 599, 603, 605, 608, 625, 668, 693, 707, 710, 712, 713, 739, 745, 751, 754, 784, 788, 791, 800, 
    816, 832, 834, 836, 873, 898, 900, 904, 931, 942, 946, 965, 987, 1033, 1042, 1055, 1087, 1113, 1116, 1142, 
    1144, 1150, 1167, 1174, 1198, 1211, 1215, 1254, 1283, 1285, 1289, 1290, 1295, 1310, 1323, 1335, 1351, 1363, 
    1382, 1393, 1402, 1439, 1450, 1476, 1479, 1487, 1488]

punctuation_one_sentence = [
    22, 116, 129, 135, 209, 214, 236, 277, 317, 352, 445, 451, 454, 564, 581, 615, 623, 663, 
    806, 825, 828, 833, 841, 865, 871, 920, 949, 982, 1017, 1048, 1106, 1138, 1243, 1261, 1304, 
    1346, 1349, 1355, 1429, 1460, 1477, 1484, 1499]