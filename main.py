import re
import numpy as np
from scipy import spatial

with open('sentences.txt', 'r') as file:
    f = file.readlines()


def creating_dict_uniq_words(f):  # Создаем словарь уникальных слов из всех предложений
    for i, s in enumerate(f):
        f[i] = s.strip('\n').lower()
    uniq_words = {}
    d = 0  # Число раличных слов в предложениях
    for j, sentence in enumerate(f):
        for i in re.split('[^a-z]', sentence):
            if i != '' and i not in uniq_words.values():
                uniq_words[d] = i
                d += 1
    return uniq_words


def creating_matr(uniq_words):  # Создаем матрицу
    matr = np.arange(len(f) * len(uniq_words)).reshape(len(f), len(uniq_words))
    return matr


def matr_occupancy(matr, uniq_words):  # Заполняем матрицу вхождением слов в предложения
    for i, row in enumerate(matr):
        for j, element in enumerate(row):
            matr[i][j] = f[i].count(uniq_words[j])
    return matr


def find_same_sentences(matr):  # С помощью косинусного расстояния находим похожие предложения
    the_samest_sentence_1 = 0
    the_samest_sentence_2 = 0
    nums_of_sentences = [0, 0]
    for i, row in enumerate(matr[1:-1]):
        dis = 1 - (spatial.distance.cosine(matr[0], row))
        if dis > the_samest_sentence_1:
            the_samest_sentence_2 = the_samest_sentence_1
            the_samest_sentence_1 = dis
            nums_of_sentences[1] = nums_of_sentences[0]
            nums_of_sentences[0] = i + 1
        elif dis > the_samest_sentence_2:
            the_samest_sentence_2 = dis
            nums_of_sentences[1] = i + 1
    return ' '.join(map(str, nums_of_sentences))


cr_u_w = creating_dict_uniq_words(f)
cr_m = creating_matr(cr_u_w)
m_o = matr_occupancy(cr_m, cr_u_w)
sentences = find_same_sentences(m_o)
with open('submission-1.txt', 'w') as file:
    file.write(sentences)
