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
    dict_to_return = {}

    for index, arg in enumerate(args):
        if isinstance(arg, str) and "--" in arg:
            parameter = arg.replace("--", "")

            try:
                value = args[index + 1]
            except Exception as _:
                value = None
            finally:
                dict_to_return[parameter] = value

    return dict_to_return
