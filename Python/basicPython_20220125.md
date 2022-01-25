20220125

# 1. 평균 점수 구하기

    from functools import reduce

    # def sum_total(total, scores):
    #     return total + score

    def get_average(scores):
        return reduce(lambda total, score: total + score, scores, 0) / len(scores)

    get_average(d.value())


# 2. 혈액형 분류하기
    #1
    def count_blood(bloods):
        blood_dict = {}

        for blood in bloods:
            # 1. 해당 혈액형이 blood_dict에 있다면, 카운트 +1
            if blood in blood_dict:
                blood_dict[blood] += 1
            # 2. 없다면, 카운트 시작
            else:
                blood_dict[blood] = 1

        return blood_dict

    count_blood(['A', 'A', 'B', 'B', 'O', 'AB'])

    #2
    def count_blood(bloods):
        blood_dict = {}

        for blood in bloods:
            if blood_dict.get[blood]:
                blood_dict[blood] += 1
            else:
                blood_dict.set_default(blood, 1)

        return blood_dict