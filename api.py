#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 25 00:37:35 2023

@author: Rino_Geek
"""

from flask import Flask, jsonify, request

app = Flask(__name__)
app.config["DEBUG"] = True

comptes = [
    {
     'id':1,
     'name':'John',
     'surname': 'Doe',
     'email': 'johndoe@gmail.com'
     },
    {
     'id':2,
     'name':'Richi',
     'surname':'Good',
     'email': 'richi@gmail.com'
     },
    {
     'id':3,
     'name':'Naomi',
     'surname':'Lee',
     'email': 'leenaomi@gmail.com'
     },
    {
     'id':4,
     'name':'Brice',
     'surname':'Gant',
     'email': 'gbrice@gmail.com'
     }
    ]

@app.route('/', methods=['GET'])
def home():
    return "<h1>hello Flask</h1><p>this is my first code flask</p>"

@app.route('/api/v1.0/resources/comptes/all', methods=['GET'])
def api_all():
    return jsonify(comptes)

@app.route('/api/v1.0/resources/comptes', methods=['GET'])
def api():
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Erreur id introuvable! ajoutez l'id à votre requète"
    
    resultat = []
    for compte in comptes:
        if compte['id']==id:
            resultat.append(compte)
    return jsonify(resultat)

@app.route('/api/v1.0/resources/compte/like', methods=['GET'])
def like():
    result = []
    if request.args['namelike'] in request.args:
        for name in comptes:
            if request.args['namelike'] in name['name']:
                result.append(name)
    return jsonify(result)
                

app.run()