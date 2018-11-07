def evaluateActions(actions):

    locations, supporters, attacked, supports = {}, set(), set(), {}

    # move armies
    for action in actions:
        action = action.split()
        supports[action[0]] = 1
        if action[2] == 'Move':
            army = action[0]
            dst = action[3]
            # check if army should be removed from 'from'
            attacked.add((dst, army))
            if dst in locations:
                locations[dst].add(army)
            else:
                locations[dst] = {army}
        elif action[2] == 'Support':
            supporter, dst, supported = action[0], action[1], action[3]
            supporters.add((supporter, supported))
            if dst in locations:
                locations[dst].add(supporter)
            else:
                locations[dst] = {supporter}
        elif action[2] == 'Hold':
            dst = action[1]
            if dst in locations:
                locations[dst].add(action[0])
            else:
                locations[dst] = {action[0]}

    # remove attacked supporters
    ignored_support = set()

    for loc, attacker in attacked:
        for resident in list(locations.get(loc)):
            if resident != attacker:
                ignored_support.add(resident)

    for support in list(supporters):
        if support[0] in ignored_support:
            supporters.remove(support)

    for supporter, supported in supporters:
        supports[supported] += 1

    result = {}
    # evaluate units
    for loc, residents in locations.items():
        max_support = supports[max(residents, key=lambda res: supports[res])]
        victorious = filter(lambda army: supports[army] == max_support, residents)

        for res in residents:
            result[res] = '[dead]'
        if len(victorious) == 1:
            result[victorious[0]] = loc

    final_res = []
    for res, loc in result.items():
        final_res.append(res + ' ' + loc)

    return sorted(final_res)


actions = ['A Munich Hold', 'B Bohemia Move Munich', 'C Warsaw Support B']
print(evaluateActions(actions))

