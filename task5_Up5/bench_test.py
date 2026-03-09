import pytest
import math
import subprocess
import json
import fastmath

N = 1_000_000  

def python_heavy(n):
    res = 0.0
    for i in range(n):
        res += math.sqrt(math.exp(math.sin(i)))
    return res

def rust_heavy(n):
    return fastmath.heavy_computation(n)

def go_heavy(n):
    proc = subprocess.Popen(["./calculator"], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    input_data = json.dumps({"n": n})
    output, _ = proc.communicate(input_data.encode())
    return json.loads(output)["result"]

def test_python(benchmark):
    benchmark(python_heavy, N)

def test_rust(benchmark):
    benchmark(rust_heavy, N)

def test_go(benchmark):
    benchmark(go_heavy, N)