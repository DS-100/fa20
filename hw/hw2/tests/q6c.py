test = {   'name': 'q6c',
    'points': 1,
    'suites': [   {   'cases': [   {'code': '>>> len(simulations) == 100000\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> sum([-1 < x < 1 for x in simulations]) == len(simulations)\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> abs(np.mean(simulations) - 0.007) <= 0.016\nTrue', 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
