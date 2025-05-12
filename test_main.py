from main import hello

def test_hello():
    assert hello() == "Hello, GitHub Actions!"
    
def test_hello_custom_name ( ):
    
    assert hello ("EPSI") == "Hello, EPSI!"
