#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
@author:nali 
@file: word2vector.py 
@time: 2019/3/13/下午3:47
@software: PyCharm
"""

"""
comment here
"""

import sys
import tensorflow as tf
import numpy as np

reload(sys)
sys.setdefaultencoding("utf8")
tf.reset_default_graph()

# 3 Words Sentence
sentences = [ "i like dog", "i like cat", "i like animal",
              "dog cat animal", "apple cat dog like", "dog fish milk like",
              "dog cat eyes like", "i like apple", "apple i hate",
              "apple i movie book music like", "cat dog hate", "cat dog like"]

word_sequence = " ".join(sentences).split()
word_list = " ".join(sentences).split()
word_list = list(set(word_list))
word_list.sort()
word_dict = {w: i for i, w in enumerate(word_list)}

# Word2Vec Parameter
batch_size = 20
embedding_size = 2# To show 2 dim embedding graph
voc_size = len(word_list)

def random_batch(data, size):
    random_inputs = []
    random_labels = []
    random_index = np.random.choice(range(len(data)), size, replace=False)
    for i in random_index:
        random_inputs.append(np.eye(voc_size)[data[i][0]])  # target
        random_labels.append(np.eye(voc_size)[data[i][1]])  # context word

    return random_inputs, random_labels


skip_gram = []

for i in range(1, len(word_sequence) - 1):
    target = word_dict[word_sequence[i]]
    context = [word_dict[word_sequence[i-1]], word_dict[word_sequence[i+1]]] #上下文

    for w in context:
        skip_gram.append([target, w])

#Model
inputs = tf.placeholder(tf.float32, shape=[None, voc_size])
labels = tf.placeholder(tf.float32, shape=[None, voc_size])

#variable
W = tf.Variable(tf.random_uniform([voc_size, embedding_size], -1.0, 1.0))
WT = tf.Variable(tf.random_uniform([embedding_size, voc_size], -1.0, 1.0))

hidden = tf.matmul(inputs, W)
output = tf.matmul(hidden, WT)

cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits_v2(logits=output, labels=labels))
optimizer = tf.train.AdamOptimizer(0.001).minimize(cost)


# runner
with tf.Session() as sess:
    init = tf.global_variables_initializer()

    sess.run(init)

    for epoch in range(5000):
        batch_inputs, batch_labels = random_batch(skip_gram, batch_size)
        _,  loss = sess.run([optimizer, cost], feed_dict={inputs: batch_inputs, labels: batch_labels})

        if (epoch + 1) % 1000 == 0:
            print('Epoch:', '%04d' % (epoch + 1), 'cost =', '{:.6f}'.format(loss))

        trained_embeddings = W.eval()



if __name__ == "__main__":
    pass