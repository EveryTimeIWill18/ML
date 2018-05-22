import os
import abc
from abc import abstractmethod
import pandas as pd

# --- setup abstract interfaces


class AbsDataPreprocessing(metaclass=abc.ABCMeta):
    """interface for data preoprocessing"""

    @abstractmethod
    def preprocess(self):
        """process data"""
        pass


class DataStruct(object):
    """stores processed data"""
    _DataSet = dict()
    _Target = dict()
    _Features = dict()


class HBCDataPreprocessing(AbsDataPreprocessing):
    """concrete implementation of AbsDataPreprocessing"""

    def __init__(self, f_path: str, file: str):
        self._f_path = f_path
        self._file = file
        self.is_open = False

    def __repr__(self):
        """machine readable print"""
        return '[{}]\n[{}]\nFile:[{}]'.format(self.__class__.__name__,
                                              self._f_path, self._file)

    def preprocess(self):
        """process data"""
        f = str(self._f_path + self._file)
        try:
            if os.path.exists(f):
                self.is_open = True
                raw_data = open(f, 'r')
                dataset_ = raw_data.readlines()
                feature_names = dataset_[0].strip('\n')\
                                           .split(",")
                features_ = dataset_[1:]
                DataStruct._DataSet = {str(h): [] for h in feature_names}
                for i, _ in enumerate(list(DataStruct._DataSet.keys())):
                    for f in features_:
                        current_feature = f.strip('\n')\
                                           .split(",")
                        for j, _ in enumerate(current_feature):
                            if j == i:
                                DataStruct._DataSet\
                                          .get(list(DataStruct._DataSet
                                                    .keys())[i])\
                                          .append(current_feature[j])
                DataStruct._DataSet = pd.DataFrame(DataStruct._DataSet)
            else:
                raise FileExistsError("Err: file not found")
        except FileExistsError as e:
            print(e)
        finally:
            if self.is_open:
                f.close()
