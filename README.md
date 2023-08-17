# CA4021: Visualisation Tool for Social Bias in NLP Models

## Project Description

This project aims to highlight the presence of social biases that have been trained into language models through visualisation. 

This project improved the quality and reliability of an existing social bias benchmark dataset, [CrowS-Pairs](https://github.com/nyu-mll/crows-pairs). This was done in three iterations, the first two iterations focussed on correcting sentences with incorrect structure or spelling errors, and the third iteration dealt with inconsistent punctuation. From the first two iterations, a total of 425 sentences were manually verified and 144 of them were updated.

The methods of improving the data collection process for training language models were also explored. This project has used the updated version of the CrowS-Pairs dataset to train a BERT binary classifier to identify stereotyped and non-stereotyped sentences. This identifier achieved an overall accuracy of 75%, although only received a 'true' accuracy of 57% (more info in the notebook '[Fine_Tuning_BERT_on_Stereotyped_data](https://gitlab.computing.dcu.ie/murpl239/2022-ca4021-murpl239/-/blob/master/BERT%20Classifier/Fine_Tuning_BERT_on_Stereotyped_data.ipynb)'). 

This project also introduces a more efficient metric, a neutrality metric, to measure how fair a language model is. Originally, CrowS-Pairs had only measured a 'metric_score', which represented the proportion of sentence pairs where the model assigned a higher probability to the sentence pair. This score could not differentiate between sentence pairs with a large difference in probabilities and pairs with almost identical probabilities. By introducing a threshold, a neutrality score can be measured. The threshold assigns a value to how different the probabilities of two sentences have to be before it is considered biased or not biased. This threshold can be any value from 0-1.

Using the updated dataset as our test set, and our new neutrality metric, visualisations are created and made available on the front end. The visualisations include various types of bar charts and radar charts, produced using a Python package, Plotly. This package allows for visualisations to be interactive, and can be integrated seamlessly using Flask, a web framework.

## Repository Structure

The repository is structured as follows:

<u>Directories:</u>
* [All Output Files](All%20Output%20Files): This directory contains three sub-directories. Each sub-directory corresponds to the results obtained on all 22 language models using the original CrowS-Pairs dataset, the updated version after iteration 1, and the final updated version of the dataset. It also contains the master file used to compute all visualisations in real-time.
* [Archive](Archive): This directory contains various notebooks that have been used throughout the project. Some of these notebooks have been used to explore different areas, some were used to produce the output files, and some were just original copies of notebooks that have later been summarised/expanded on.
* [BERT Classifier](BERT%20Classifier): This directory contains a notebook to manipulate the updated CrowS-Pairs dataset into a training file and a testing file (also contained in this directory). There is also a notebook that fine-tunes BERT and contains the accuracy and short analysis on performance.
* [Front End](Front%20End): This is the directory containing the files required to run the front end. The front end can be created by cloning this repo, and running 'python -m flask run' in the terminal in this directory (Note: this requires the [master output file](https://gitlab.computing.dcu.ie/murpl239/2022-ca4021-murpl239/-/blob/master/All%20Output%20Files/master_output_file.zip) to be unzipped and located in the parent directory).
* [Graphics and Demos](Graphics%20and%20Demos): This directory contains images used in the report, such as diagrams and visual examples, and screenshots of the charts created. There is also two videos, one to show an interactive slider bar bar chart, and one to show a demo of the front end site.
* [docs](docs): This folder contains the submission files for the final report and presentation. Also in this directory is the submission of the proposal and the ethics documentation.

<u>Notebooks:</u>
* [Analysis - Comparison of Original and Updated Datasets](Analysis%20-%20Comparison%20of%20Original%20and%20Updated%20Datasets.ipynb): This notebook performs analyses on the effects of each iteration of cleaning on the original dataset.
* [Analysis - Effects of Adding Thresholds](Analysis%20-%20Effects%20of%20Adding%20Thresholds.ipynb): This notebook performs analyses on the effect of adding a threshold and neutrality score (to replace the original 'metric_score').
* [Fixing Errors in Dataset Pt. 1](Fixing%20Errors%20in%20Dataset%20Pt.%201.ipynb): This notebook goes through the first iteration of cleaning. This notebook verifies 217 sentences that have mismatched lengths, and goes into detail for each of the 63 sentence pairs that had to be updated.
* [Fixing Errors in Dataset Pt. 2](Fixing%20Errors%20in%20Dataset%20Pt.%202.ipynb): This notebook performs the second iteration of cleaning, by identifying sentences with differing vocabulary. Through verifying the vocabulary lists, 81 of 208 identified sentences had to be updated in this notebook.
* [Fixing Errors in Dataset Pt. 3](Fixing%20Errors%20in%20Dataset%20Pt.%203.ipynb): This notebook adds punctuation to all sentence pairs, to prevent unpredictable behaviour from language models. This is an automated process that updated 153 sentence pairs.
* [Replicating CrowS-Pairs Results](Replicating%20CrowS-Pairs%20Results.ipynb): This notebook shows the process of replicating the CrowS-Pairs results to ensure sound usage of their methodology.
* [Visualisations](Visualisations.ipynb): This notebook contains a series of visualisations that show the different ways the data produced can be visualised. This is an extensive list with different variations of the same chart, the charts available via the front end is a more compact series of visualisations, available through [this notebook](Front%20End/Visualisation%20Functions.ipynb)

<u>Python Scripts:</u>
* [crows_pairs_methods](crows_pairs_methods.py): This is a python script that contains all the functions required to test a language model against the test dataset.
* [functions](functions.py): This is a python script to store various functions that can be used for various tasks throughout the project, primarily to calculate scores using the master dataset in real-time.
* [variables](variables.py)	: This is a python script to store recurring variable names, such as model names and bias types.
