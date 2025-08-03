

env_data = [
    {"key": "key 1", "name": "dev"},
    {"key": "key 2", "name": "prod"}
]

flag_data = [
    {'key': "flag-a",
            'name': "Flag A",
            'description': "Enables Flag A",
            'default_variation': "on",
            'enabled': True},
    {'key': "flag-b",
     'name': "Flag B",
     'description': "Enables Flag B",
     'default_variation': "on",
     'enabled': False}
]

var_data = [
    {'key': 'key a', 'value': 'value a',
        'description': 'nothing here a'},
    {'key': 'key b', 'value': 'value b',
        'description': 'nothing here b'}
]


rule_data = [
    {'variation': 'on', 'priority': 3, 'conditions': []},
    {'variation': 'off', 'priority': 2, 'conditions': []}
]


condition_data = [
    {'attribute': 'email', 'operator': '=', 'value': 'var 1'},
    {'attribute': 'name', 'operator': '<', 'value': 'val 2'}
]
