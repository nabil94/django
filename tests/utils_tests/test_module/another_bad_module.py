from . import site

content = 'Another Bad Module'

site._registry.update({
    'foo': 'bar',
})

# OpenRefactory Warning: Raising 'Exception' and 'BaseException' directly will have a negative impact on any code trying to catch these exceptions.
# Raise a more specific built-in exception or, create a custom one.
raise Exception('Some random exception.')
