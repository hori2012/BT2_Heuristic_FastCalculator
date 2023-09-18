import math
#Kiem tra tinh hop le cua bieu thuc
#Chi kiem tra bieu thuc chua so va toan tu
def valid_expression(exprs):
    operators = ['+', '-', '*']
    for x in range(len(exprs)):
        if not(exprs[x].isdigit() or exprs[x] in operators):
            return False
        if exprs[x] == '-' and exprs[x + 1] == '*':
            return False
        if exprs[x] == '*' and exprs[x + 1] == '*':
            return False
        if exprs[x] == '+' and exprs[x + 1] == '*':
            return False
    if exprs[len(exprs) - 1].isdigit() == False:
        return False
    return True   
        
#Kiem tra dang cua bieu thuc
#Bieu thuc chi  phep cong hoac tru '+', '-' thi tra ve 0
#Bieu thuc chi phep nhan '*' thi tra ve 1
#Bieu thuc chi co +, -, * thi tra ve -1
def check_expression(exprs):
    operators = ['+','-','*']
    terms = []
    char = ''
    for x in exprs:
        if x in operators:
            char += x
        elif x.isdigit():
            if char != '':
                terms.append(char)
                char = ''
    if ('-' in terms or '+' in terms) and ('*' in terms or '*-' in terms):
        return -1
    elif ('*' in terms or '*-' in terms) and ('-' not in terms and '+' not in terms):
         return 1
    return 0

#Bien doi bieu thuc
def transform_expression(exprs):
    result = exprs
    result = result.replace('++', '+')
    result = result.replace('+-', '-')
    result = result.replace('--', '+')
    result = result.replace('-+', '-')
    result = result.replace('*+', '*')
    return result

#Quy tac 1: Cac so hang doi nhau
def combine_terms_rul1(expr):
    terms = []
    term = ''
    result = ''
    for char in expr:
        if char.isdigit() or (char == '-' and term == ''):
            term += char
        else:
            terms.append(int(term))
            term = char
    terms.append(int(term))
    i = 0
    terms_copy = terms.copy()
    for term in terms_copy:
        if term in terms and -term in terms:
            terms.remove(term)
            terms.remove(-term)
    for i, x in enumerate(terms):
        if x < 0 or i == 0:
            result += str(x)
        else:
            result = result + '+' + str(x)
    return result

#Quy tac 2: Gom nhóm các số hạng có tổng tròn trăm ,tròn chục, tròn nghìn.
def combine_terms_rul2(expr):
    terms = []
    term = ''
    for char in expr:
        if char.isdigit() or (char == '-' and term == ''):
            term += char
        elif char == '-' and term != '':
            terms.append(int(term))
            term = char
        else:
            terms.append(int(term))
            term = ''
    terms.append(int(term))
    terms_copy = terms.copy()
    for i1, term1 in enumerate(terms_copy):
        for i2, term2 in enumerate(terms_copy):
            if i1 == i2:
                 continue
            elif (term1 + term2) % 10 == 0 and (term1 in terms and term2 in terms):
                terms.remove(term1)
                terms.remove(term2)
                terms.append(term1 + term2)
                break
    result = ''
    for i, x in enumerate(terms):
        if x < 0 or i == 0:
            result += str(x)
        else:
            result = result + '+' + str(x)
    return result

#Quy tac 3: Nhan voi 0
def combine_terms_rul3(exprs):
    for i in range(len(exprs)):
        if exprs[i] == '*' and exprs[i+1] == '0':
            return '0'
    return exprs

#Quy tac 4: Gom nhom cac so hang co tich tron tram, tron chuc, tron nghin
def combine_terms_rul4(expr):
    terms = []
    term = ''
    for char in expr:
        if char.isdigit() or char == '-':
            term += char
        elif char == '*':
            terms.append(int(term))
            term = ''
    terms.append(int(term))
    print(terms)
    # for i1, val1 in enumerate(terms):
    #     for i2, val2 in enumerate(terms):
    #         if i1 == i2:
    #             continue
    #         elif (val1*val2) % 10 == 0:
    #             terms.append(val1 * val2)
    #             break
    return "Hello"

#Quy tac 5: Bo cac so 0 sau ket qua, va them lai cac so 0 vao ket qua cuoi cung
def combine_terms_rul5(expr):
    terms = []
    term =''
    for char in expr:
        if char.isdigit():
            term += char
        else:
            terms.append(term)
            terms.append(char)
            term = ''
    terms.append(term)
    zero = 0
    count = 0
    for i in range(0, len(terms), 2):
        if '0' in terms[i]:
            for j in terms[i]:
               if j.isdigit() and j !='0':
                   count+=1
            zero += (len(terms[i]) - count)
            terms[i] = terms[i][0:count]
            count = 0
    terms.append({'zero': zero})
    terms[0:(len(terms) - 1)] = [''.join(str(x) for x in terms[0:(len(terms) - 1)])]
    return terms

#Quy tac 6: Dat thua so chung

#Quy tac 7: Tinh tuan tu
def combine_terms_rul7(exprs):
    return eval(exprs)

#Main 
while True:
    exprs = str(input("Enter the expression to calculate: "))
    while not valid_expression(exprs):
        exprs = str(input("Enter the expression to calculate: "))
    exprs = transform_expression(exprs)
    exprs = exprs.replace(' ', '')
    if check_expression(exprs) == 0 and exprs !='':
        #Expression sample: 2+5-2+8-7-5+8+2-7+9
        print("After apply rules 1: ",combine_terms_rul1(exprs))
        print("After apply rules 2: ",combine_terms_rul2(combine_terms_rul1(exprs)))
        print("Result: ",combine_terms_rul7(combine_terms_rul2(combine_terms_rul1(exprs))))
    elif check_expression(exprs) == 1 and exprs !='':
       #Expression example 25*10*5*20*4*100
       if combine_terms_rul3(exprs) == '0':
            print("Result: ",combine_terms_rul3(exprs))
       else:
            print("After apply rules 4: ",combine_terms_rul4(exprs))
            my_list = combine_terms_rul5(exprs)
            print(my_list)
            result = str(combine_terms_rul7(my_list[0])) + ('0' * my_list[1]['zero'])
            print("(After apply rules 5)Result: ", result)
    else:
        break