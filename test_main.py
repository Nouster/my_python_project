import pytest
import time
from main import hello

def test_hello():
    assert hello() == "Hello, GitHub Actions!"

def test_hello_custom_name():
    assert hello("EPSI") == "Hello, EPSI!"

def test_hello_chaine_invalide():
    with pytest.raises(TypeError):
        hello(7878567)

def test_hello_performance():
  start = time.time()
  for _ in range(1000):
    hello("EPSI")
  duration = time.time() - start
  assert duration < 1
  
def test_hello_full_name():
    assert hello("Jane", "Smith") == "Hello, Jane Smith!"