from ML_one import (AbsDataPreprocessing, HBCDataPreprocessing)

f_path='E:\\'
file = 'Gilt_datascience_exercise.csv - Gilt_datascience_exercise.csv.csv'


read_data_ = HBCDataPreprocessing(f_path=f_path, file=file)

print(read_data_.file_path)
