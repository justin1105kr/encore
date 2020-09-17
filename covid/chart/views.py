import pandas as pd
from django.shortcuts import render


def main_view(request):

    df = pd.read_csv(r'D:/Google Drive/20200915/covid19.csv')
    labels = list(map(str, df['stateDt'].values.tolist()[1:]))
    data = df['new'].values.tolist()[1:]
    data2 = df['clear_new'].values.tolist()[1:]

    return render(request, 'line-chart.html',{
        'labels': labels,
        'data'  : data,
        'data2' : data2
    })