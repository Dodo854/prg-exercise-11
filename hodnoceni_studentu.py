from sorting import random_numbers

class StudentsGrades:
    def __init__(self, scores):
        self.scores = scores

    def get_by_index(self, index):
        return self.scores[index]

    def count(self):
        return len(self.scores)

    def get_grade(self, index):
        score = self.scores[index]

        if score >= 90:
            return "A"
        elif score >= 80:
            return "B"
        elif score >= 70:
            return "C"
        elif score >= 60:
            return "D"
        elif score >= 50:
            return "E"
        else:
            return "F"

    def find(self, points):
        positions = []
        for i, score in enumerate(self.scores):
            if score == points:
                positions.append(i)
        return positions


    def get_sorted(self):
        scores = self.scores.copy()
        p = len(scores)
        for i in range(p):
            swapped = False
            for j in range(0, p - i - 1):
                if scores[j] > scores[j + 1]:
                    scores[j], scores[j + 1] = scores[j + 1], scores[j]
                    swapped = True
                    if not swapped:
                        break
        return scores


def main():
    results = StudentsGrades([85, 42, 91, 67, 50, 73, 100, 38, 58])
    print(f"Test psalo: {results.count()} studentů")

    for i in range(results.count()):
        points = results.get_by_index(i)
        grade = results.get_grade(i)
        print(f"Student {i}: {points} points – {grade}")

    print(f"Studenti s indexi: {results.find(100)} měl/měli 100 bodů.")
    print(f"Vysledky vzestupně {results.get_sorted()}")

    random_results = StudentsGrades(random_numbers(30, 0, 100))
    print(f"Test psalo: {random_results.count()} studentů")

    for i in range(random_results.count()):
        points = random_results.get_by_index(i)
        grade = random_results.get_grade(i)
        print(f"Student {i}: {points} points – {grade}")

    print(f"Studenti s indexi: {random_results.find(100)} měl/měli 100 bodů.")
    print(f"Vysledky vzestupně {random_results.get_sorted()}")

if __name__ == "__main__":
    main()
