import copy
import random


class Hat:

    def __init__(self, **kwargs):
        self.contents = []
        for key, value in kwargs.items():
            for i in range(value):
                self.contents.append(key)

    def draw(self, n):
        choices = []
        if n > len(self.contents):
            return self.contents
        for i in range(n):
            k = random.randrange(0, len(self.contents), 1)
            choices.append(self.contents.pop(k))
        return choices


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    m = 0
    for i in range(num_experiments):
        temp_hat = copy.deepcopy(hat)
        drawn = temp_hat.draw(num_balls_drawn)
        temp = {}
        for j in drawn:
            temp[j] = 0
        for j in drawn:
            temp[j] += 1
        flag = True
        for j in expected_balls.keys():
            try:
                x = temp[j]
            except:
                flag = False
                break
            else:
                if temp[j] < expected_balls[j]:
                    flag = False
        if flag:
            m += 1
    return m / num_experiments


def main():
    hat = Hat(black=6, red=4, green=3)
    probability = experiment(hat=hat,
                             expected_balls={"red": 2, "green": 1},
                             num_balls_drawn=5,
                             num_experiments=2000)
    print(probability)


if __name__ == '__main__':
    main()
