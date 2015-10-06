#Doing math "by hand":

DATA_SET = {0: 2,
            1: 4,
            2: 6,
            3: 8}

HYPO_FUNCTION = (2, 2)


def generate_perfect_data(theta_0, theta_1, x_range):
    d = {}
    for i in x_range:
        d[i] = theta_0 + i * theta_1

    return d


def hypo_function(theta_0, theta_1):
    def the_func(x):
        return theta_0 + theta_1 * x

    return the_func


def cost_function(data_set, hypo_function):
    cost = 0.0
    for i, (x, y) in enumerate(data_set.items()):
        cost += (hypo_function(x) - y) ** 2

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


print cost_function(generate_perfect_data(2, 1, range(20)), hypo_function(-2, -2))

# print linear_gradient_descent(generate_perfect_data(2, 1, range(5)), 3, 3, 0.1)
