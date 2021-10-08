def debug_control(*args,**kwargs):
    s,i,f = [0] * 3
    for lox in  args:
        if type(lox)== str:
            s+=1
        if type(lox)==int:
            i+=1
        if type(lox) == float:
            f+=1
    for j,v in kwargs.items():
        if type(v)== str:
            s+=1
        elif type(v)==int:
            i+=1
        elif type(v) == float:
            f+=1
    return f'str: {s}, int: {i}, float {f}'
