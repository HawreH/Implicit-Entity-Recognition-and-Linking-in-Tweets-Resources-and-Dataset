# Implicit-Entity-Linking-in-Tweets-Resources-and-Dataset

# Overview
This repository includes a gold standard dataset containing 7870 tweets for the task of implicit entity recognition and classification. The publication pertinent to this work is titled "". 
Moreover, a manuscript as an extension to the aforementioned publication titled "" has been submitted for a journal publication.

# Publications

The source codes and resources pertinent to the first publication, "Implicit Entity Linking through Ad-hoc Retrieval", can be found [here] (https://github.com/HawreH/Implicit-Entity-Linking-through-Ad-Hoc-Document-Retrieval_).

The source codes and data pertinent to "Implicit Entity Linking in Tweets: an Ad-hoc Retrieval Approach" can be found in this repository as described below. Additionally, the abstract and more detailed explanation of the research work can be found on the [wiki] (https://github.com/HawreH/Implicit-Entity-Recognition-and-Linking-in-Tweets-Resources-and-Dataset/wiki) of this repository.



# Dataset
This [gold standard dataset for implicit entity recognition, classification and linking](somewhere) is comprised of three major categories of tweets, namely tweets with explicit mention/s of entities ("explicit"), tweets with implicit mention/s of entities ("implicit"), and tweets without either ("NIL"). As per a random sampling using Twitter API and ratio calculation, the ratio of different types of tweets in our dataset is as follows: 35\% Explicit, 15\% Implicit, and 50\% NIL.

A two-level taxonomy comprised of fine-grained and coarse-grained class levels has been designed for structuring and collection of our gold standard dataset. Our taxonomy contains 7 coarse-grained entity types, namely PERSON, ORGANIZATION, LOCATION, PRODUCT, EVENT, and WORK. These tags and the fine-grained classes pertinent to each tag are based on the DBpedia taxonomy.

Tagged tweets have been collected in a four-month time frame spanning from October 2017 to January 2018. We maintain such information as tweet ID, user ID, date, and so forth.


# Source Codes
As explained in the paper, several features have been designed to train classifiers. The source codes for extraction of these features are provided in Src folder.
