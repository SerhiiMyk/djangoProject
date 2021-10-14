from django.shortcuts import render


# Create your views here.

def calc(request, a, operation, b):
    res = 'wrong'
    try:
        a = int(a)
        b = int(b)
        if operation == '+':
            res = f'{a}{operation}{b}={a + b}'
        elif operation == '-':
            res = f'{a}{operation}{b}={a - b}'
        elif operation == ':':
            res = f'{a}{operation}{b}={a / b}'
        elif operation == '*':
            res = f'{a}{operation}{b}={a * b}'
    except Exception:
        pass
    return render(request, 'calcRes.html', {'res': res})
