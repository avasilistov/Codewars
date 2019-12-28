def is_valid_walk(walk):
    if len(walk) != 10:
        return False
    dict_direction = {}
    for direction in  walk:
        dict_direction[direction] = walk.count(direction)
    if 'n' in dict_direction.keys() and dict_direction.get('n') != dict_direction.get('s'):
        return False
    if 'w' in dict_direction.keys() and dict_direction.get('w') != dict_direction.get('e'):
        return False
    if 's' in dict_direction.keys() and dict_direction.get('n') != dict_direction.get('s'):
        return False
    if 'e' in dict_direction.keys() and dict_direction.get('w') != dict_direction.get('e'):
        return False

    return True
