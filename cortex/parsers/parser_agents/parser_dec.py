

def parser(field):
    def decorator(parser):
        parser._field = field
        return parser
    return decorator