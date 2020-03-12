

def listener(scheme):
    def decorator(f):
        f._scheme = scheme
        return f
    return decorator