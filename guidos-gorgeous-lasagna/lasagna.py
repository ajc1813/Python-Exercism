EXPECTED_BAKE_TIME=40
preparation_time_per_layer=2

def bake_time_remaining(elapsed_time):
    """Calculate how many minutes the lasagna still needs to bake 
    """
    return EXPECTED_BAKE_TIME-elapsed_time

def preparation_time_in_minutes(number_of_layers):
    """Calculate how many minutes is required to prepare 
    """
    return number_of_layers*preparation_time_per_layer

def elapsed_time_in_minutes(number_of_layers,elapsed_time):
    """
    Return elapsed cooking time.

    This function takes two numbers representing the number of layers &        the time already spent baking and calculates the total elapsed minutes     spent cooking the lasagna.
    """
    return elapsed_time+preparation_time_in_minutes(number_of_layers)

          


        

          


        

          



        

          

    """Calculate the preparation time.

        

          

 

        

          

    :param number_of_layers: int the number of lasagna layers made

        

          

    :return: int amount of prep time (in minutes), based on 2 minutes per layer added

        

          

 

        

          

    This function takes an integer representing the number of layers added to the dish,

        

          

    calculating preparation time using a time of 2 minutes per layer added.

        

          

    """

        

          


        

          

    return number_of_layers * PREPARATION_TIME

        

          


        

          


        

          

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):

        

          

    """Calculate the elapsed time.

        

          

 

        

          

    :param number_of_layers: int the number of layers in the lasagna

        

          

    :param elapsed_bake_time: int elapsed cooking time

        

          

    :return:  int total time elapsed (in in minutes) preparing and cooking

        

          

 

        

          

    This function takes two integers representing the number of lasagna layers and the time already spent baking

        

          

     and calculates the total elapsed minutes spent cooking the lasagna.

        

          

    """

        

          


        

          

    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time

        

          