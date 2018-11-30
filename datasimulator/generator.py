import rstr
import random

from errors import UserError


def generate_string_data(size=10, pattern=None):
    pattern = pattern or "^[0-9a-f]{" + str(size) + "}"
    return rstr.xeger(pattern)


def generate_number(minx=0, maxx=100, is_int=False):
    return random.randint(minx, maxx) if is_int else random.uniform(minx, maxx)


def generate_list_numbers(counts, nmax=100, random=False):
    if not random:
        return [1, 1000] + [1000 * x for x in range(counts - 2)]
        # return [nmax for _ in range(counts)]
    return [
        generate_number(minx=max(1, int(0.2 * nmax)), maxx=nmax, is_int=True)
        for _ in range(counts)
    ]


def generate_boolean():
    return bool(random.getrandbits(1))


def generate_hash():
    return generate_string_data(pattern=r"^[0-9a-f]{32}")


def generate_datetime():
    return rstr.xeger(
        r"^\d\d\d\d-(0[1-9]|1[0-2])-(0?[1-9]|[12][0-9]|3[01]) (0[0-9]|1[0-9]|2[0-3]):(0[0-9]|[0-5][0-9]):(0[0-9]|[0-5][0-9])$"
    )


def generate_simple_primitive_data(data_type, pattern=None):
    """
    Generate a single primitive data
    """
    if isinstance(data_type, list):
        if "null" in data_type:
            data_type.remove("null")
        if not data_type:
            raise UserError("{} contains only null type".format(data_type))
        data_type = data_type[0]

    if data_type == "string":
        return generate_string_data(pattern=pattern)
    if data_type == "integer":
        return generate_number(is_int=True)

    if data_type == "float" or data_type == "number":
        return generate_number()

    if data_type == "boolean":
        return generate_boolean()
    raise UserError("{} is not supported".format(data_type))
