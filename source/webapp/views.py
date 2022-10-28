from django.shortcuts import render


def calculate(request):
    if request.method == "GET":
        return render(request, "form_view.html")
    elif request.method == 'POST':
        try:
            num1 = float(request.POST.get('num1'))
            num2 = float(request.POST.get('num2'))
            symbol = request.POST.get('action')
            if symbol == '+':
                output = num1 + num2
            elif symbol == '-':
                output = num1 - num2
            elif symbol == '/':
                output = num1 / num2
            else:
                output = num1 * num2
            context = {
                'output': output,
                'num1': num1,
                'num2': num2,
                'symbol': symbol
            }
        except ValueError:
            context = {
                'error_message': "Input only numbers and select an action"
            }
        except ZeroDivisionError:
            context = {
                'error_message': "You can't divide by zero"
            }
        return render(request, 'math_result.html', context)
