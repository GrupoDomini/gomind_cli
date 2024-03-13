def get_sys_args_as_dict() -> dict:
    """Retorna os parâmetros do terminal

    Example:
        Terminal Command: `python main.py --name Hello-world`
        Function Output: `{'name': 'Hello-world'}`

    Returns:
        dict: Um dict contendo os parâmetros e seus respectivos valores
    """
    import sys

    args = sys.argv

    for index, arg in enumerate(args):
        if isinstance(arg, str) and "--params" == arg:
            return json.loads(args[index + 1])

    return {}
