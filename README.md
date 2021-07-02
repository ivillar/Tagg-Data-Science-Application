<h1 align="center">
    Tagg Data Science Challenge
</h1>

## Intro

As a data scientist at Tagg, you will be working on extracting useful user data from our live mobile application and developing machine learning models to classify users and content, and optimize how we display and rank content for our users' feeds and their suggested people pages. In this project, you will demonstrate your knowledge of basic machine learning principles and mathematics skills by developing a classification model in Python.


## Useful Resources

- [scikit-learn Documentation](https://scikit-learn.org/stable/)
- [pandas Documentation](https://pandas.pydata.org/docs/reference/index.html)
- [Bivariate Analysis](https://www.statisticshowto.com/bivariate-analysis/)


## Getting Started

### 1. Forking the repository

Go ahead and fork this repository to your Github account. You will be working on your fork, and will use it to hand in your final work. For a refresher on forks, check out the [Github docs](https://docs.github.com/en/get-started/quickstart/fork-a-repo).

### 2. Getting the data

You will be working with a dataset that describes customer satisfaction with an anonymized service based on demographics and other parameters. Many of the features in the dataset have been anonymized, so some columns will have the names `f1`, `f2`, ..etc. The labels are in the last column, named `Satisfaction`, so make sure you do not include those in your input features.

The data may need to be cleaned in order to be made usable in a model, so feel free to write any preprocessing code you find necessary.

### 3. Training your model

Once the dataset is ready, use the data in `train.csv` to train your classifier. You are free to use any Python libraries you need to create and train your model, but you should research different types of classifiers and use a suitable model for your task.

### 4. Testing your model

After training your model on the training data, use the data in `test.csv` to test your model. Calculate classification accuracy as the percentage of datapoints that were classified correctly by the model.

## Requirements
* You should be able to achieve a >90% accuracy level with your classifications on the test set. 
* You should provide a `methodology.md` file describing your approach to classifying the data, any insight you were able to draw, and any specific design choices you made.


## Submitting your code
Commit and push your work to your fork. Your final submission should be the commit with the commit message `Final Submission`. We will be considering the first commit with this message as your final submission, so make sure not to commit this until you have finished your work.


## Extra Credit

### Higher Accuracy
It is possible to achieve a classifying accuracy of >95% on this dataset, so feel free to expirement with different classification methods and tune them to achieve better results.

### Feature Analysis
The dataset contains 23 features for each datapoint. Some of these matter more than others when trying to classify the data. Perform analysis on the data to figure out which features matter more than others, and drop the features that have a low impact on the labeling. Re-run your model on the trimmed data and report your findings.