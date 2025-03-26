from flask import Flask, request, jsonify
from typing import Optional, List, Union
import math

app = Flask(__name__)

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Эндпоинт 1: Генерация чисел Фибоначчи
@app.route('/api/fibonacci', methods=['GET'])
def get_fibonacci():
    try:
        n = request.args.get('n', type=int)
        if n is None:
            return jsonify({"error": "Parameter 'n' is required"}), 400
        
        if not isinstance(n, int) or n <= 0:
            return jsonify({"error": "n must be a positive integer"}), 400

        if n == 1:
            return jsonify({"sequence": [0]})
        
        fib_sequence = [0, 1]
        for _ in range(2, n):
            fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        
        return jsonify({"sequence": fib_sequence[:n]})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Эндпоинт 2: Проверка на палиндром
@app.route('/api/palindrome', methods=['GET'])
def check_palindrome():
    try:
        number = request.args.get('number', type=int)
        if number is None:
            return jsonify({"error": "Parameter 'number' is required"}), 400
        
        if not isinstance(number, int) or number < 0:
            return jsonify({"error": "number must be a non-negative integer"}), 400

        str_num = str(number)
        is_palindrome = str_num == str_num[::-1]
        return jsonify({"is_palindrome": is_palindrome, "number": number})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Эндпоинт 3: Разворот связного списка
@app.route('/api/reverse-linked-list', methods=['POST'])
def reverse_linked_list():
    try:
        data = request.get_json()
        if not data or 'list' not in data:
            return jsonify({"error": "JSON body with 'list' array is required"}), 400
        
        input_list = data['list']
        if not isinstance(input_list, list):
            return jsonify({"error": "'list' must be an array"}), 400

        # Конвертируем список в связный список
        if not input_list:
            return jsonify({"reversed_list": []})
        
        head = ListNode(input_list[0])
        current = head
        for val in input_list[1:]:
            current.next = ListNode(val)
            current = current.next

        # Разворачиваем связный список
        prev = None
        current = head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        # Конвертируем обратно в список
        reversed_list = []
        current = prev
        while current:
            reversed_list.append(current.val)
            current = current.next

        return jsonify({"reversed_list": reversed_list})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
