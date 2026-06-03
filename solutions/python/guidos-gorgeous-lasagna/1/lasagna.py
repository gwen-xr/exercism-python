
EXPECTED_BAKE_TIME = 40

def bake_time_remaining(elapsed_bake_time):
    """Return remaining bake time in minutes.

    Parameters:
        elapsed_bake_time (int): Minutes already spent baking.

    Returns:
        int: Remaining baking time until expected done time.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time
    

preparation_time_constant = 2

def preparation_time_in_minutes(number_of_layers):
    """Return preparation time based on number of layers.

    Parameters:
        number_of_layers (int): Number of lasagna layers.

    Returns:
        int: Total preparation time in minutes.
    """
    return preparation_time_constant*number_of_layers
    



def elapsed_time_in_minutes(number_of_layers,elapsed_bake_time):
    """Return total cooking time spent so far.

    Parameters:
        number_of_layers (int): Number of lasagna layers.
        elapsed_bake_time (int): Minutes already spent baking.

    Returns:
        int: Total time spent preparing and baking.
    """
    return number_of_layers*preparation_time_constant + elapsed_bake_time
    

