def openOrSenior(data):
    return ['Open' if mem[0] < 55 or mem[1] < 8 else 'Senior' for mem in data]



