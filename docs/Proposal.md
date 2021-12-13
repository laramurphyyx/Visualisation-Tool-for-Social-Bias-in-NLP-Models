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


## 2    Problem statement

As discussed in §1, the existence of biases in training data and language models can have negative effects on many individuals. Ideally, all language models should have completely unbiased and factual data for training, although this is rarely the case for large models. The social bias present in large NLP models such as BERT and GPT-2 have been criticised by many researchers, and some have even attempted to offer new, less discriminatory ways to train models or perform post-hoc bias removal. These efforts have often reduced the overall performance of the model, and are not perfect solutions to this problem. 


As there are many language models available, making the right decision can be difficult. The model chosen will be dependent on its use and its desired performance, however, the degree of social bias contained in the model will also be a contributing factor. In order to comprehend the social bias contained in each language model, there needs to be a standard benchmark for evaluation of this bias. This information is available through publications of papers where benchmarks (such as SteroeSet or CrowS-Pairs) were introduced, however it can be difficult to fully understand the extremity/frequency of biases using just a single score. 


The aim of this project is to create a visualisation tool to compare the performance of the language models with respect to social biases. This tool may identify specific areas of bias in the models, such as gender bias or race bias. It allows for visualisation of word embeddings and may show that certain gender-specific words have negative/positive connotations. This tool will allow for users of language models to make educated decisions and ensure that their chosen model will perform fairly and accurately.


## 3    State of the art

## 4    Methodology

## 5    Project plan

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



Other links: 

[Short Article about Social Bias](https://counseling.ufl.edu/resources/bam/module1-4/)

[Edwards, E., Bunting, W., Garcia, L. (2013). The War on Marijuana in Black and White. New York, NY: American Civil Liberties Union.](https://www.aclu.org/files/assets/1114413-mj-report-rfs-rel1.pdf)

[UN Report reveals nearly 90 per cent of all people have ‘a deeply ingrained bias’ against women](https://news.un.org/en/story/2020/03/1058731)

[BBC statistics about gender bias](https://www.bbc.com/news/world-51751915)

[Racial Disparities Report to the UN](https://www.sentencingproject.org/publications/un-report-on-racial-disparities/)

[Statistical Discrimination and the Rationalization of Stereotypes](https://journals.sagepub.com/doi/10.1177/0003122420969399)

[Controversial Tool about measuring bias](https://digest.bps.org.uk/2018/12/05/psychologys-favourite-tool-for-measuring-implicit-bias-is-still-mired-in-controversy/)

[Bias in Social Research (not sure if this is social bias or data bias)](https://journals.sagepub.com/doi/full/10.5153/sro.55)