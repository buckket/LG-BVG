#!/usr/bin/env python2
# -*- coding: utf-8 -*-


import csv


bad_words = ['Yesica', 'Yesi', 'Ines', 'Nico', 'André', 'René', 'Chris', 'Petra', 'Klaus', 'Sabine', 'Dirk', 'Elma', 'Feierabend', 'verabschiede', 'verabschieden']
input_files = ['bvg_ubahn.csv', 'bvg_tram.csv', 'bvg_bus.csv']

if __name__ == '__main__':
    counter = 0

    for input_file in input_files:
        with open('data/{}'.format(input_file), 'rb') as csv_file:
            csv_reader = csv.DictReader(csv_file, delimiter=",", quotechar='\"')

            for row in csv_reader:

                # filter RTs
                if not row['Text'].startswith('RT'):

                    if not any(word in row['Text'] for word in bad_words):
                        folder = 'information'
                    else:
                        folder = 'greetings'

                    path = 'data/{}/{}.txt'.format(folder, counter)
                    print(path + ": " + row['Text'])
                    with open(path, 'w') as tfile:
                        tfile.write(row['Text'])

                    counter += 1
