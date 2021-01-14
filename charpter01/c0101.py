#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
TF-IDF

@author NickZxing
@date 2021/1/14 10:20
"""

import os
import math

file_path_dir = "./data"
raw_path = "./raw.data"
idf_path = './idf.data'
file_index = 1
try:
    file_writer = open(raw_path, "w", encoding="utf-8")
    for file in os.scandir(file_path_dir):
        lines = []
        with open(file, "r", encoding="utf-8") as read:
            for line in read:
                lines.append(line.strip())
        content = '\t'.join([str(file_index), ' '.join(lines)]) + '\n'
        file_writer.writelines(content)
        file_index += 1
finally:
    if file_writer:
        file_writer.close()

try:
    file_words = []
    file_writer = open(idf_path, 'w', encoding='utf-8')
    with open(raw_path, "r", encoding="utf-8") as read:
        for line in read:
            line = line.strip().split("\t")
            if len(line) != 2:
                continue
            words = line[1].strip().split(" ")
            words = set(words)
            for word in words:
                file_words.append((word, 1))
    file_words = sorted(file_words, key=lambda x: x[0])
    word_count = 0
    current_word = None
    for word in file_words:
        w, n = word
        if not current_word:
            current_word = w
        if not current_word.__eq__(w):
            idf = math.log(file_index / (word_count + 1))
            word_content = "\t".join([current_word, str(idf)]) + "\n"
            file_writer.write(word_content)
            current_word = w
            word_count = 0
            continue
        word_count += n
    idf = math.log(file_index / (word_count + 1.0))
    word_content = "\t".join([current_word, str(idf)]) + "\n"
    file_writer.write(word_content)
finally:
    if file_writer:
        file_writer.close()
