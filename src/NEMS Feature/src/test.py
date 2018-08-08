# -*- coding: utf-8 -*-
"""
Created on Mon Aug 14 21:24:52 2017

@author: tam
"""

from __future__ import unicode_literals
import logging
#import ujson as json
import spacy
import sense2vec
import ujson as json
from sense2vec import util
from sense2vec.vectors import VectorMap
import pickle, codecs, os


class Similarity(object):
    '''
    Handle sense2vec similarity queries.
    '''
    def __init__(self, spacy_nlp, sense2vec_vector_map):
        self.nlp = spacy_nlp
        self.w2v = sense2vec_vector_map
        self.lemmatizer = self.nlp.vocab.morphology.lemmatizer
        self.parts_of_speech = ['NOUN', 'VERB', 'ADJ', 'ORG', 'PERSON', 'FAC',
                                'PRODUCT', 'LOC', 'GPE']
        logging.info("Serve")

    def __call__(self, query, n=100):
        # Don't return the original
        logging.info("Find best query")
        key = self._find_best_key(query)
        logging.info("Key=", repr(key))
        if not query or not key:
            return {'key': '', 'text': query, 'results': [], 'count': 0}
        text = key.rsplit('|', 1)[0].replace('_', ' ')
        results = []
        seen = set([text])
        seen.add(self._find_head(key))
        for entry, score in self.get_similar(key, n * 2):
            head = self._find_head(entry)
            freq, _ = self.w2v[entry]
            if head not in seen:
                results.append(
                    {
                        'score': score,
                         'key': entry,
                         'text': entry.split('|')[0].replace('_', ' '),
                         'count': freq,
                         'head': head
                    })
                seen.add(head)
            if len(results) >= n:
                break
        freq, _ = self.w2v[key]
        return {'text': text, 'key': key, 'results': results,
                'count': freq,
                'head': self._find_head(key)}

    def _find_best_key(self, query):
        query = query.replace(' ', '_')
        if '|' in query:
            text, pos = query.rsplit('|', 1)
            key = text + '|' + pos.upper()
            return key if key in self.w2v else None

        freqs = []
        casings = [query, query.upper(), query.title()] if query.islower() else [query]
        for text in casings:
            for pos in self.parts_of_speech:
                key = text + '|' + pos
                if key in self.w2v:
                    freqs.append((self.w2v[key][0], key))
        return max(freqs)[1] if freqs else None

    def _find_head(self, entry):
        if '|' not in entry:
            return entry.lower()
        text, pos = entry.rsplit('|', 1)
        head = text.split('_')[-1]
        return min(self.lemmatizer(head, pos))

    def get_similar(self, query, n):
        if query not in self.w2v:
            return []
        freq, query_vector = self.w2v[query]
        words, scores = self.w2v.most_similar(query_vector, n)
        return zip(words, scores)


def load(model_path='../models/reviews', via=None):
    vector_map = VectorMap(128)
    vector_map.load(model_path)
    return vector_map

def create_entity_dict(entity_annot_line, QueryOrReview):
    #inputs entity annotation of a document (query or document)
    #Format of the input file will be:
    # outputs a dictionary of {entity: (score, frequency)}
    #file = codecs.open(entity_annot_file_directory, 'r', 'utf8').read().split('\n')
    entityDict = {}
    if QueryOrReview=='query':
        entities = entity_annot_line.split(')-@-')
        entities.remove('')
        for entity in entities:
            tup=[]
            entity=entity.strip()
            entity=entity.split('##')
            namedEntity= entity[1].lstrip().rstrip()
            score= entity[2].lstrip().rstrip()
            if namedEntity in entityDict.keys():
                cnt = entityDict[namedEntity][1]
            else:
                cnt = 0
            cntt= cnt+1
            tup.append(score)
            tup.append(cntt)
            entityDict[namedEntity] =tup

    else:
        entity_annot_line= entity_annot_line.split('\n')
        for line in entity_annot_line:
            sntcs = line.split('\t')
            for sntc in sntcs:
                entities = sntc.split(')-@-')
                if '' in entities:
                    entities.remove('')
                for entity in entities:
                    tup=[]
                    entity=entity.split('##')
                    namedEntity= entity[1].rstrip().lstrip()
                    score= entity[2].rstrip().lstrip()
                    if namedEntity in entityDict.keys():
                        cnt = entityDict[namedEntity][1]
                    else:
                        cnt = 0
                    cntt= cnt+1
                    tup.append(score)
                    tup.append(cntt)
                    entityDict[namedEntity]=tup
    return entityDict


if __name__ == '__main__':
    handler = Similarity(
            spacy.load('en', parser=False, entity=False),
            load())
    '''Preparing the queries for the NN Model: Entities in the queries, unigrams in the queries, bigrams in the queries, etc'''
    query = 'Belgium|ENT'
    dict = handler(query)
    print(dict)


'''

{'text': 'Mark Wahlberg', 'key': 'Mark_Wahlberg|ENT', 'results': [{'score': 0.6611595749855042, 'key': 'Will_Ferrell|ENT', 'text': 'Will Ferrell', 'count': 441, 'head': 'ferrell'}, {'score': 0.6317983865737915, 'key': 'Denzel_Washington|ENT', 'text': 'Denzel Washington', 'count': 316, 'head': 'washington'}, {'score': 0.6177240610122681, 'key': 'Will_Ferrel|PROPN', 'text': 'Will Ferrel', 'count': 23, 'head': 'ferrel'}, {'score': 0.600273847579956, 'key': 'Marky_Mark|ENT', 'text': 'Marky Mark', 'count': 54, 'head': 'mark'}, {'score': 0.5943540930747986, 'key': 'Mila_Kunis|ENT', 'text': 'Mila Kunis', 'count': 290, 'head': 'kunis'}, {'score': 0.5698482394218445, 'key': 'Mark_Whalberg|ENT', 'text': 'Mark Whalberg', 'count': 19, 'head': 'whalberg'}, {'score': 0.5373093485832214, 'key': 'teddy_bear|NOUN', 'text': 'teddy bear', 'count': 31, 'head': 'bear'}, {'score': 0.5301126837730408, 'key': 'Denzel|ENT', 'text': 'Denzel', 'count': 378, 'head': 'denzel'}, {'score': 0.5264583230018616, 'key': 'Adam_McKay|ENT', 'text': 'Adam McKay', 'count': 20, 'head': 'mckay'}, {'score': 0.5258525609970093, 'key': 'Anthony_Mackie|ENT', 'text': 'Anthony Mackie', 'count': 51, 'head': 'mackie'}, {'score': 0.5151354670524597, 'key': 'Other_Guys|PROPN', 'text': 'Other Guys', 'count': 58, 'head': 'guys'}, {'score': 0.5063566565513611, 'key': 'Seth_MacFarlane|ENT', 'text': 'Seth MacFarlane', 'count': 79, 'head': 'macfarlane'}, {'score': 0.5014283657073975, 'key': 'Will_Farrell|ENT', 'text': 'Will Farrell', 'count': 33, 'head': 'farrell'}, {'score': 0.4899759292602539, 'key': 'Dwayne_Johnson|ENT', 'text': 'Dwayne Johnson', 'count': 243, 'head': 'johnson'}, {'score': 0.4884707033634186, 'key': "Mark_Wahlberg's|ENT", 'text': "Mark Wahlberg's", 'count': 21, 'head': "wahlberg's"}, {'score': 0.48273637890815735, 'key': 'excellent_chemistry|NOUN', 'text': 'excellent chemistry', 'count': 36, 'head': 'chemistry'}, {'score': 0.48151931166648865, 'key': 'hilarious_comedy|NOUN', 'text': 'hilarious comedy', 'count': 52, 'head': 'comedy'}, {'score': 0.48063111305236816, 'key': 'The_Rock|ENT', 'text': 'The Rock', 'count': 30, 'head': 'rock'}, {'score': 0.47645774483680725, 'key': 'Zach_Galifianakis|ENT', 'text': 'Zach Galifianakis', 'count': 221, 'head': 'galifianakis'}, {'score': 0.47458308935165405, 'key': 'Steve_Carell|ENT', 'text': 'Steve Carell', 'count': 273, 'head': 'carell'}, {'score': 0.4724138081073761, 'key': 'Mark_Walberg|ENT', 'text': 'Mark Walberg', 'count': 17, 'head': 'walberg'}, {'score': 0.4719523787498474, 'key': '_Paul_Rudd|ENT', 'text': ' Paul Rudd', 'count': 125, 'head': 'rudd'}, {'score': 0.4645739495754242, 'key': 'main_stars|NOUN', 'text': 'main stars', 'count': 43, 'head': 'stars'}, {'score': 0.46160075068473816, 'key': 'Cam_Brady|ENT', 'text': 'Cam Brady', 'count': 11, 'head': 'brady'}, {'score': 0.4600691795349121, 'key': 'Emile_Hirsch|ENT', 'text': 'Emile Hirsch', 'count': 79, 'head': 'hirsch'}, {'score': 0.4548090398311615, 'key': 'Jon_Hamm|ENT', 'text': 'Jon Hamm', 'count': 101, 'head': 'hamm'}, {'score': 0.4485180079936981, 'key': 'good_team|NOUN', 'text': 'good team', 'count': 21, 'head': 'team'}, {'score': 0.44746047258377075, 'key': 'Date_Night|ENT', 'text': 'Date Night', 'count': 18, 'head': 'night'}, {'score': 0.44273847341537476, 'key': 'Hart|ENT', 'text': 'Hart', 'count': 56, 'head': 'hart'}, {'score': 0.44149813055992126, 'key': 'Peter_Berg|ENT', 'text': 'Peter Berg', 'count': 40, 'head': 'berg'}, {'score': 0.44103413820266724, 'key': 'Micheal_Bay|ENT', 'text': 'Micheal Bay', 'count': 10, 'head': 'bay'}, {'score': 0.4405251443386078, 'key': 'Jason_Mantzoukas|ENT', 'text': 'Jason Mantzoukas', 'count': 10, 'head': 'mantzoukas'}, {'score': 0.438912570476532, 'key': 'Robert_Zemeckis|ENT', 'text': 'Robert Zemeckis', 'count': 43, 'head': 'zemeckis'}, {'score': 0.4377138018608093, 'key': 'Paula_Patton|ENT', 'text': 'Paula Patton', 'count': 30, 'head': 'patton'}, {'score': 0.43619924783706665, 'key': 'Mark_Walhberg|ENT', 'text': 'Mark Walhberg', 'count': 11, 'head': 'walhberg'}, {'score': 0.4309101104736328, 'key': 'Bullock|ENT', 'text': 'Bullock', 'count': 117, 'head': 'bullock'}, {'score': 0.43046683073043823, 'key': 'Steve_Carrel|ENT', 'text': 'Steve Carrel', 'count': 20, 'head': 'carrel'}, {'score': 0.4302973449230194, 'key': 'Chris_Pratt|ENT', 'text': 'Chris Pratt', 'count': 107, 'head': 'pratt'}, {'score': 0.427740216255188, 'key': 'Zach|ENT', 'text': 'Zach', 'count': 74, 'head': 'zach'}, {'score': 0.4269143342971802, 'key': 'great_comedians|NOUN', 'text': 'great comedians', 'count': 13, 'head': 'comedians'}


'''
