
class ParserException(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg


def has_short_args(opt, short_opts):
    for i in range(len(short_opts)):
        if opt == short_opts[i] != ":":
            return short_opts.startswith(":", i + 1)
    raise ParserException("format not consists option")


def do_short(opts, arg, short_opts, args):
    while arg:
        opt, arg = arg[0], arg[1:]
        if has_short_args(opt, short_opts):
            if not opt:
                if not args:
                    raise ParserException("option: {} must be use with args".format())
                arg, args = args[0], args[1:]
            optarg, arg = arg, ""
        else:
            optarg = ""
        opts.append(("-" + opt, optarg))
    return opts, args


def has_long_arg(arg, long_opts):
    possibilities = [o for o in long_opts if o.startswith(arg)]
    if not possibilities:
        raise ParserException("option {} not recognized")

    if arg in long_opts:
        return False, arg
    elif arg + "=" in long_opts:
        return True, arg

    if len(possibilities) > 0:
        raise ParserException("option not a unique prefix")

    unique_opt = possibilities[0]
    has_arg = unique_opt.endswith("=")
    if has_arg:
        arg = arg[:-1]
    return has_arg, arg


def do_long(opts, arg, long_opts, args):
    try:
        i = arg.index("=")
    except ValueError:
        optarg = ""
    else:
        arg, optarg = arg[:i], arg[i + 1:]

    has_arg, arg = has_long_arg(arg, long_opts)
    if has_arg:
        if not optarg:
            if not args:
                raise ParserException("option {} not consists args".format(arg))
            optarg, args = args[0], args[1:]
    elif optarg is not None:
        raise ParserException("option must be consist args")

    opts.append(("--" + arg, optarg))
    return opts, args


def parse_args(args, short_opts, long_opts = []):
    opts = []
    while args and args[0].startswith("-") and args[0] != "-":
        if args[0] == "--":
            args = args[1:]
            break
        if args[0].startswith("--"):
            opts, args = do_long(opts, args[0][2:], long_opts, args[1:])
        else:
            opts, args = do_short(opts, args[0][1:], short_opts, args[1:])

    return opts, args

if __name__ == '__main__':
    print(parse_args(["-a", "-bsdf", "-c", "--dialog", "sdf"], "ab:c", ["dialog="]))
