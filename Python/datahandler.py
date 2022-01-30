from statistics import *
import openpyxl

class DataHandler:
    evaluator = Stat()
    
    @classmethod
    def get_data_from_excel(cls, filename):
        dic= {}
        wb = openpyxl.load_workbook(filename)
        ws = wb.active
        g = ws.rows

        for name, score in g:
            dic[name.value] = score.value

        return dic

    def __init__(self, filename, year_class):
        self.rawdata = DataHandler.get_data_from_excel(filename)
        self.year_class = year_class
        self.cache = {}


    def get_scores(self):
        if 'scores' not in self.cache:
            self.cache['scores'] = list(self.rawdata.values())

        return self.cache.get('scores')

    def get_average(self):
        if 'average' not in self.cache:
            self.cache['average'] = self.evaluator.average(self.get_scores())

        return self.cache.get('average')

    def get_variance(self):
        if 'scores' not in self.cache:
            self.cache['variance'] = self.evaluator.variance(self.get_scores(), self.get_average())

        return self.cache.get('variance')

    def get_standard_deviation(self):
        if "standard_deviation" not in self.cache:
            self.cache["standard_deviation"] = self.evaluator.std_dev(self.get_variance())

        return self.cache.get('standard_deviation')

        
    def evaluate_class(self, total_avrg, sd):
        avrg = self.get_average()
        std_dev = self.get_standard_deviation()

        if avrg < total_avrg and std_dev > sd:
            print("성적이 너무 저조하고 학생들의 차도 큽니다.")
        elif avrg < total_avrg and std_dev < sd:
            print("성적이 저조하고, 학생 간 차이가 안납니다.")
        elif avrg > total_avrg and std_dev > sd:
            print("성적이 좋으나, 학생 간 차이가 많이나네요.")
        elif avrg > total_avrg and std_dev < sd:
            print("성적이 평균 이상이고, 학생간 차이가 크지 않습니다.")

    def get_evaluation(self, total_avrg, sd = 20):
        print("*" * 50)
        print('{} 반 성적 분석 결과'.format(self.year_class))
        print('{0}반의 평균 점수는 {1}이고, 분산은 {2}이며, 표준편차는 {3}입니다.'.format(self.year_class, self.get_average(), self.get_variance(), self.get_standard_deviation()))
        print("*" * 50)
        print("{}반 종합평가결과".format(self.year_class))
        print('*' * 50)
        self.evaluate_class(total_avrg, sd)