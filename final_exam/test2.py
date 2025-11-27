def revert_dict(d):
    if not d:
        return {}
    return {str(v).capitalize(): str(k).upper() for k, v in d.items()}

assert revert_dict({}) == {}
assert revert_dict({"foo": "bar"}) == {"Bar": "FOO"}
