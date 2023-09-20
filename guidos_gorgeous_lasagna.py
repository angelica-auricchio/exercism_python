EXPECTED_BAKE_TIME = 40
MINUTES_PREPARATION_PER_LAYER = 2

def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time


# You might also consider using 'PREPARATION_TIME' here, if you have it defined.
def preparation_time_in_minutes(number_of_layers):
    """Calculate the preparation time

    :param number_of_layers: int lasagna number of layers
    :return: int time for lasagna preparation
    """
    return number_of_layers * MINUTES_PREPARATION_PER_LAYER

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate total elapsed cooking time (prep + bake) in minutes

    :param number_of_layers: int lasagna number of layers
    :param elapsed_bake_time: int time lasagna in baker
    :return: int time of lasagna preparation
    """
    return elapsed_bake_time + preparation_time_in_minutes(number_of_layers)
    
# Remember to add a docstring (you can copy and then alter the one from bake_time_remaining.)

print('bake_time_remaining: ' + str(bake_time_remaining(20)))
print('preparation_time_in_minutes: ' + str(preparation_time_in_minutes(2)))
print('elapsed_time_in_minutes: ' + str(elapsed_time_in_minutes(4, 28)))
