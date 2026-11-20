string = "ADCBBBBCABBCBDACBDCAACDDDCAABABDBCBCBDBDBDDABBAAAAAAADADBDBCBDABADCADC"
point = {'A':4,'B':3,'C':2,'D':1}
result = sum(map(lambda s: point[s], string))
print(result)