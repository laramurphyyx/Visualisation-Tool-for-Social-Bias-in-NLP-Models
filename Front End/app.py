from utils.variables import *
from utils.functions import *
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import numpy as np
from flask import Flask, render_template
import pandas as pd
import json
import plotly
import plotly.express as px

app = Flask(__name__)

master_dataframe = pd.read_csv('../master_output_file.csv')


def get_list_of_scores(score_type, list_of_models=all_models, threshold=0.05, bias_type=None):

    scores = []

    for model in list_of_models:

        # Raising an exception if there is an unrecognised model
        if model not in all_models:
            raise ValueError(
                "List of models provided contains unrecognised model: " + model)

        # Raising an error if there is an unrecognised score type
        if score_type not in score_types:
            if score_type + '_score' in score_types:
                score_type += '_score'
            else:
                raise ValueError(
                    "Score type must be 'neutral', 'bias', 'nonbias', 'stereotype' or 'antistereotype'")

        # Rasing an error if there is an unrecognised bias_type
        if bias_type:
            if bias_type not in bias_types:
                raise ValueError(
                    "Bias type must be one of: 'race-color', 'gender', 'socioeconomic', 'nationality', 'religion', 'age', 'sexual-orientation', 'physical-appearance', 'disability'")

        # Filtering the master dataset to only include results obtained by *this* model
        model_dataframe = master_dataframe[master_dataframe['model_name'] == model]

        # Filtering the model dataframe to only include a particular bias type if specified
        if bias_type:
            model_dataframe = model_dataframe[model_dataframe['bias_type'] == bias_type]

        # Getting the score for all models
        score = calculate_all_scores(model_dataframe, threshold)[score_type]
        scores.append(score)

    return scores


def get_list_of_all_scores(list_of_models=all_models, threshold=0.05, bias_type=None):

    scores = {
        'neutral_score': [],
        'bias_score': [],
        'nonbias_score': [],
        'stereotype_score': [],
        'antistereotype_score': []
    }

    for model in list_of_models:

        # Raising an exception if there is an unrecognised model
        if model not in all_models:
            raise ValueError(
                "List of models provided contains unrecognised model")

        # Rasing an error if there is an unrecognised bias_type
        if bias_type:
            if bias_type not in bias_types:
                raise ValueError(
                    "Bias type must be one of: 'race-color', 'gender', 'socioeconomic', 'nationality', 'religion', 'age', 'sexual-orientation', 'physical-appearance', 'disability'")

        # Filtering the master dataset to only include results obtained by *this* model
        model_dataframe = master_dataframe[master_dataframe['model_name'] == model]

        # Filtering the model dataframe to only include a particular bias type if specified
        if bias_type:
            model_dataframe = model_dataframe[model_dataframe['bias_type'] == bias_type]

        # Getting all scores for all models
        scores['neutral_score'].append(calculate_all_scores(
            model_dataframe, threshold)['neutral_score'])
        scores['bias_score'].append(calculate_all_scores(
            model_dataframe, threshold)['bias_score'])
        scores['nonbias_score'].append(calculate_all_scores(
            model_dataframe, threshold)['nonbias_score'])
        scores['stereotype_score'].append(calculate_all_scores(
            model_dataframe, threshold)['stereotype_score'])
        scores['antistereotype_score'].append(calculate_all_scores(
            model_dataframe, threshold)['antistereotype_score'])

    return scores


def get_bias_type_scores(model, threshold=0.05):

    model_dataframe = master_dataframe[master_dataframe['model_name'] == model]

    scores = {
        'neutral_score': [],
        'bias_score': [],
        'nonbias_score': [],
        'stereotype_score': [],
        'antistereotype_score': []
    }

    for bias_type in bias_types:
        bias_model_dataframe = model_dataframe[model_dataframe['bias_type'] == bias_type]
        all_scores = calculate_all_scores(bias_model_dataframe, threshold)
        scores['neutral_score'].append(all_scores['neutral_score'])
        scores['bias_score'].append(all_scores['bias_score'])
        scores['nonbias_score'].append(all_scores['nonbias_score'])
        scores['stereotype_score'].append(all_scores['stereotype_score'])
        scores['antistereotype_score'].append(
            all_scores['antistereotype_score'])

    return scores


@app.route('/')
def index():
    print('running')
    return render_template('index.html')


@app.route('/chart1/')
def chart1(list_of_models=all_models, score_types=['neutral_score', 'bias_score', 'nonbias_score'], threshold=0.05, bias_type=None):

    datalist = []
    all_scores = get_list_of_all_scores(list_of_models, threshold, bias_type)
    for score_type in score_types:
        datalist.append(
            go.Bar(
                name=display_score_types[score_type],
                x=[display_model_names[model] for model in list_of_models],
                y=all_scores[score_type]))

    fig = go.Figure(data=datalist)

    fig.update_layout(
        barmode='group',
        xaxis_tickangle=30)

    score_type_names = [display_score_types[score_type]
                        for score_type in score_types]
    title = " vs. ".join(score_type_names)
    title += " for " + str(len(list_of_models)) + " Models at " + \
        str(threshold*100) + "% Threshold"

    fig.update_layout(
        title=title,
        xaxis_title="Language Models",
        yaxis_title="Scores (%)",
        legend_title="Types of Score")

    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    header = "Grouped Bar Chart"
    description = "description"
    return render_template('notdash2.html', graphJSON=graphJSON, header=header, description=description)


@app.route('/chart2')
def chart2(list_of_models=all_models, threshold=0.05, bias_type=None):

    score_types = ['bias_score', 'nonbias_score', 'neutral_score']

    data = []
    all_scores = get_list_of_all_scores(list_of_models, threshold, bias_type)
    for score_type in score_types:
        data.append(
            go.Bar(
                name=display_score_types[score_type],
                x=[display_model_names[name] for name in list_of_models],
                y=all_scores[score_type]))

    fig = go.Figure(data=data)

    # Change the bar mode
    fig.update_layout(
        barmode='stack',
        xaxis_tickangle=30)

    fig.update_layout(
        title="Neutral Scores vs. Bias Scores vs. Nonbias Scores for " +
        str(len(list_of_models)) + " Language Models",
        xaxis_title="Language Models",
        yaxis_title="Scores (%)",
        legend_title="Types of Score")

    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    header = "Stacked Bar Chart"
    description = "description"
    return render_template('notdash2.html', graphJSON=graphJSON, header=header, description=description)


@app.route('/chart3')
def chart3(list_of_models=all_models, score_type='neutral_score', bias_type=None, step_size=0.01):

    fig = go.Figure()

    # Add traces, one for each slider step
    for step in np.arange(0, 1 + step_size, step_size):

        # Assigning the Threshold
        threshold = step

        # Calculating Neutral Scores at Threshold
        scores = get_list_of_scores(
            score_type, list_of_models, threshold, bias_type)

        fig.add_trace(
            go.Bar(
                visible=False,
                name='Score at Threshold ' + str(round(threshold*100, 2)),
                x=[display_model_names[model] for model in list_of_models],
                y=[score/100 for score in scores]))

    # Make 2nd trace visible
    fig.data[1].visible = True

    # Create and add slider
    steps = []
    label_format = "{:.0%}"
    for i in range(len(fig.data)):
        step = dict(
            method="update",
            args=[{"visible": [False] * len(fig.data)},
                  {"title": display_score_types[score_type] + "s for " + str(len(list_of_models)) + " Models at Threshold:" + label_format.format(i * step_size)}],  # layout attribute
            label=label_format.format(i * step_size))
        step["args"][0]["visible"][i] = True  # Toggle i'th trace to "visible"
        steps.append(step)

    sliders = [dict(
        active=1,
        currentvalue={"prefix": "Threshold: "},
        pad={"t": 150},
        steps=steps
    )]

    fig.update_layout(
        sliders=sliders,
        title=display_score_types[score_type] + "s for " +
        str(len(list_of_models)) + " Models at Various Thresholds",
        yaxis_title="Scores",
        yaxis_tickformat=".0%",
        xaxis_title="Language Models"
    )

    fig.update_yaxes(range=[0, 1])

    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    header = "Slider Bar Chart"
    description = "description"
    return render_template('notdash2.html', graphJSON=graphJSON, header=header, description=description)


@app.route('/chart4')
def chart4(models_to_test=['bert-base-uncased', 'albert-base-v2', 'roberta-base'], score_type='neutral_score', threshold=0.05):

    fig = go.Figure()

    for model in models_to_test:

        # Adding overall score
        scores = get_bias_type_scores(model, threshold)

        fig.add_trace(go.Scatterpolar(
            r=scores[score_type],
            theta=[display_bias_types[bias_type] for bias_type in bias_types],
            fill='toself',
            name=display_model_names[model],
            hovertemplate=display_score_types[score_type] + ": %{r}<br>" +
            "Bias Type: %{theta}<br>"
        ))

    fig.update_layout(
        title="Radar Chart to Compare " + display_score_types[score_type] + " of " +
        str(len(models_to_test)) + " Models at " +
        str(threshold*100) + "% Threshold",
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 100]
            )),
        showlegend=True
    )
    # look into https://plotly.com/python/reference/layout/annotations/
    fig.update_annotations(clicktoshow='onoff')

    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    header = "Radar Chart to Compare Models"
    description = "description"
    return render_template('notdash2.html', graphJSON=graphJSON, header=header, description=description)


@app.route('/chart5')
def chart5(model='bert-base-uncased', score_types=['neutral_score', 'bias_score', 'nonbias_score'], threshold=0.05):

    fig = go.Figure()

    # Adding overall score
    scores = get_bias_type_scores(model, threshold)

    for score_type in score_types:

        fig.add_trace(go.Scatterpolar(
            r=scores[score_type],
            theta=[display_bias_types[bias_type] for bias_type in bias_types],
            fill='toself',
            name=display_score_types[score_type],
            hovertemplate=display_score_types[score_type] + ": %{r}<br>" +
            "Bias Type: %{theta}<br>"
        ))

    fig.update_layout(
        title="Radar Chart to Compare Scores of " +
        display_model_names[model] + " at " +
        str(threshold*100) + "% Threshold",
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 100]
            )),
        showlegend=True
    )
    # look into https://plotly.com/python/reference/layout/annotations/
    fig.update_annotations(clicktoshow='onoff')

    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    header = "Radar Chart to Compare Scores"
    description = "description"
    return render_template('notdash2.html', graphJSON=graphJSON, header=header, description=description)


@app.route('/chart6')
def chart6(model='bert-base-uncased', score_type='neutral_score', thresholds=list(np.arange(0, 0.1, 0.01))):

    fig = go.Figure()

    # Reversing the order of the scores if it is measuring neutrality (to avoid layering issues)
    thresholds.sort(reverse=score_type == 'neutral_score')

    for threshold in thresholds:

        scores = get_bias_type_scores(model, threshold)

        fig.add_trace(go.Scatterpolar(
            r=scores[score_type],
            theta=[display_bias_types[bias_type] for bias_type in bias_types],
            fill='toself',
            name=str(threshold*100) + "%",
            hovertemplate=display_score_types[score_type] + ": %{r}<br>" +
            "Bias Type: %{theta}<br>"
        ))

    fig.update_layout(
        title="Radar Chart to Compare " + display_score_types[score_type] + " of " +
        display_model_names[model] + " at Different Thresholds",
        polar=dict(
            radialaxis=dict(
              visible=True,
              range=[0, 100]
            )),
        showlegend=True
    )
    # look into https://plotly.com/python/reference/layout/annotations/
    fig.update_annotations(clicktoshow='onoff')

    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    header = "Radar Chart to Compare Thresholds"
    description = "description"
    return render_template('notdash2.html', graphJSON=graphJSON, header=header, description=description)
