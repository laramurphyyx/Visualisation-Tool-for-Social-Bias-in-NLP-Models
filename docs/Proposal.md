# CA4021 Final Year Project Proposal
# Visualisation of Social Bias in Natural Language Models

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Student Name: Lara Murphy

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Student Email: lara.murphy239@mail.dcu.ie

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Student ID: 18390323

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Supervisor: Jennifer Foster


## 0    Executive Summary

This project aims to highlight the presence of social biases that have been trained into language models through visualisation. Social bias is a huge issue we face as a society, and this can be a difficult behaviour/opinion to correct, as large language models, such as BERT and GPT-2, have used training data that contains problematic stereotypes, which further promotes these harmful biases. With no industry-standard evaluation metric for biases in language models, it is difficult to identify  non-biased models over biased models. This visualisation tool will aid the comparison of models and their respective bias scores/areas.

This project will create visualisations to allow for easier comprehension of the types and frequency of biases that are present in a language model. This will be achieved through using existing benchmark datasets for measuring bias, such as StereoSet and CrowS-Pairs and testing against the chosen language models.

## 1    Motivation & Background

Social bias is a very prominent flaw in our society, and despite some recent advancements such as the 'Black Lives Matter' movement, there are still people who hold socially biased views. These biases are often based on stereotypes and prejudices that are systemically maintained, and may be explicit or implicit biases, making the identification and eradication of these harmful views a difficult challenge. Social bias is not limited to a person's race, gender or ethnicity, it can also include age, religion, sexual orientation, physical abilities or even a person's weight. A report carried out by the American Civil Liberties Union shows that black people are 3.7 times more likely to be arrested for possession of marijuana than white people, even though their rate of marijuana usage was comparable [[1.1](https://www.aclu.org/files/assets/1114413-mj-report-rfs-rel1.pdf)] [[1.2](www.aclu.org/report/report-war-marijuana-black-and-white)] [[1.3](https://www.semanticscholar.org/paper/The-War-on-Marijuana-in-Black-and-White-Bunting-Garcia/cf862f2cd14a07da0df5258d17c0f138851510f6)]. This treatment of black people is explicit discrimination, but discrimination can also be implicit. The University of Virginia carried out a study in 2011 that showed women are 47% more likely to suffer severe injuries in car accidents than men, this is as a result of cars' safety features being designed for men [[2](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3222446/)]. It’s likely that this design flaw was not done with intent to put women at risk, rather it was done out of ignorance, due to the implicit bias held about men and women’s status/roles.


Different social groups can be victims of discrimination in all aspects of life, whether it be job interviews or being arrested for a misdemeanor. Not only are there direct implications for targeted social groups as a result of these biases, there are also indirect implications. Indirect discrimination may arise in situations where machine learning has been trained on biased data, or if the machine learning algorithms outputs/methodologies are not monitored or assessed by someone correctly. In this proposal, we will be focussing specifically on the social biases that are contained in natural language processing models. As the use of and need for natural language models rises, the more potential they hold to hurt minority groups. With natural language processing models becoming more popular in technologies such as text generation, recommendation systems and search engines, it is important to try to mitigate any social bias trained into the model as there is huge potential for damage if left untreated.


We interact with natural language processing regularly, possibly without even realizing it. The use of predictive text on our mobile phones, or suggestions made by search engines for what you may search next are some of the many powerful language modelling tools that we are exposed to in our daily lives. When these language models are trained on text corpora that exhibit socially problematic biases, the models influence, encourage or reinforce harmful stereotypes. When creating automated systems that are dependent on these trained language models, it’s likely that there will be problematic actions taken towards certain individuals due to biased profiling. This is apparent in CV screening, where the system tends to favour male candidates [[3.1](http://dx.doi.org/10.3115/v1/P14-2050)] [[3.2](https://aclanthology.org/P14-2050.pdf)] [[3.3](https://www.semanticscholar.org/paper/Dependency-Based-Word-Embeddings-Levy-Goldberg/0183b3e9d84c15c7048e6c2149ed86257ccdc6cb)]. The choice of training data can have major effects on the performance of a language model, if the training data contains harmful biases, this can lead to amplified biases in the model/system. This can be seen in the GPT-2 language model, where it was trained on user-generated data from reddit. A survey carried out by Pew’s Research Centre shows that less than a third of Reddit’s members are female, and over two thirds are from America, a developed country [[4](https://www.pewresearch.org/internet/2016/11/11/social-media-update-2016/)]. This underrepresentation of women’s opinions leads to amplified biases in the overall language model.

The concept of social bias can often be subjective, there is no finite set of stereotypes to avoid or biases that are harmful, and this can make it difficult to identify and eradicate biases in a language model. Large text corpora are required to train large models effectively, and it is difficult to obtain a large amount of text without allowing for user-generated data, where the majority of social biases arise from. This leaves researchers trying to find a balance between unbiased and high-performance language models, and unfortunately the fair language model is sacrificed for a model with improved performance capabilities.

## 2    Problem statement

As discussed in §1, the existence of biases in training data and language models can have negative effects on many individuals. Ideally, all language models should have completely unbiased and factual data for training, although this is rarely the case for large models. The social bias present in large, pretrained NLP models such as BERT and GPT-2 have been criticised by many researchers, and some have even attempted to offer new, less discriminatory ways to train models or perform post-hoc bias removal. These efforts have often reduced the overall performance of the model, and are not perfect solutions to this problem. 


As there are many pretrained language models available, making the right decision can be difficult. The model chosen will be dependent on its use and its desired performance, however, the degree of social bias contained in the model will also be a contributing factor. In order to comprehend the social bias contained in each language model, there needs to be a standard benchmark for evaluation of this bias. This information is available through publications of papers where benchmarks (such as SteroeSet or CrowS-Pairs) were introduced, however it can be difficult to fully understand the extremity/frequency of biases using just a single score. 


The aim of this project is to create a visualisation tool to compare the performance of pretrained language models with respect to social biases. This tool may identify specific areas of bias in the models, such as gender bias or race bias. It allows for visualisation of word embeddings and may show that certain gender-specific words have negative/positive connotations. This tool will allow for users of language models to make educated decisions and ensure that their chosen model will perform fairly and accurately.


## 3    State of the art

There have been numerous investigations showing that the large, pretrained language models that are commonly used in NLP tasks contain social biases. These discoveries have led researchers to propose alternative methods to create unbiased language models and benchmarks to evaluate them, although some of these benchmarks have been later criticised. We will delve deeper into the papers that will influence the direction of this project. 

The work of Emily M. et al. [[5.1](https://dl.acm.org/doi/pdf/10.1145/3442188.3445922)] [[5.2](https://dl.acm.org/doi/10.1145/3442188.3445922)] has gained popularity as being the centre-piece for the dismissal of Timnit Gebru from Google. Timnit Gebru is one of the authors of this paper, which ultimately calls the reliability of Google’s BERT model, and its variants, into question. This paper challenges the model’s environmental impact and its sensitivity to social biases. This paper highlights the issues associated with using large online text corpora to train language models, and recommends creating datasets as large as can be sufficiently documented. They also note the clear distinction between natural language processing and natural language understanding, as this is a concept that is often misconstrued by both the public and researchers. LMs only perform well in tasks that can be approached by manipulating linguistic form.

This paper outlines that the expected benefits of using petabytes of data will increase diversity within the data and include a broad representation of how different individuals view the world. Unfortunately, this is not the case, the data needs to be filtered, and the opinions of people who conform to a hegemonic viewpoint are more likely to be retained. This paper references work from Gehman et al. [[6.1](https://aclanthology.org/2020.findings-emnlp.301/)] [[6.2](https://arxiv.org/pdf/2009.11462.pdf)], which shows models, such as GPT-3, that are trained with at least 570GB of training data collected through Common Crawl, can generate sentences with high toxicity scores, even when prompted with non-toxic sentences. This investigation also shows that the GPT-2 model’s training data includes 272 thousand documents from unreliable news sites and 63 thousand documents from banned subreddits. Emily M. et al. also make the observation that despite the existence of the list of protected attributes in the US (attributes associated with harmful stereotypes), that this list is only applicable to the United States. Different biases and stereotypes exist in different cultures, and it can be difficult to audit for discrimination of such marginalized entities when we don’t know what these cultural-bound biases are. This paper ultimately emphasizes the necessity for more resources to be spent on the gathering and documenting of training data, using a more justice-oriented data collection methodology and ideally preventing the amplified  hegemonic views that are harmful to marginalized groups.

In the paper written by Paul Pu Lang et al., ‘Towards Understanding and Mitigating Social Biases in Language Models’ [7](https://arxiv.org/pdf/2106.13219.pdf), there is further discussion regarding the identification and treatment of the encoded biases in LMs. This paper identifies three difficulties when defining and measuring bias, these are granularity, context and diversity. Granularity is relevant as there can be social biases that may be more subtle and therefore more difficult to spot by standard association tests. Preserving unbiased context is also a challenge, for example, in a sentence ‘The man performing surgery on a patient is a [blank]’, we expect that the masked term would be ‘doctor’. We aim to have a model that will not associate men with being doctors over nurses, although we would like to preserve the association between ‘doctor’ and ‘surgery’. The diversity element requires the LM to be unbiased across a diverse range of real-life contexts, requiring a large-scale evaluation benchmark. 

With these three challenges taken into consideration, Paul Pu Lang et al. propose a new benchmark that tackles each of these issues. They also make a second contribution, a post-hoc debiasing method for large LMs called Autoregressive INLP (A-INLP). They will rely on bias-sensitive tokens rather than bias-sensitive words as it has the ability to capture more nuanced/subtle biases. Their approach to mitigate bias is to learn a set of biased tokens and then mitigating these biases through their autoregressive iterative nullspace algorithm. This paper has shown that the implementation of their new benchmarks and A-INLP methods cause a tradeoff between performance and fairness. Another limitation is that there is more time and resources required during the preprocessing phase, although it achieved a similar inference run time as GPT-2 meaning deployment is feasible.


There have been two approaches to measure bias in coreference resolution systems, WinoBias [8]https://aclanthology.org/N18-2003.pdf) and WinoGender [9](https://arxiv.org/abs/1804.09301). [expand]

StereoSet is another dataset as outlined by Moin Nadeem et al. [10](https://arxiv.org/pdf/2004.09456.pdf) to measure social bias in a pretrained language model. StereoSet measures four domains of biases: gender, profession, race and religion, and has been crowdsourced using Amazon Mechanical Turk, where crowdworkers are based solely in the United States. This paper uses the dataset to measure the level of bias contained in the BERT, GPT-2, RoBERTa and XLNet language models. Prior to this research, language models were evaluated using a small set of artificially constructed bias-assessing sentences, however, this paper will perform this evaluation using StereoSet, a large-scale natural dataset.

The StereoSet dataset includes examples, where examples consist of three sentences, each sentence corresponds to either a stereotypical, an anti-stereotypical, or an unrelated association. An example could be referring to a housekeeper as ‘a Mexican’, ‘an American’ or ‘a round’. The purpose of the stereotype and anti-stereotype sentences is to measure the favorability of either sentence, in an ideal language model the probability of both of these options are 50%, meaning the model exhibits no stereotypical biases. The purpose of the unrelated sentence is to evaluate language modelling ability. These examples create a Context Association Test (CAT) score for pre-trained language models. They have designed two types of association tests, intrasentence and intersentence CATs, which measure bias at sentence-level and discourse-level. A limitation identified in this paper is that the stereotypes are subjective and they may collide with objective facts. This also suggests that there are some cases where the stereotyped association may be a more likely association, creating complex implications for the CAT scores.

Similarly to the StereoSet dataset, the Crowdsourced Stereotype Pairs (CrowS-Pairs) Benchmark dataset [[11](https://aclanthology.org/2020.emnlp-main.154.pdf)] is crowdsourced instead of template-based. This paper evaluates three masked language models (MLM) using the CrowS-Pairs dataset, these models are BERT, RoBERTa and ALBERT. This evaluation dataset contains 1508 examples, where each example consists of a stereotype sentence, and an anti-stereotype sentence. CrowS-Pairs includes more types of bias, there are 9 types of bias included in this dataset, and only 4 types in StereoSet. The tested MLMs use wordpiece models, which allows for links/connections to be made between orthographically similar words/tokens. This can prevent certain words from achieving a higher/lower probability based on their frequency in the training data. This research shows that BERT, being the smallest of the three models evaluated, received the lowest bias score, although it’s also the worst performing model on downstream NLP tasks. This is in-line with the concept raised in literature [5], that there are disadvantages to using too much data.

While the introduction of benchmark datasets to evaluate the performance of a language model with respect to its encoded social bias is an important step to mitigate these biases, these benchmarks have faced some controversy. Su Lin Blodgett et al. [12](https://www.microsoft.com/en-us/research/uploads/prod/2021/06/The_Salmon_paper.pdf) has shown that only between 0%-58% of these four datasets mentioned above [8] [9] [10] [11] are not affected by a domain of pitfalls.

## 4    Methodology

### 4.1     Programming Environment & Development

This project will be a visualisation tool to showcase the social bias present in natural language models. I have chosen to develop my project using Jupyter Notebook. This technology is a popular data science Interactive Development Environment (IDE) as it is easy to use and communicate/interpret results. Jupyter Notebook allows for easy execution of code to allow for quick debugging/testing. Python development is supported by Jupyter Notebooks and is one of their core languages. By using python, we have access to a vast amount of libraries and packages. This project will likely utilise python libraries such as Matplotlib, Seaborn, Plotly, Bokeh or Pygal for the visualization aspect, and will use the Huggingface Transformer Models from the PyTorch module to import and run the language models. I will be using GitLab for version control and aim to make regular commits to track progress.

The coding involved in this project will be primarily focused on the usage and analysis of different language models, such as BERT or GPT-2, and also on creating interactive visualisations. Specifically, I will be importing the social bias benchmark dataset, CrowS-Pairs [], to reproduce the findings as stated by Nangia et al. by testing them on BERT. With these findings reproduced, we can continue to test other models against the CrowS-Pairs benchmark dataset. Running this dataset through each model will give bias scores for each domain of bias contained in the dataset. These biases will be compared with other language models, and subsequently visualised. The visualisations will be produced using the python packages mentioned above, and may be interactive depending on the content/type of chart required.


### 4.2     Source of Data & Experiments

The data that will be used for this project is the CrowS-Pairs dataset, an open-source benchmark dataset used to measure and evaluate social bias in language models. This data is available on GitHub, and is in CSV format. The data contains 1,508 example sentence pairs where each pair includes a sentence with stereotype associations and and a sentence with anti-stereotype associations. The nine bias domains outlined in this dataset are: race, gender/gender identity, sexual orientation, religion, age, nationality, disability, physical appearance, and socioeconomic status. As Blodgett et al. have outlined, there are 29 examples within the CrowS-Pairs dataset that are considered invalid and are not good indicators of social bias. These examples have not been made publicly available, and as these examples represent less than 2% of the dataset, I have decided to continue using this dataset without making any adjustments.

There are several experiments I can carry out with this dataset. My first experiment is to run the test sentences on each language model and to explore the suitable visualizations that would portray the data the clearest. A second experiment that I can perform with this dataset is to test it against the BERT model in isolation. The BERT model has several domain-specific variations, such as BioBERT, SciBERT and FinBERT, which are pretrained Biomedical, Scientific and Financial text mining respectively [ , , ]. These models do not completely re-train BERT, as this is too computationally and financially expensive, they do, however, initialise the model with learned weights from BERT-base, and subsequently train it on domain-specific texts. This experiment will show if there are any significant positive/negative differences in the bias score for each bias domain. 

### 4.3     Desired Result & Evaluation

The final result of this project will be a collection of interactive visualisations representing the level of social bias present in a selected set of language models. Each visualisation will be interactive with hover functionality. There are two stretch-goals in this project, the first goal is to improve the interactive functionality associated with each visualisation by allowing a drill-down option. This can allow users to identify specific examples of where their chosen models have performed weakly, and to ensure that our findings are reliable and transparent. The second stretch goal is to compile these visualisations into a web application, to allow for this information to be easily accessible and comprehensible to the public.

With many of the bias scores of models already validated and published, it is unnecessary to evaluate the performance of the language models against the test dataset. The findings as shown in [] will be reproduced to ensure that the models and training data are being used correctly, and to ensure that bias scores given to unseen models are accurate. The next evaluation to be performed will be based on the visualisations. I intend to carry out a user study to receive feedback regarding the effectiveness and clarity of the charts, and use this feedback as a metric to evaluate the performance of these visualisations. 


## 5    Project plan

While there are some parts of the project plan that may experience minor changes as the project progresses, there is an initial guideline for the tasks to be completed and their intended timeframe. They are as follows:

1. Research / Exploratory Analysis
    * Read existing literature in related NLP areas
    * Investigate the most suitable charts/graphs for the data produced
    * Investigate the most suitable python packages for each visualisation

2. Writing the Code
    * Import the datasets
    * Import the models
    * Evaluating performance of test set for each model
    * Creating visualisations 

3. Testing the Code
    * Replication of Results in Papers
    * Creating Assertions

4. Evaluation of Visualisations
    * Ethics Form
    * Conducting User Survey
    * Interpreting & Analysing Results of Survey

5. Stretch Goals
    * Increased Functionality for Visualisations
    * Creating Web app

6. Final Report

![Gantt Chart for Project Timeline](gantt_chart.png)

The gantt chart above shows the preliminary timeline of tasks to be completed. The plan is designed to allow for most work to be completed by weeks 10-12, to accommodate for other assignments that may be due during this period.

## 6    References

1. UCLA Report - Racial discrimination for marijuana related crimes

    * MLA: Bunting, William C. et al. “The War on Marijuana in Black and White.” PSN: Politics of Race (Topic) (2013): n. pag.
    * APA: Bunting, W.C., Garcia, L.R., & Edwards, E. (2013). The War on Marijuana in Black and White. PSN: Politics of Race (Topic).
    * Chicago: Bunting, W.C., Garcia, L.R., & Edwards, E. (2013). The War on Marijuana in Black and White. PSN: Politics of Race (Topic).
    * EasyBib: “Report: The War on Marijuana in Black and White.” American Civil Liberties Union, www.aclu.org/report/report-war-marijuana-black-and-white
    * Zotero: Court, Sam, and Roderick Battle. ‘The War on Marijuana in Black and White’, n.d., 190.



2. Article from University of Virginia - Cars designed for men

    * MLA: Bose, Dipan et al. “Vulnerability of female drivers involved in motor vehicle crashes: an analysis of US population at risk.” American journal of public health vol. 101,12 (2011): 2368-73. doi:10.2105/AJPH.2011.300275
    * APA: Bose, D., Segui-Gomez, M., & Crandall, J. R. (2011). Vulnerability of female drivers involved in motor vehicle crashes: an analysis of US population at risk. American journal of public health, 101(12), 2368–2373. https://doi.org/10.2105/AJPH.2011.300275
    * EasyBib: Bose, Dipan, et al. “Vulnerability of Female Drivers Involved in Motor Vehicle Crashes: an Analysis of US Population at Risk.” American Journal of Public Health, American Public Health Association, Dec. 2011, www.ncbi.nlm.nih.gov/pmc/articles/PMC3222446/



3. Paper - Gender Bias in CV Screening

    * From a different paper: Omer Levy and Yoav Goldberg. 2014. Dependencybased word embeddings. In Proceedings of the 52nd Annual Meeting of the Association for Computational Linguistics (Volume 2: Short Papers), volume 2, pages 302–308
    * MLA: Levy, Omer and Yoav Goldberg. “Dependency-Based Word Embeddings.” ACL (2014).
    * APA: Levy, O., & Goldberg, Y. (2014). Dependency-Based Word Embeddings. ACL.
    * Chicago: Levy, Omer and Yoav Goldberg. “Dependency-Based Word Embeddings.” ACL (2014).



4. Pew Research Centre - Reddit's Diversity of users

    * EasyBib: Greenwood, Shannon, et al. “Demographics of Social Media Users in 2016.” Pew Research Center: Internet, Science & Tech, Pew Research Center, 31 July 2020, www.pewresearch.org/internet/2016/11/11/social-media-update-2016/.


5. Literature 1 - Criticism of language models

    * ACM: Emily M. Bender, Timnit Gebru, Angelina McMillan-Major, and Shmargaret Shmitchell. 2021. On the Dangers of Stochastic Parrots: Can Language Models Be Too Big? 🦜 In <i>Proceedings of the 2021 ACM Conference on Fairness, Accountability, and Transparency</i> (<i>FAccT '21</i>). Association for Computing Machinery, New York, NY, USA, 610–623. DOI:https://doi.org/10.1145/3442188.3445922
    * idk: Bender, Emily & Gebru, Timnit & McMillan-Major, Angelina & Shmitchell, Shmargaret. (2021). On the Dangers of Stochastic Parrots: Can Language Models Be Too Big?. 610-623. 10.1145/3442188.3445922. 
    * EasyBib: Emily M. Bender University of Washington, et al. “On the Dangers of Stochastic Parrots: Can Language Models Be Too Big? 🦜.” On the Dangers of Stochastic Parrots | Proceedings of the 2021 ACM Conference on Fairness, Accountability, and Transparency, 1 Mar. 2021, dl.acm.org/doi/10.1145/3442188.3
    * link that might include apa reference: https://www.google.com/url?client=internal-element-cse&cx=000299513257099441687:fkkgoogvtaw&q=https://www.aclweb.org/anthology/2021.teachingnlp-1.17.pdf&sa=U&ved=2ahUKEwjR1dnrkOn0AhWBUcAKHVQ_AYQQFnoECAUQAQ&usg=AOvVaw14BXxwg8yxGZ8Q_23e9U8d

6. Toxicity Score paper

    * In Paper [5]: Samuel Gehman, Suchin Gururangan, Maarten Sap, Yejin Choi, and Noah A. Smith. 2020. RealToxicityPrompts: Evaluating Neural Toxic Degeneration in Language Models. In Findings of the Association for Computational Linguistics: EMNLP 2020. Association for Computational Linguistics, Online, 3356–3369. https://doi.org/10.18653/v1/2020.findings-emnlp.301
    * EasyBib: Gehman, Samuel, et al. “RealToxicityPrompts: Evaluating Neural Toxic Degeneration in Language Models.” ACL Anthology, aclanthology.org/2020.findings-emnlp.301/.
    * Researchgate: Gehman, Samuel & Gururangan, Suchin & Sap, Maarten & Yejin, Choi & Smith, Noah. (2020). RealToxicityPrompts: Evaluating Neural Toxic Degeneration in Language Models. 3356-3369. 10.18653/v1/2020.findings-emnlp.301. 


7. Literature 2 - Understanding & Mitigating Social Bias

    * MLA: Liang, Paul Pu et al. “Towards Understanding and Mitigating Social Biases in Language Models.” ICML (2021).
    * APA: Liang, P.P., Wu, C., Morency, L., & Salakhutdinov, R. (2021). Towards Understanding and Mitigating Social Biases in Language Models. ICML.
    * Chicago: Liang, Paul Pu, Chiyu Wu, Louis-Philippe Morency and Ruslan Salakhutdinov. “Towards Understanding and Mitigating Social Biases in Language Models.” ICML (2021).
    * EasyBib: Liang, Paul Pu, et al. “[PDF] Towards Understanding and Mitigating Social Biases in Language Models: Semantic Scholar.” Undefined, 1 Jan. 1970, www.semanticscholar.org/paper/Towards-Understanding-and-Mitigating-Social-Biases-Liang-Wu/114aa720872462b0ca1b97bfdec0ebd56c36fd0a.


8. Literature 3 - WinoBias

    * In WinoGender paper: Jieyu Zhao, Tianlu Wang, Mark Yatskar, Vicente Ordonez, and Kai-Wei Chang. 2018. Gender bias in coreference resolution: Evaluation and debiasing methods. In Proceedings of the 2018 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies, New Orleans, Louisiana. Association for Computational Linguistics.
    * In CrowS-Pairs paper: Jieyu Zhao, Tianlu Wang, Mark Yatskar, Vicente Ordonez, and Kai-Wei Chang. 2018. Gender bias in coreference resolution: Evaluation and debiasing methods. In Proceedings of the 2018 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies, Volume 2 (Short Papers), pages 15–20, New Orleans, Louisiana. Association for Computational Linguistics.


9. Literature 4 - WinoGender

    * Researchgate: Rudinger, Rachel & Naradowsky, Jason & Leonard, Brian & Durme, Benjamin. (2018). Gender Bias in Coreference Resolution. 
    * https://aclanthology.org/N18-2002/

10. Literature 5 - StereoSet

    * Researchgate: Nadeem, Moin & Bethke, Anna. (2020). StereoSet: Measuring stereotypical bias in pretrained language models. 
    * https://aclanthology.org/2021.acl-long.416/

11. Literature 6 - CrowS-Pairs

    * MLA: Nangia, Nikita et al. “CrowS-Pairs: A Challenge Dataset for Measuring Social Biases in Masked Language Models.” EMNLP (2020).
    * APA: Nangia, N., Vania, C., Bhalerao, R., & Bowman, S.R. (2020). CrowS-Pairs: A Challenge Dataset for Measuring Social Biases in Masked Language Models. EMNLP.
    * Chicago: Nangia, Nikita, Clara Vania, Rasika Bhalerao and Samuel R. Bowman. “CrowS-Pairs: A Challenge Dataset for Measuring Social Biases in Masked Language Models.” EMNLP (2020).

12. Literature 7 - Stereotyping Norwegian Salmon

    * Researchgate: Blodgett, Su & Lopez, Gilsinia & Olteanu, Alexandra & Sim, Robert & Wallach, Hanna. (2021). Stereotyping Norwegian Salmon: An Inventory of Pitfalls in Fairness Benchmark Datasets. 1004-1015. 10.18653/v1/2021.acl-long.81. 
    * MLA: Blodgett, Su Lin et al. “Stereotyping Norwegian Salmon: An Inventory of Pitfalls in Fairness Benchmark Datasets.” ACL/IJCNLP (2021).
    * APA: Blodgett, S.L., Lopez, G., Olteanu, A., Sim, R., & Wallach, H.M. (2021). Stereotyping Norwegian Salmon: An Inventory of Pitfalls in Fairness Benchmark Datasets. ACL/IJCNLP.
    * Chicago: Blodgett, Su Lin, Gilsinia Lopez, Alexandra Olteanu, Robert Sim and Hanna M. Wallach. “Stereotyping Norwegian Salmon: An Inventory of Pitfalls in Fairness Benchmark Datasets.” ACL/IJCNLP (2021).

13. SciBERT

    * MLA: Beltagy, Iz et al. “SciBERT: A Pretrained Language Model for Scientific Text.” EMNLP (2019).
    * APA: Beltagy, I., Lo, K., & Cohan, A. (2019). SciBERT: A Pretrained Language Model for Scientific Text. EMNLP.
    * Chicago: Beltagy, Iz, Kyle Lo and Arman Cohan. “SciBERT: A Pretrained Language Model for Scientific Text.” EMNLP (2019).

14. BioBERT

    * MLA: Lee, Jinhyuk et al. “BioBERT: a pre-trained biomedical language representation model for biomedical text mining.” Bioinformatics 36 (2020): 1234 - 1240.
    * APA: Lee, J., Yoon, W., Kim, S., Kim, D., Kim, S., So, C.H., & Kang, J. (2020). BioBERT: a pre-trained biomedical language representation model for biomedical text mining. Bioinformatics, 36, 1234 - 1240.
    * Chiacgo: Lee, Jinhyuk, Wonjin Yoon, Sungdong Kim, Donghyeon Kim, Sunkyu Kim, Chan Ho So and Jaewoo Kang. “BioBERT: a pre-trained biomedical language representation model for biomedical text mining.” Bioinformatics 36 (2020): 1234 - 1240.

15. FinBERT

    * MLA: Liu, Zhuang et al. “FinBERT: A Pre-trained Financial Language Representation Model for Financial Text Mining.” IJCAI (2020).
    * APA: Liu, Z., Huang, D., Huang, K., Li, Z., & Zhao, J. (2020). FinBERT: A Pre-trained Financial Language Representation Model for Financial Text Mining. IJCAI.
    * Chicago: Liu, Zhuang, Degen Huang, Kaiyu Huang, Zhuang Li and Jun Zhao. “FinBERT: A Pre-trained Financial Language Representation Model for Financial Text Mining.” IJCAI (2020).

Other links: 

[Short Article about Social Bias](https://counseling.ufl.edu/resources/bam/module1-4/)

[Edwards, E., Bunting, W., Garcia, L. (2013). The War on Marijuana in Black and White. New York, NY: American Civil Liberties Union.](https://www.aclu.org/files/assets/1114413-mj-report-rfs-rel1.pdf)

[UN Report reveals nearly 90 per cent of all people have ‘a deeply ingrained bias’ against women](https://news.un.org/en/story/2020/03/1058731)

[BBC statistics about gender bias](https://www.bbc.com/news/world-51751915)

[Racial Disparities Report to the UN](https://www.sentencingproject.org/publications/un-report-on-racial-disparities/)

[Statistical Discrimination and the Rationalization of Stereotypes](https://journals.sagepub.com/doi/10.1177/0003122420969399)

[Controversial Tool about measuring bias](https://digest.bps.org.uk/2018/12/05/psychologys-favourite-tool-for-measuring-implicit-bias-is-still-mired-in-controversy/)

[Bias in Social Research (not sure if this is social bias or data bias)](https://journals.sagepub.com/doi/full/10.5153/sro.55)