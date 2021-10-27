"""
Name: Jessica Andrews
weighted_average.py

Problem: Takes information from the text file and outputs averages of the students involved
"""


def weighted_average(in_file_name, out_file_name):
    avg_open = open(out_file_name, 'w')
    grades_open = open(in_file_name, 'r')
    body = grades_open.read()
    lines = body.split('\n')
    aver_list = []
    result = ""
    for line in range(len(lines)):
        w = []
        g = []
        average = 0
        separate = lines[line].split(": ")
        word = separate[1].split()
        print(word)
        # names = word[1].split(":")
        for i in range(0, len(word), 2):
            weight = eval(word[i])
            w.append(weight)
        for i in range(1, len(word), 2):
            grade = eval(word[i])
            g.append(grade)
        for i in range(len(g)):
            average = ((w[i]) * (g[i])) + average
            aver = average / 100
            aver_list.append(aver)
            result = str(round(aver,1))
        if sum(w) == 100:
            avg_open.write(separate[0] + "'s average: " + result + '\n')
        elif sum(w) < 100:
            avg_open.write(separate[0] + "'s average: Error: The weights are less than 100.\n")
        elif sum(w) > 100:
            avg_open.write(separate[0] + "'s average: Error: The weights are more than 100.\n")

    all_aver = (sum(aver_list) / len(aver_list))
    avg_open.write("Class average: " + str(round(all_aver, 1)))
    avg_open.close()
    grades_open.close()


def main():
    weighted_average("grades.txt", "avg.txt")

if __name__ == '__main__':
    main()