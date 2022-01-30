from note3 import *

if __name__ == "__main__":
    raw_data = get_data('C:/Users/Ayaan/Desktop/vscode_workspace/python_study/Python/class_2_3.xlsx')
    scores = list(raw_data.values())

    avrg = average(scores)
    var = variance(scores, avrg)
    std = std_dev(var)

    print("평균 : {}, 분산 : {}, 표준편차 :{}".format(avrg, var, std))

    evaluation(avrg, 65, std, 20)