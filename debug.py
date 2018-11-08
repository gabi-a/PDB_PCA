import inspect
def debug():
    print(f"Breakpoint on line {inspect.currentframe().f_back.f_lineno} hit")
    while True:
        try:
            cmd = input()
            exec(cmd)
        except EOFError:
            return
        except Exception as e:
            print(e)