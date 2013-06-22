#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from flask import Flask, render_template, redirect, request
from wordbase import WordBase

app = Flask(__name__)
wb = WordBase('data/wordbase.txt')

@app.route('/')
def index():
	return render_template('index.html',num_of_words=wb.getNumberOfWords())

@app.route('/highlight',methods=['POST'])
def highlight():
	text = request.form.get('complete_text')
	words = [(w, wb.hasWord(w)) for w in text.split()]
	return render_template('highlight.html',words=words)

@app.route('/save',methods=['POST'])
def save():
	text = request.form.get('new_words')
	new_words = wb.saveWordsFromText(text)
	return render_template('save.html',new_words=sorted(new_words),num=len(new_words))

if __name__ == '__main__':
	app.run(debug=True)