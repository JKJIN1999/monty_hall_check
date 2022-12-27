import random


def monti_hall_result(car, total_door, show, time):
    correct = 0
    wrong = 0
    if show == 0:
        show = total_door-car - 1
    for _ in range(time):
        goat = total_door - car
        doors_list = [0] * total_door
        car_nums = random.sample(range(total_door), car)
        # first choice exception list
        first_choice = random.choice(range(total_door))
        # left choice after showing one goat
        reveal_goat = random.sample([x for x in range(total_door) if x not in car_nums and x != first_choice], show)
        left_choice = [x for x in range(total_door) if x != first_choice and x != reveal_goat]
        if first_choice in car_nums:
            correct += 1
        else:
            wrong += 1
    return correct, wrong
