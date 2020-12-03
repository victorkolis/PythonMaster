# data_structures.py

import pprint

# The dictionary list below is a data structure
child = {'name': 'Isaac', 'age': 2, 'gender': 'M'}

children = []
children += [child]
children += [{'name': 'Peter', 'age': 0, 'gender': 'M'}]
children += [{'name': 'Rebecca', 'age': 0, 'gender': 'F'}]
children += [{'name': 'Levi', 'age': 0, 'gender': 'M'}]
children.append({'name': 'Judah', 'age': 0, 'gender': 'M'})

pprint.pprint(children)
