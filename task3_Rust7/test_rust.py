import rust_module

def test_greet_basic():
    result = rust_module.greet("Rust")
    assert result == "Привет из Rust, Rust!"

def test_greet_empty():
    result = rust_module.greet("")
    assert result == "Привет из Rust, !"

def test_greet_unicode():
    result = rust_module.greet("🦀")
    assert "🦀" in result

