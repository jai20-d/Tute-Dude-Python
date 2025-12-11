operand_1=int(input('enter operand1: '))
operand_2=int(input('enter operand2: '))
operator=input('enter operator (+,-,/,*):  ')
if operator=='+':
    print(operand_1+operand_2)
elif operator=='-':
    print(operand_1-operand_2)
elif operator=='/':
    print(operand_1/operand_2)
elif operator=='*':
    print(operand_1*operand_2)
else:
    print('invalid operator')

print('thank you')