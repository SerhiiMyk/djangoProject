from django.shortcuts import render


# Create your views here.

def calc(request, a, operation, b):



    if type(a) is int:
        check = True
        if operation == '+':
            return render(request, 'calcRes.html',
                          {'a': a, 'operation': operation, 'b': b, 'res': a + b, 'check': check})
        elif operation == '-':
            return render(request, 'calcRes.html',
                          {'a': a, 'operation': operation, 'b': b, 'res': a - b, 'check': check})
        elif operation == 'div':
            operation = '/'
            return render(request, 'calcRes.html',
                          {'a': a, 'operation': operation, 'b': b, 'res': a / b, 'check': check})
        elif operation == '*':
            return render(request, 'calcRes.html',
                          {'a': a, 'operation': operation, 'b': b, 'res': a * b, 'check': check})
        else:
            check = False
            return render(request, 'calcRes.html',
                          {'a': a, 'operation': operation, 'b': b, 'res': 'wrong', 'check': check})
    else:
        check = False
        return render(request, 'calcRes.html', {'res': 'wrong', 'check': check})
