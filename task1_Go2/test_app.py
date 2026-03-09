import subprocess
import json
import time


def python_sum_squares(numbers):
    total = 0
    for n in numbers:
        time.sleep(0.1)
        total += n * n
    return total

def run_go_calculator(numbers):
    proc = subprocess.Popen(
        ["./calculator"], 
        stdin=subprocess.PIPE, 
        stdout=subprocess.PIPE, 
        stderr=subprocess.PIPE
    )
    input_data = json.dumps({"numbers": numbers})
    stdout, _ = proc.communicate(input_data.encode())
    return json.loads(stdout.decode())

def test_compare_python_vs_go_goroutines():
    numbers = [1, 2, 3, 4, 5]
    
    start_py = time.time()
    py_result = python_sum_squares(numbers)
    end_py = time.time()
    py_duration = end_py - start_py
    
    start_go = time.time()
    go_result = run_go_calculator(numbers)
    end_go = time.time()
    go_duration = end_go - start_go
    
    print(f"\n--- Сравнение производительности ---")
    print(f"Python (последовательно): {py_duration:.4f} сек, Результат: {py_result}")
    print(f"Go (горутины):         {go_duration:.4f} сек, Результат: {go_result['sum']}")
    
    assert py_result == go_result["sum"]
    
    assert go_duration < py_duration
    print(f"Ускорение в {py_duration / go_duration:.1f} раз!")

