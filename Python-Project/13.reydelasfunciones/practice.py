def ejemplo(a, *args, **kwargs):
    print("a:", a)
    print("args:", args)
    print(type(args))
    for a in args:
        print(a)
    print("kwargs:", kwargs)

ejemplo("hola", 20, 30, [1, 2], x=1, y=2, c="hoho")
