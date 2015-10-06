#Doing math "by hand":

DATA_SET = {0: 2,
            1: 4,
            2: 6,
            3: 8}

HYPO_FUNCTION = (2, 2)


def hypo_function(theta_0, theta_1):
    def the_func(x):
        return theta_0 + theta_1 * x

    return the_func


def cost_function(data_set, hypo_fucntion):
    cost = 0.0
    for i, (x, y) in enumerate(data_set.items()):
        cost += (hypo_fucntion(x) - y) ** 2

    return cost / (2 * len(data_set))


def linear_gradient_descent_step(data_set, theta_0, theta_1, step):
    cur_func = hypo_function(theta_0, theta_1)

    #theta_0:
    calced = 0
    for i, (x, y) in enumerate(data_set.items()):
        calced += cur_func(x) - y

    new_theta_0 = theta_0 - step * calced / len(data_set)

    #theta_1:
    calced = 0
    for i, (x, y) in enumerate(data_set.items()):
        calced += (cur_func(x) - y) * x

    new_theta_1 = theta_1 - step * calced / len(data_set)

    return new_theta_0, new_theta_1


def linear_gradient_descent(data_set, theta_0, theta_1, step):
    new_theta_0, new_theta_1 = linear_gradient_descent_step(data_set, theta_0, theta_1, step)
    while (theta_0, theta_1) != (new_theta_0, new_theta_1):
        theta_0, theta_1 = new_theta_0, new_theta_1
        new_theta_0, new_theta_1 = linear_gradient_descent_step(data_set, theta_0, theta_1, step)

    return new_theta_0, new_theta_1


print linear_gradient_descent(DATA_SET, 3, 3, 0.1)
