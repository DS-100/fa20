---
layout: page
title: Graduate Project
nav_exclude: true
nav_order: 6
description: Specifications for the final project for Data 200.
---

# Graduate Project

The graduate project is offered only to students enrolled in Data C200 or CS C200A. Other students are welcome to explore the questions and datasets in the project for learning, but their work will not be graded or counted towards their final grades.

The purpose of the project is to give students experience in both open-ended data science analysis and research in general. As part of the project, you have the option to either

* [[**Option 1**](#multiple_datasets)] work with a combination of datasets provided to you to explore research questions that you define.
* [[**Option 2**](#image_classification)] complete the computer vision project.

**Note**: each option has its own set of requirements for Report Format and Submission. Be sure to consult the correct section for your project option.

You will receive feedback from peer grading before the final deadline, and you are expected to incorporate the feedback into the final report and presentation. You will be graded on both the final report and presentation, as well as [deliverables](#deliverables) before the submission of the final reports, including your peer reviews. 

**Teamwork**: You can work alone or in a group with at most two other students. If you are interested in working with others, we will have a Piazza post for teammate search. Everyone in the same group will receive the same grade. The group size will be taken into consideration for grading.


## <a name="multiple_datasets"></a>Option 1: Multiple Datasets

This project option involves studying **two or more** of the following datasets. You are welcome to bring in additional datasets to complement the datasets provided here, but you must cite the sources and clearly describe the content of any additional data you use in the final report.

Please be sure to consult the [references on causal inference](#causal_inference) for guidance on how to work with multiple datasets. 

### Datasets

The following datasets can be found in `~/shared/grad_proj/multiple_datasets` on DataHub. If you wish to work on the project locally, you can download `~/shared/grad_proj/multiple_datasets.zip` containing all the datasets.


#### COVID-19

This dataset contains global and US daily reports on testing and cases from the [COVID-19 Data Repository by the Center for Systems Science and Engineering (CSSE) at Johns Hopkins University](https://github.com/CSSEGISandData/COVID-19). It is located at `~/shared/grad_proj/multiple_datasets/covid` on DataHub, and the global reports and US reports are located in two separate directories:

* `csse_covid_19_daily_reports` contains global daily reports ([documentation](https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data#daily-reports-csse_covid_19_daily_reports))
* `csse_covid_19_daily_reports_us` contains US daily reports ([documentation](https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data#usa-daily-state-reports-csse_covid_19_daily_reports_us))

You can choose to work with either the global reports or the US reports. You are not required to study both if you were to choose this dataset.


#### Mental Health in Tech Survey

This dataset contains questions and answers in the [OSMI Mental Health in Tech Survey](https://osmihelp.org/research) conducted annually between 2014 and 2019. It is located at `~/shared/grad_proj/multiple_datasets/mental_health` on DataHub and comprises two tables:

* `mental_health_question.csv` contains the questions and their IDs in `QuestionText` and `QuestionID` respectively.
* `mental_health_answer.csv` contains the survey participants' answers to the questions in `AnswerText`. `SurveyID` is the year in which the survey is conducted, and `QuestionID` matches the `QuestionID` in `mental_health_question.csv`. Each row corresponds to the answer to a specific question by a specific user identified by `UserID`.

Note that the set of questions asked in the survey changes from year to year. 


#### Global Climate

This dataset contains the daily temperature and precipitation measured by weather stations in the [Global Historical Climatology Network](https://www.ncdc.noaa.gov/data-access/land-based-station-data/land-based-datasets/global-historical-climatology-network-ghcn) for January to October 2020. 

This dataset can be found in `~/shared/grad_proj/multiple_datasets/climate` on DataHub. 
The data in `daily_global_weather_2020.csv` is derived from the source file at https://www1.ncdc.noaa.gov/pub/data/ghcn/daily/by_year/2020.csv.gz.

To help you get started with a dataset of manageable size, we have preprocessed the GHCN dataset to include only the average temperature and precipitation measurements from stations that have both measurements. Each row in the preprocessed dataset contains both the average temperature and precipitation measurements for a given station on a given date. 

If you wish to explore the climate data for a different year, you can use the `GHCN_data_preprocessing.ipynb` notebook to download and perform the preprocessing described above. Please be advised that depending on the dataset size for a given year, `GHCN_data_preprocessing.ipynb` may not run on DataHub. We will not be providing infrastructural support for running the notebook, but you are welcome to run it on a different machine you have access to or ask a GSI to dump the data for you.

This dataset contains only the (latitude, longitude) coordinates for the weather stations. To map the coordinates to geographical locations, the [reverse-geocoder](https://github.com/thampiman/reverse-geocoder) package mentioned in the [References](#coordinates) section might be helpful.


#### 2019 US Census

The 2019 US Census dataset contains demographic, housing and economic information reported at the county level. The dataset is located at `~/shared/grad_proj/multiple_datasets/census` on DataHub and comprises two tables:

* **DP05**: ACS Demographic and Housing Estimates (exported from the [DP05 table](https://data.census.gov/cedsci/table?q=dp05&tid=ACSDP1Y2019.DP05) at county level summary from data.census.gov).
* **DP03**: Selected Economic Characteristics (exported from the [DP03 table](https://data.census.gov/cedsci/table?q=dp03&tid=ACSDP1Y2019.DP03) at county level summary from data.census.gov).

Documentation for these two tables can be found in `DP03/ACSDP1Y2019.DP03_table_title.txt` and `DP05/ACSDP1Y2019.DP05_table_title.txt`, respectively. You can also visit data.census.gov for more information on the datasets.

### Example Research Questions Involving Multiple Datasets

* COVID-19 + Climate: Does weather have an effect on the spread of COVID-19? How do we control for test availability and differences in response to the disease? Here are some [existing studies](http://berkeleyearth.org/archive/coronavirus-and-the-weather/) on the topic. 
* COVID-19 + Mental Health: Are there specific populations that are particularly susceptible to both COVID-19 and mental health ailments?
* COVID-19 + US Census: what is the relationship between COVID-19 cases and socioeconomic factors and healthcare coverage? Can you use demographic features to predict COVID-19 infection and mortality rates?

### Report Format and Submission
The project submission should include the following two components.

1. **Analysis Notebooks**. The Jupyter Notebook(s) containing all the analyses that you performed on the datasets to support your claims in the narrative notebook. Make sure that all references to datasets are done as `data/[path to data files]`. You can copy the datasets from `~/shared/grad_proj/multiple_datasets` into `data/` at the top-level directory for your project on DataHub to do this.
2. **Narrative Notebook**. This is a single Jupyter Notebook that summarizes your workflow and what you have learned. It should be structured as a research paper and include a title, list of authors, abstract, introduction, description of data, description of methods, summary of results, and discussion. Make sure to number figures and tables and include informative captions. Specifically, you should address the following in the narrative:

    * Clearly stated research questions and why they are interesting and important. You must include **at least one research question involving multiple datasets**, but you may include additional research questions about each individual dataset. At least one of your research questions has to include a modeling component, e.g., can we build a model using climate data to predict growth in COVID-19 cases accurately? The modeling question does not need to be about multiple datasets.
    * A brief survey of related work on the topic(s) of your analysis and how your project differs from or complements existing research.
    * If applicable, descriptions of additional datasets that you gathered to support your analysis.
    * Methodology: carefully describe the methods you use and why they are appropriate for answering your search questions. It must include 
        * a brief overview of causal inference, which should be written in a way such that another student in Data 100 who has never been exposed to the concept can carry out the analyses involving multiple datasets in your project.
        * a detailed description of how modeling is done in your project, including inference or prediction methods used, feature engineering and regularization if applicable, and cross-validation or test data as appropriate for model selection and evaluation.  
    * _Interesting findings_* about each dataset when analyzed individually. Include visualizations and descriptions of data cleaning and data transformation necessary to perform the analysis that led to your findings.
    * _Interesting findings_* involving multiple datasets. Include visualizations and descriptions of data cleaning and data transformation necessary to perform the analysis that led to your findings.
    * Analysis of your findings to answer your research question(s). Include visualizations and specific results. If your research questions contain a modeling component, you must compare the results using different inference or prediction methods (e.g., linear regression, logistic regression, or classification and regression trees). Can you explain why some methods performed better than others?
    * An evaluation of your approach and discuss any limitations of the methods you used.
    * Describe any surprising discoveries that you made and future work.

\* Examples of **interesting findings**: interesting data distributions and trends, correlations between different features, the relationship between the data distribution for the general population and specific datasets (e.g., the gender distribution in the census dataset vs. in the mental health dataset), specific features that are notably effective/ineffective for prediction. 

The narrative notebook should include figures sparingly to support specific claims. It can include runnable components, but it should not have large amounts of code. The length of the report should be 8+/-2 pages when it is printed as a PDF, excluding figures and code.

Tip: if you need to write a large amount of $\LaTeX$, you may want to use the `%%latex` cell magic.

Please submit everything as a zip file to Gradescope. Please make sure the folder in the zip file has the following structure:

```
studentIDs/
    data/[all datasets used]
    analysis/[analysis notebooks]
    narrative/[narrative notebook]
    figures/[figures included in the narrative notebook]
```

For groups of size two, please use `studentID1_studentID2` as the name for the top-level directory. The analysis notebooks must be runnable within this directory structure. If the narrative notebook includes any figures that are created in the analysis notebooks, the figures should be saved to `figures/` by the analysis notebooks and imported from `figures/` by the narrative notebook.


## <a name="image_classification"></a>Option 2: Image Classification

For the image classification project, you are provided with a set of "real-world" images of 20 different types (e.g., "dog", "goat") and your task is to train and evaluate several predictors for the class of an image. You will then evaluate your proposed final classifier using a test set for which we have withheld the class labels. 

Everything you need for the project can be found in `~/shared/grad_proj/computer_vision` on DataHub.

### Dataset
The dataset for training and validation, referred to simply as the training set from here on, consists of a total of 2,921 images, of 20 different types and of possibly different sizes (i.e., numbers of pixels). Each image is represented as 3-d array with the first two dimensions corresponding to the row and column pixels and third dimension to the color. The third dimension size is always 3, and each value corresponds to a red, green, or blue (RGB) color intensity between 0 and $2^8 - 1$. 

The training set can be found in the 20 categories training folder in the project starter directory. 
The test set can be found in the 20 validation folder in the project starter directory.

### Project Guidelines
The project involves carrying through the following steps.

1. **Data Input**
    * Read in all the provided training and test set images.
    * Store the images in two data frames, one for the training set (with class labels) and one for the test set (without class labels).

2. **Exploratory data analysis and feature extraction.** (Training set only.)
    * Display three of the training set images.
    * Provide graphical summaries of the sizes of the images, pixel intensities, and class frequencies.
    * Provide functions that summarize pixel intensity data (e.g., https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_feature2d/py_table_of_contents_feature2d/py_table_of_contents_feature2d.html#py-table-of-content-feature2d). Compute at least 15 such image features (a method for each), including the following (NOTE: At least 10 of these must be scalar features and 2 matrix-based features): (i) image size, (ii) average of the red-channel intensity, (iii) aspect ratio.
    * Examine how these image features vary between classes.

3. **Classifier training.** (Training set only.) Using all or a selected subset of the features from Step 2 and all or a selected subset of individual pixel intensities, build the following classifiers using only the training set. Feel free to generate a combination of these models for your final predictions.
    * Logistic regression: http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html.
    * k-nearest neighbors (kNN): http://scikitlearn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html.
    * Classification tree: https://scikit-learn.org/stable/modules/tree.html.
    * Random Forests: http://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html.
    * Support vector machines (SVM): http://scikit-learn.org/stable/modules/svm.html.

4. **Classifier performance assessment.** (Training set only.) Evaluate the performance of the classifiers in Step 3 using five-fold cross-validation of the training set to estimate the misclassification error rate, i.e., perform all the tasks in Step 3) (including feature selection) on the training sets and compute misclassification rates on the validation sets.

5. **Neural networks.** (Optional. Extra credit: 10% (out of 100%) of project score, but your total project score cannot exceed 100%.) Build a neural network classifier using an architecture of your choosing. This application of deep learning can be done in PyTorch, TensorFlow, or a framework of your choice. Describe your network and assess its performance. To receive extra credit, your neural network classifier must outperform your other methods.


### Report Format and Submission
The project submission should include the following three components.

#### Jupyter Notebooks. 
Use the provided starter notebooks to complete the following aspects of the project.
1. Data input.
2. Exploratory data analysis and feature extraction.
3. Classifier training and performance assessment.
4. Neural networks (Extra credit).

Note: We will run the notebooks in that order when grading, so please account for that.

#### Project narrative. 
This Jupyter Notebook should summarize your workflow and what you have learned. It should be structured as a research paper and include a title, list of authors, abstract, introduction, description of data, description of methods, summary of results, and discussion. Make sure to number figures and tables and include informative captions. Specifically, you should address the following in the narrative.

* Frame the question.
* Describe the data.
* Perform exploratory data analysis (EDA) and provide data visualizations.
* Describe any data cleaning or transformations that you perform and why they are motivated by your EDA.
* Carefully describe the methods you are using and why they are appropriate for the question to be answered.
* Summarize and interpret your results (including visualization). Address the following three specific questions. (i) What were two or three of the most interesting features you came across? Describe the process of finding those features. (ii) Describe one feature you thought would be useful but turned out to be ineffective. (iii) Describe the differences in the classifiers that you used. Why did some work better than others? Which turned out to be the most effective?
* Provide an evaluation of your approach and discuss any limitations of the methods you used.
* Describe any surprising discoveries that you made and future work.

The narrative notebook should include figures sparingly to support specific claims. It can include runnable components, but it should not have large amounts of code. The length of the report should be 8+/-2 pages when it is printed as a PDF, excluding figures and code.

3. Image class predictions for test set. Run the classifier of your choice on the test data of 716 images and generate a CSV file of the classification for each image. Submit this CSV file on Gradescope. It is your responsibility to follow the order of the files when creating the CSV (predict validation 1 before validation 2...).
Note 1: You are not to use the test data in any way for training or creating your classifer.
Note 2: You are not allowed to use a neural network for your final classifier.

**The accuracy of your final classifier on the test set will count for 25% of your grade on the final report.**

Please submit everything as a zip file to Gradescope. The directory structure in the zip file should be the same as the one in `~/shared/grad_proj/computer_vision`.



## <a name="deliverables"></a>Deliverable Deadlines

### Summary of deadlines and grade breakdown

| Deliverable | Deadline | % Grade (out of 100%) |
| -------- | -------- | -------- |
| [Project Signup](#signup)     | November 12th, 11:59 pm PT | 5% (full credit for submitting on time) |
| [Proposal](#proposal) | November ~~17th~~ 18th, 11:59 pm PT | 5% (full credit for submitting on time) |
| [Report draft for peer review](#draft) | November 24th, 11:59 pm PT | 5% (full credit for submitting on time) |
| [Peer reviews](#review) | December 1st, 11:59 pm PT | 10% (rubric TBD)|
| [Final report and presentation](#final) | December 9th, 11:59 pm PT| 75% (rubric TBD)|

### <a name="signup"></a>Datasets selection and group signup (Due 11:59pm PT, November 12th)

Please sign up with your group and dataset selections [here](https://forms.gle/i9Uj3rMeLmDWusTD9) by November 12th. Only one person per partner group needs to fill out the form.

If you are interested in working with another student, we will have a Piazza post for teammate search.

You are encouraged but not required to explore all datasets provided before deciding on the datasets to use for your project.

This accounts for 5% (out of 100%) of your project grade. You will receive full credit for submitting the signup form by the deadline.

### <a name="proposal"></a>Research questions and proposed methodology (Due 11:59pm PT, November ~~17th~~ 18th)

A one-page PDF document addressing the following questions:
* What are the research questions you are tackling in your project? What are some existing works, if any, related to your research questions? If you selected Option 2, talk about what questions you'd like to explore for the image dataset.
* What data analysis do you plan on performing for each dataset to help answer your research questions?
* [Option 1 only] How does causal inference apply to the analysis you plan on doing involving multiple datasets? What is the difference between causation and association? What are potential sources of confounding? How do you identify and adjust for it? 
* [Option 2 only] How do you plan on testing your classifier?

Consult the textbooks in [References](#references) or other reputable materials you find to answer these questions. Make sure to cite any reference materials and related work. 

You will submit the proposal via Gradescope. The proposal accounts for 5% (out of 100%) of your project grade. You will receive full credit for submitting the proposal by the deadline.


### <a name="draft"></a>Report submission for peer review (Due 11:59pm PT, November 24th)
An initial draft of your report to be shared with other groups in the class for peer review. You will not be graded on the quality of this draft, but feedback from your peers may be taken into consideration for the final grade.

Follow the instructions in the Report Format and Submission section of the project option that you chose to prepare the zip file to be submitted via Gradescope.

This accounts for 5% (out of 100%) of your project grade. You will receive full credit for submitting the report by the deadline. Late reports might not be able to participate in peer review, and peer feedback will be taken into consideration for the final report grade.

**Make sure to anonymize your report for this submission.** That means the names of the group members should not be shown anywhere in the report notebooks. 

### <a name="review"></a>Peer Review Submission (Due 11:59pm PT, December 1st)
Each group will peer grade two to three (TBD) other projects. For each project reviewed, the review should include the following components:
* A score between 1 to 5 (5 is the best).
* A summary of the report & rationale for the score
* 3 strong points 
* 3 weak points
* Detailed feedback (>= 3 suggestions for improvement)

This accounts for 10% (out of 100%) of your project grade. You will be graded on the quality of your reviews, and your peers will take your reviews into consideration when preparing their reports for final submission. 

Your reviews will be disseminated to your peers shortly after the deadline, so it is important that your reviews are submitted on time. You will submit your reviews via Gradescope.

### <a name="final"></a>Final report & presentation submission (Due 11:59pm PT, December 9th)
The final submission contains two parts:
* The zip file containing all of the necessary components of the report according to the instructions in in the Report Format and Submission section of the project option that you chose.
* A two-minute video walkthrough of your report. 

You are expected to incorporate feedback from peer review into the final report. You will submit a single zip file containing the following directory structure when decompressed:

```
studentIDs\
    studentIDs_final_report.zip
    peer_review\
        review1.pdf
        ...
    studentIDs.mp4
```

This accounts for 75% (out of 100%) of your project grade. Rubric to be released after the proposal deadline.


## References

### <a name="coordinates"></a>Working with Geographical Coordinates
For datasets containing only latitude and longitude information, you may want to use the [reverse-geocoder](https://github.com/thampiman/reverse-geocoder) Python package to help you map the coordinates to geographic regions.

Tip: when using `reverse-geocoder`, you might want to run queries in bulk instead of one coordinate at a time, e.g.,
```
import reverse_geocoder as rg
query = rg.search([tuple(x) for x in df[['Latitude', 'Longitude']].values])
```

We have also provided a mapping from country codes to country names and regions in `UID_ISO_FIPS_LookUp_Table.csv`. Be sure to read the documentation for `reverse-geocoder` to decide what type of country codes to use for the join.


### <a name="causal_inference"></a>Causal Inference

When studying the relationship between datasets, you might want to consult the following references on causality vs. correlation. Oftentimes, it is tempting to make claims about causal relationships when there is not enough evidence from the data to support such claims. Please review the following references, or other reputable references that you find on the topic to familiarize yourself with relevant concepts and methods. 

* [Data 102  Data, Inference, and Decisions Spring 2020: Lecture 13: Causal Inference I. Moritz Hardt.](https://data102.org/sp20/assets/notes/notes13.pdf) 
* [Hernán MA, Robins JM (2020). Causal Inference: What If. Boca Raton: Chapman & Hall/CRC.](https://www.hsph.harvard.edu/miguel-hernan/causal-inference-book/)
* [Advanced Data Analysis from an Elementary Point of View by Cosma Rohilla Shalizi](https://www.stat.cmu.edu/~cshalizi/ADAfaEPoV/)
