def KebapCaseToPascalCase(value):
    return "".join(x for x in value.title() if not x == "-")