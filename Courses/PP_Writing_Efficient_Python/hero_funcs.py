def convert_units(heroes_lst, heights, weights):
    new_hts = [ht * 0.39370 for ht in heights]
    new_wts = [wt * 2.20462 for wt in weights]

    heroes_dict = {}

    for i, hero in enumerate(heroes_lst):
        heroes_dict[hero] = (new_hts[i], new_wts[i])

    return heroes_dict