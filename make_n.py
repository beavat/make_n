import itertools
import pprint

OPERATOR = ['+', '-', '*', '/']

def make_n(num_list, ans):
    ope_list = list(itertools.product(OPERATOR, repeat=3))
    for v in itertools.permutations(num_list):
        ll = list(v)
        for ope_l in ope_list:
            fomula_list = []
            for i in range(len(ope_l)):
                fomula_list.append(ll[i])
                fomula_list.append(ope_l[i])
            fomula_list.append(ll[-1])
            for i in range(len(fomula_list) - 2):
                # print(fomula_list[i].isdecimal,isinstance(fomula_list[i], int))
                if fomula_list[i].isdecimal():
                    tmp_fomula = []
                    tmp_fomula.extend(fomula_list)
                    tmp_fomula.insert(i, '(')
                    for j in range(i + 2, len(tmp_fomula) - 1):
                        # print(tmp_fomula)
                        if tmp_fomula[j].isdecimal():
                            tmp_fomula2 = tmp_fomula[:j+1]
                            tmp_fomula2.extend(')')
                            tmp_fomula2.extend(tmp_fomula[j+1:])
                            fomula = ' '.join(tmp_fomula2)
                            print(f'{fomula}')
                            try:
                                if eval(fomula) == ans:
                                    print(f'!!!{fomula} = {ans}!!!')
                                    return
                            except ZeroDivisionError:
                                pass
    print('Unresolved!!!!!!!!')
            

if __name__ == '__main__':
    num_list = ['4', '8', '8', '9']
    ans = 23
    make_n(num_list, ans)