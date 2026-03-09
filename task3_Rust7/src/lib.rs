use pyo3::prelude::*;

#[pyfunction]
fn greet(name: String) -> PyResult<String> {
    Ok(format!("Привет из Rust, {}!", name))
}

#[pymodule]
fn rust_module(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(greet, m)?)?;
    Ok(())
}