import math
import requests
from django.http import JsonResponse

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def is_perfect(n):
    if n <= 0:
        return False
    return sum(i for i in range(1, n) if n % i == 0) == n

def is_armstrong(n):
    num_str = str(abs(n))  # Convert to string and ignore sign
    num_digits = len(num_str)
    return sum(int(digit) ** num_digits for digit in num_str) == abs(n)

def digit_sum(n):
    return sum(int(digit) for digit in str(abs(n)))  # Ignore sign

def RandomMathFacts(request):
    if request.method == 'GET':
        number = request.GET.get('number', None)

        # Validate input
        if number is None or not number.lstrip("-").isdigit():
            return JsonResponse({"number": number, "error": True}, status=400)

        # Allow negative numbers but reject alphabets & 0
        try:
            number = int(number)  # Convert string to integer
            if number == 0:
                return JsonResponse({'number': number,'error': True}, status=400)
        except ValueError:
            return JsonResponse({'number': number,'error': True}, status=400)

        try:
            # Fetch math fact
            response = requests.get(f'http://numbersapi.com/{number}')
            response.raise_for_status()
            fun_fact = response.text

            # Compute properties
            properties = []
            if is_armstrong(number):
                properties.append("armstrong")
            if number % 2 == 1:
                properties.append("odd")
            else:
                properties.append("even")

            context = {
                "number": number,
                "is_prime": is_prime(number),
                "is_perfect": is_perfect(number),
                "properties": properties,
                "digit_sum": digit_sum(number),
                "fun_fact": fun_fact
            }
            return JsonResponse(context, status=200)

        except requests.exceptions.RequestException as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)

    return JsonResponse({'status': 'error', 'message': 'Method not allowed'}, status=405)
