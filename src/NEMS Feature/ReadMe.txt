Author: Tam T. Nguyen, Hawre Hosseini

1. copy your textual data into raw_data folder
2. run preprocess_text.py to process raw data and save it under processed_data folder
3. run train_word2vec.py to train the model
4. run gensim2sense.py to save the model under models/reviews folder
5. run test.py to extract the feature

To process the whole queries, you may run preprocess.py on query data

In order to use the results as features of MRF model, the following should be done:

1. for each unigram, use the model to extract the most relevant unigrams and use these unigrams as new input of unigram feature function
2. we can do the same for bi-grams, tri-grams....
3. for each entity, find most relevant entities, and use them as new input of entity feature functions

For instance, in our query, we have 'Marvel' as entity, we use it in our entity feature function
besides that, we find most relevant entities such as 'Sony', 'Conan', 'DC',....
we will use these entities in the input of our entity functions too
however, we may try using weighted entity feature function
0.5*f('Marvel') + 0.3*f('DC') + 0.2*f('Conan') + 0.2 * f('Sony')

The optimal weightage could be computed as well.
0.5*f('Marvel') + 0.3*f('DC') + 0.2*f('Conan') + 0.1 * f('Sony')

or the relevant score of deep learning model could be used directly.