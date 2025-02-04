from django.http import JsonResponse
from django.shortcuts import render
import requests
# Create your views here.

def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_perfect(n):
    """Check if a number is a perfect number (sum of divisors excluding itself = number)."""
    return n > 1 and sum(i for i in range(1, n) if n % i == 0) == n

def is_armstrong(n):
    """Check if a number is an Armstrong number."""
    digits = [int(d) for d in str(n)]
    power = len(digits)
    return sum(d**power for d in digits) == n

def digit_sum(n):
    """Calculate the sum of digits of a number."""
    return sum(int(d) for d in str(n))

def RandomMathFacts(request):
    if request.method == 'GET':
        number = request.GET.get('number', None)

        if not number or int(number) < 0:
            return JsonResponse({'number': number, 'error': True}, status=400)
        
        if not number or not number.isdigit():
            return JsonResponse({'number': number, 'error': True}, status=400)
        

        number = int(number)

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
