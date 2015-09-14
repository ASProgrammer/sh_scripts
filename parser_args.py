
def parse_args(args, short_opts, long_opts = []):
    opts = []
    while args and args[0].startswith("-") and args[0] != "-":
        if args[0] == "--":
            args = args[1:]
            break
        if args[0].startswith("--"):
            break;
        else:
            break
    return opts, args

if __name__ == '__main__':
    parse_args(["-a", "-b", "-cafd", "--dialog=sdf"], "abc:", ["dialog="])