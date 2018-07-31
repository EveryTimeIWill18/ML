#!ve/bin/python3
import sys, os
import boto3
from urllib.parse import quote_plus
import requests
from functools import wraps
from sqlalchemy import create_engine
from sqlalchemy import (create_engine, MetaData,
                        Table, Column, select, or_, and_, func, INT)
from sqlalchemy.sql import text
from sqlalchemy.types import DateTime
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression, Ridge, Lasso, LogisticRegression
from sklearn.model_selection import train_test_split, cross_validate
from sklearn.metrics import (mean_squared_error, classification_report,
                             confusion_matrix, roc_curve, roc_auc_score)

from bokeh.io import output_notebook, show
from bokeh.plotting import  figure


def import_web_data(url: str) -> bytes:
    """connect to a data source"""
    url_ = str(url)
    try:
        r = requests.get(url_)
        if r.status_code == 200:
            print("Successfully connected. status[{}]".format(r.status_code))
            return r.content
        else:
            raise ConnectionError("Err: could not connec to data. status[{}]".format(r.status_code))
    except ConnectionError as e:
        print(str(e))


def import_sql_data(server: str, database: str, un: str, pw: str):
    """import data from sql"""
    driver = 'driver={SQL Server}'
    conn_string = driver + ';server={};DATABASE={};UID={};PWD={}'.format(server, database,
                                                                         un, pw)
    try:
        engine = create_engine("mssql+pyodbc:///?odbc_connect=%s" % quote_plus(conn_string))
    except:
        print("Err: Could not properly create engine.")


def preprocess_web_data(data: bytes):
    """pre-process the data into a useful format"""

    b = data.decode("utf-8").splitlines()
    data_dict_ = {str(k): [] for k in b[0].split(",")}
    rows_ = b[1:]

    for i, _ in enumerate(rows_):
        row = rows_[i].split(",")
        for j, _ in enumerate(row):
            data_dict_[list(data_dict_.keys())[j]].append(row[j])

    return pd.DataFrame(data_dict_)


def preprocess_web_decorator(data: bytes):
    """pre-process the data into a useful format"""
    @wraps(data)
    def wrapper(*args, **kwargs):
        f = data(*args, **kwargs)
        b = f.decode("utf-8").splitlines()
        data_dict_ = {str(k): [] for k in b[0].split(",")}
        rows_ = b[1:]
        for i, _ in enumerate(rows_):
            row = rows_[i].split(",")
            for j, _ in enumerate(row):
                data_dict_[list(data_dict_.keys())[j]].append(row[j])
        return pd.DataFrame(data_dict_)
    return wrapper

@preprocess_web_decorator
def wrapped_import_web_data(url: str) -> bytes:
    """connect to a data source"""
    url_ = str(url)
    try:
        r = requests.get(url_)
        if r.status_code == 200:
            print("Successfully connected. status[{}]".format(r.status_code))
            return r.content
        else:
            raise ConnectionError("Err: could not connec to data. status[{}]".format(r.status_code))
    except ConnectionError as e:
        print(str(e))


def build_model():
    """build ML model"""

def plot_data():
    """plot data visualization"""

s3 = boto3.resource("s3")
bucket = s3.Bucket("mha-nyc-poc-logstash-output-bucket")
objs = bucket.objects.filter(Prefix='http-2')

def main():
    """main function"""
    url = "https://assets.datacamp.com/production/course_5612/datasets/Big9Returns2017.csv"
    d = preprocess_web_data(data=import_web_data(url))
    dcrtr = wrapped_import_web_data(url=url)
    print(type(dcrtr['"T"']))

if __name__ == '__main__':
    main()
