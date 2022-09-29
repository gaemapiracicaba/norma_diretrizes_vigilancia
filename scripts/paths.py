#!/usr/bin/env python
# coding: utf-8

#!pip install sidrapy --upgrade


import os

data_path = os.path.join('..', 'data')
output_path = os.path.join(data_path, 'output')
output_path_graph = os.path.join(output_path, 'graph')


os.makedirs(output_path, exist_ok=True)
os.makedirs(output_path_graph, exist_ok=True)
