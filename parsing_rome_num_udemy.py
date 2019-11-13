
dict_rome_number = dict(I=1, V=5, X=10, L=50, C=100, D=500, M=1000)

print(dict_rome_number['X'])


# rome_num=XIV
def pars_rome_num(rome_num):
    res = 0  # сюда записываются значения по ключу
    for i, v in enumerate(rome_num):
        if i + 1 < len(rome_num) and dict_rome_number[rome_num[i]] < dict_rome_number[rome_num[i + 1]]:
            res -= dict_rome_number[v]  # работа со значения\ми словаря dict_rome_number
        else:
            res += dict_rome_number[v]
    return res


print(pars_rome_num('V') == 5)
print(pars_rome_num('IV') ==4)

print(pars_rome_num('XV') == 15)
print(pars_rome_num('XVI') == 16)
