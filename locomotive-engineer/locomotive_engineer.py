"""Functions which helps the locomotive engineer to keep track of the train."""


# TODO: define the 'get_list_of_wagons' function
def get_list_of_wagons(*wagon_id):
    """Return a list of wagons.

    :param: arbitrary number of wagons.
    :return: list - list of wagons.
    """
    return list(wagon_id)


# TODO: define the 'fixListOfWagons()' function
def fix_list_of_wagons(each_wagons_id, missing_wagons):
    """Fix the list of wagons.

    :parm each_wagons_id: list - the list of wagons.
    :parm missing_wagons: list - the list of missing wagons.
    :return: list - list of wagons.
    """
    
    a,b,c,*last=each_wagons_id
    new_wagon=[a,b]
    loco_id=[c]
    *wagon_list, = *loco_id, *missing_wagons, *last, *new_wagon
    return wagon_list

# TODO: define the 'add_missing_stops()' function
def add_missing_stops(route,**stops):
    """Add missing stops to route dict.

    :param route: dict - the dict of routing information.
    :param: arbitrary number of stops.
    :return: dict - updated route dictionary.
    """
    
    return {**route, **{"stops":list(stops.values())}}

# TODO: define the 'extend_route_information(route,more_route)' function
def extend_route_information(route, more_route_information):
    """Extend route information with more_route_information.

    :param route: dict - the route information.
    :param more_route_information: dict -  extra route information.
    :return: dict - extended route information.
    """
    return {**route, **more_route_information}


# TODO: define the 'fix_wagon_depot()' function
def fix_wagon_depot(wagons_rows):
    """Fix the list of rows of wagons.

    :param wagons_rows: list[tuple] - the list of rows of wagons.
    :return: list[tuple] - list of rows of wagons.
    """

    a,b,c=wagons_rows
    x,y,z=zip(tuple(a),tuple(b),tuple(c)) 
    return [list(x),list(y),list(z)]


