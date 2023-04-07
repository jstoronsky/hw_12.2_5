def get_val(collection, key, default='lancer'):
    """
    :param collection: исходный словарь.
    :param key: ключ.
    :param default: значение по-умолчанию.
    :return: значение по ключу или значение по-умолчанию.
    """
    if key in collection.keys():
        return collection[key]

    return default
