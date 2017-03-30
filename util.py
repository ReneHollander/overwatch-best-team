import itertools


def auto_str(cls):
    def __str__(self):
        return '%s{%s}' % (
            type(self).__name__,
            ', '.join('%s=%s' % item for item in vars(self).items())
        )

    cls.__str__ = __str__
    return cls

def assign(lst, idx, value, fill=None):
    if idx < len(lst):
        lst[idx] = value
    else:
        lst.extend(itertools.repeat(fill, -(len(lst) - idx)))
        lst.append(value)