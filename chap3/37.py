# class SimpleGradebook:
#     def __init__(self):
#         self._grades = {}
#
#     def add_student(self, name):
#         self._grades[name] = []
#
#     def report_grade(self, name, score):
#         self._grades[name].append(score)
#
#     def average_grade(self, name):
#         grades = self._grades[name]
#         return sum(grades) / len(grades)
#
#
# book = SimpleGradebook()
# book.add_student('Isaac Newton')
# book.report_grade('Isaac Newton', 90)
# book.report_grade('Isaac Newton', 95)
# book.report_grade('Isaac Newton', 85)
#
# print(book.average_grade('Isaac Newton'))

from collections import defaultdict


# class BySubjectGradebook:
#     def __init__(self):
#         self._grades = {}                       # Outer dict
#
#     def add_student(self, name):
#         self._grades[name] = defaultdict(list)  # Inner dict
#         # print(self._grades[name])
#
#     def report_grade(self, name, subject, grade):
#         # print(name, self._grades[name])
#         by_subject = self._grades[name]
#         grade_list = by_subject[subject]
#         grade_list.append(grade)
#
#     def average_grade(self, name):
#         by_subject = self._grades[name]
#         # print(by_subject)
#         total, count = 0, 0
#         for grades in by_subject.values():
#             print(by_subject.values())
#             total += sum(grades)
#             count += len(grades)
#         return total / count
#
#
# book = BySubjectGradebook()
# book.add_student('Albert Einstein')
# book.report_grade('Albert Einstein', 'Math', 75)
# book.report_grade('Albert Einstein', 'Math', 65)
# book.report_grade('Albert Einstein', 'Gym', 90)
# book.report_grade('Albert Einstein', 'Gym', 95)
# print(book.average_grade('Albert Einstein'))

class WeightedGradebook:
    def __init__(self):
        self._grades = {}

    def add_student(self, name):
        self._grades[name] = defaultdict(list)

    def report_grade(self, name, subject, score, weight):
        by_subject = self._grades[name]
        grade_list = by_subject[subject]
        # print(grade_list, self._grades[name])
        grade_list.append((score, weight))


# Example 7
    def average_grade(self, name):
        by_subject = self._grades[name]

        score_sum, score_count = 0, 0
        for subject, scores in by_subject.items():
            # print(by_subject.items())
            subject_avg, total_weight = 0, 0
            for score, weight in scores:
                subject_avg += score * weight
                total_weight += weight

            score_sum += subject_avg / total_weight
            print(score_sum, subject_avg, total_weight)
            score_count += 1

        return score_sum / score_count


# Example 8
book = WeightedGradebook()
book.add_student('Albert Einstein')
book.report_grade('Albert Einstein', 'Math', 75, 0.05)
book.report_grade('Albert Einstein', 'Math', 65, 0.15)
book.report_grade('Albert Einstein', 'Math', 70, 0.80)
book.report_grade('Albert Einstein', 'Gym', 100, 0.40)
book.report_grade('Albert Einstein', 'Gym', 85, 0.60)
print(book.average_grade('Albert Einstein'))

