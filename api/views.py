import math
import requests
from django.http import JsonResponse
from django.views import View

class NumberView(View):
    def get(self, request):
        number = request.GET.get("number")
        if number is None or not number.lstrip("-").isdigit():
            return JsonResponse({"number": number, "error": True}, status=400)
        number = int(number)
        response_data = {
            "number": number,
            "is_prime": self.is_prime(number),
            "is_perfect": self.is_perfect(number),
            "properties": self.get_properties(number),
            "digit_sum": self.digit_sum(number),
            "fun_fact": self.get_fun_fact(number),
        }
        return JsonResponse(response_data, status=200)
    def is_prime(self, n):
        if n < 2:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True
    def is_perfect(self, n):
        if n <= 0:
            return False
        return sum(i for i in range(1, n) if n % i == 0) == n
    def is_armstrong(self, n):
        num_str = str(abs(n)) 
        num_digits = len(num_str)
        return sum(int(digit) ** num_digits for digit in num_str) == abs(n)
    def get_properties(self, n):
        properties = ["even" if n % 2 == 0 else "odd"]
        if self.is_armstrong(n):
            properties.insert(0, "armstrong")
        return properties
    def digit_sum(self, n):
        return sum(int(digit) for digit in str(abs(n)))
    def get_fun_fact(self, n):
        try:
            response = requests.get(f"http://numbersapi.com/{n}/math", timeout=5)
            if response.status_code == 200:
                return response.text
        except requests.exceptions.RequestException:
            pass
        return "No fun fact available."
