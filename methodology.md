# Methodology

## Data Preprocessing

The datasets that were provided had a number of `nan` entries in the `f23` column, so I preprocessed my data by using a K-nearest neighbors imputer fitted on the training data and applying it to both the training and test data.

Moreover, I went ahead and created columns that were integer representations of the categorical variables of our dataset; the variables in question were Gender, Use, Tier, Customer Type, and Satisfaction. This would allow the data to be used to train and evaluate ML models.

## Model Experimentation and Selection

I initially experimented with a wide range of classifiers, including linear regression, K-nearest neighbors, decision tree, random forest, naive bayes, Adaboost, and vanilla neural network. I saw that the neural network, decision tree, and adaboost perfoermed the best, with adaboost obtaining `92.6%` accuracy on the test set, the highest of any classifier obtained.

K-nearest neighbors and linear regression were among the weakest performers on the test set, and, KNN did the worst in generalizing from the training set to the test set, with about at 12.7% dip in accuracy. The discrepancy in performance between differrent approaches makes sense. Neural networks have more expressive power than linear regression since they are universal function approximators. Moreover, decision trees perform very well on categorial data, which is plentiful in our data. This can be realized when looking at the range of values obtained under all of the columns from f8 through f21, since values are always some natural number between 0 and 4, inclusive. Adaboost is a boosting algorithm, and in this particular case it acts as an ensemble of different decision trees, so it could generate a classifier that has a higher accuracy than a decision tree.

After this, I went ahead and manually fine-tuned some more hyperparameters with the neural network, adaboost, and the decision tree, and found that adaboost still performed the best with about 94.9% test accuracy. I saved this model.

Since tree ensemble methods seemed to perform the best on this method, I then decided to use a grid search on different parameters on XGBoost and tree to see the best parameters that XGBoost could take. I chose XGBoost since it's a popular learning algorithm in Kaggle competitions and in many cases can have higher accuracy than adaboost. The grid search had a highest testing accuracy of `96.4%` and found these to be the best hyperparameters:

`{'booster': 'dart', 'max_depth': 6, 'n_estimators': 200, 'reg_lambda': 1.0, 'tree_method': 'gpu_hist'}`

I would then go on to use these hyperparameters to work with an XGBoost model and perform feature analysis.

## Feature Analysis

I used mutual information scores to rank the importance of the features in classifying satisfaction. An explanation of mutual information is offered in the IPython notebook.

I sorted the features by their ranking on this metric and found the 5 features with the top 5 MI scores were f13, f8, TierNumber, UseNumber, and f15. These were thus our most informative features. Moreover,  the features with the lowest 5 scores and thus least informative features were f11, f23, f9, GenderNumber, and f22.

I performed a search on how many top k features should be kept by using cross validation, where k could be 5, 10, 15, or 20. Keeping the top 20 features resulted in a model that performed the best in cross-validation, so I went ahead and retrained the model on the training dataset with those features and tested it on the test set.

Ultimately I found that there really wasn't a difference between the test accuracy of the XGBoost model that used the top 20 features and the model that used all of the featues. This is expected, since the models only differ in whether they take in the two lowest raking features. However, since it still used less features, I went ahead and saved it as well.
