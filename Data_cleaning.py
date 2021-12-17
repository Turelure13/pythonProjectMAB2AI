import pandas as pd
import matplotlib.pyplot as plt
import scipy.signal as sc
from os import listdir
from tqdm import tqdm
import os
import glob
import numpy as np

files_path = r"/Users/arthurlefebvre/PycharmProjects/pythonProjectMAB2AIgit/database/signals/"
file_ann_path = r"/Users/arthurlefebvre/PycharmProjects/pythonProjectMAB2AIgit/database/ann_db.csv"

def get_data_from_csv(file):
    one_signal_data = pd.read_csv(file, header=0)
    return one_signal_data


def get_all_records(files_path):
    extension = 'csv'
    os.chdir(files_path)
    results = glob.glob('*.{}'.format(extension))
    files_name = []
    for item in results:
        result = os.path.splitext(item)[0]
        files_name.append(result)

    return files_name


def deleting(data):
    one_signal_data = pd.read_csv(file_ann_path, index_col=0)

    # BDecf parameter
    BDecf = one_signal_data.loc["BDecf", :].copy()
    items_to_delete = BDecf.index[BDecf[:] != BDecf[:]].tolist()
    data = data.drop(index=items_to_delete)

    # BDecf parameter
    Presentation = one_signal_data.loc["Presentation", :].copy()
    Presentation_1 = Presentation.index[Presentation[:] == 1].tolist()
    Presentation_2 = Presentation.index[Presentation[:] == 2].tolist()
    Presentation_3 = Presentation.index[Presentation[:] == 3].tolist()

    data = data.drop(index=Presentation_2)
    data = data.drop(index=Presentation_3)

    seizures = one_signal_data.loc["Seizures", :].copy()
    seizures_nbr = seizures.index[seizures[:] != 0].tolist()
    NICU_days = one_signal_data.loc["NICU days", :].copy()
    NICU_days_nbr = NICU_days.index[NICU_days[:] != 0].tolist()
    HIE = one_signal_data.loc["HIE", :].copy()
    HIE_nbr = HIE.index[HIE[:] != 0].tolist()
    Intubation = one_signal_data.loc["Intubation", :].copy()
    Intubation_nbr = Intubation.index[Intubation[:] != 0].tolist()


    Gravidity = one_signal_data.loc["Gravidity", :].copy()
    Gravidity_nbr_1 = Gravidity.index[Gravidity[:] == 1].tolist()
    Gravidity_nbr_2 = Gravidity.index[Gravidity[:] == 2].tolist()
    Gravidity_nbr_3 = Gravidity.index[Gravidity[:] == 3].tolist()
    Gravidity_nbr_4 = Gravidity.index[Gravidity[:] == 4].tolist()
    Gravidity_nbr_5 = Gravidity.index[Gravidity[:] == 5].tolist()
    Gravidity_nbr_6 = Gravidity.index[Gravidity[:] == 6].tolist()
    Gravidity_nbr_7 = Gravidity.index[Gravidity[:] == 7].tolist()
    Gravidity_nbr_8 = Gravidity.index[Gravidity[:] == 8].tolist()

    pH = one_signal_data.loc["pH", :].copy()
    severity = pd.DataFrame(Gravidity)
    severity.insert(1, "pH", pH)

    Severe_compromise_acidemia = severity.index[((severity["Gravidity"] == 8) | (severity["Gravidity"] == 7) | (severity["Gravidity"] == 6) | (severity["Gravidity"] == 5) | (severity["Gravidity"] == 4) | (severity["Gravidity"] == 3)) & (severity["pH"] < 7.05)].tolist()
    Severe_compromise_no_acidemia = severity.index[((severity["Gravidity"] == 8) | (severity["Gravidity"] == 7) | (severity["Gravidity"] == 6) | (severity["Gravidity"] == 5) | (severity["Gravidity"] == 4) | (severity["Gravidity"] == 3)) & (severity["pH"] >= 7.05)].tolist()

    Moderate_compromise = severity.index[((severity["Gravidity"] == 1) | (severity["Gravidity"] == 2) | (severity["Gravidity"] == 3)) & (severity["pH"] < 7.05)].tolist()
    Intermediate_compromise = severity.index[((severity["Gravidity"] == 1) | (severity["Gravidity"] == 2) | (severity["Gravidity"] == 3)) & ((severity["pH"] >= 7.05) & (severity["pH"] < 7.15))].tolist()
    Normal_compromise = severity.index[((severity["Gravidity"] == 1) | (severity["Gravidity"] == 2) | (severity["Gravidity"] == 3)) & (severity["pH"] >= 7.15)].tolist()




    return data




# data = retrieve_all_signals(files_path)

test = []
index = []
for rec in tqdm(get_all_records(files_path)):
    one_signal_data = get_data_from_csv(rec + '.csv')
    index.append(rec)
    test.append(one_signal_data)

df = pd.DataFrame(data= test, index=index, columns=["dataframes"])

datas = deleting(df)


print("end")