class Course:
    def __init__(self, category, cost, credit, hours):
        self.category = category
        self.cost = cost
        self.credit = credit
        self.hours = hours


def initialize_dictionary():
    return dict(c1=Course("c1", 1000, 5, 80), c2=Course("c2", 800, 3, 40), c3=Course("c3", 1500, 8, 100))


def cost(courses_d, s):
    return s[0] * courses_d['c1'].cost + s[1] * courses_d['c2'].cost + s[2] * courses_d['c3'].cost


def wa_hours(courses_d, s):
    return (s[0] * courses_d['c1'].hours + s[1] * courses_d['c2'].hours + s[2] * courses_d['c3'].hours) / (
                s[0] + s[1] + s[2])


def sum_credit(courses_d, s):
    return s[0] * courses_d['c1'].credit + s[1] * courses_d['c2'].credit + s[2] * courses_d['c3'].credit


def wa_credit(courses_d, s):
    return (s[0] * courses_d['c1'].credit + s[1] * courses_d['c2'].credit + s[2] * courses_d['c3'].credit) / (
                s[0] + s[1] + s[2])


def main():
    max_budget = 10000
    max_hours = 700
    courses_dict = initialize_dictionary()
    print(f"In the main function with value {courses_dict}")
    (n1, n2, n3) = (max_budget // courses_dict['c1'].cost, max_budget // courses_dict['c2'].cost,
                    max_budget // courses_dict['c3'].cost)
    print(n1, n2, n3)
    solution = [0, 1, 1]
    for i1 in range(1, n1):
        for i2 in range(1, n2):
            for i3 in range(1, n3):
                print(i1, i2, i3)
                wa_hours_new = wa_hours(courses_dict, [i1, i2, i3])
                wa_credit_new = wa_credit(courses_dict, [i1, i2, i3])
                wa_cost_new = cost(courses_dict, [i1, i2, i3])
                if wa_credit(courses_dict, solution) < wa_credit_new and \
                        wa_hours_new <= max_hours and \
                        wa_cost_new <= max_budget:
                    solution = [i1, i2, i3]
    print(f"Solution {solution}")
    print(f"Budget {cost(courses_dict, solution)}")
    print(f"Credit {sum_credit(courses_dict, solution)}")
    print(f"Solution {solution}")


if __name__ == "__main__":
    main()
    print('Done')
