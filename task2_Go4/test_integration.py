import subprocess
import json
import os

GO_BINARY = "./main" if os.name != "nt" else "./main.exe"

def run_go_process(input_dict):
    process = subprocess.Popen(
        [GO_BINARY],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        encoding='utf-8'
    )
    stdout, stderr = process.communicate(input=json.dumps(input_dict))
    return stdout, stderr, process.returncode

def test_go_binary_exists():
    assert os.path.exists(GO_BINARY), f"Бинарный файл {GO_BINARY} не найден. Сначала выполните 'go build main.go'"

def test_successful_calculation():
    payload = {"name": "Ivan", "age": 20}
    stdout, stderr, returncode = run_go_process(payload)
    
    assert returncode == 0
    assert stderr == ""
    
    response = json.loads(stdout)
    assert "message" in response
    assert "Ivan" in response["message"]
    assert "30" in response["message"]  

def test_zero_age():
    payload = {"name": "Baby", "age": 0}
    stdout, _, _ = run_go_process(payload)
    
    response = json.loads(stdout)
    assert "10" in response["message"]

def test_invalid_json_input():
    process = subprocess.Popen(
        [GO_BINARY],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    stdout, stderr = process.communicate(input="not a json")
    assert process.returncode != 0
    assert "Error" in stderr