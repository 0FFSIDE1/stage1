import requests
from django.http import JsonResponse

def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(abs(n) ** 0.5) + 1):  # Handle negative numbers correctly
        if abs(n) % i == 0:
            return False
    return True

def is_perfect(n):
    """Check if a number is a perfect number."""
    return abs(n) > 1 and sum(i for i in range(1, abs(n)) if abs(n) % i == 0) == abs(n)

def is_armstrong(n):
    """Check if a number is an Armstrong number."""
    digits = [int(d) for d in str(abs(n))]
    power = len(digits)
    return sum(d**power for d in digits) == abs(n)

def digit_sum(n):
    n = abs(n)  # Work with absolute value
    total = 0  # Initialize total sum
    for digit in str(n):  # Iterate through each digit
        total += int(digit)  # Add it manually
    
    return total

def RandomMathFacts(request):
    if request.method == 'GET':
        number = request.GET.get('number', None)

        # Validate input
        if number is None:
            return JsonResponse({'number': number,'error': True}, status=400)

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
