types_to_check = [str, int, list, range, dict, bool, bytes, type(None)]

for t in types_to_check:
    print(f"Typ bazowy dla {t.__name__}: {t.__base__} : type(): {type(t)}")
