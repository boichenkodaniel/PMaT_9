use pyo3::prelude::*;

#[pyfunction]
fn heavy_computation(n: i64) -> f64 {
    let mut res: f64 = 0.0;
    for i in 0..n {
        res += (i as f64).sin().exp().sqrt();
    }
    res
}

#[pymodule]
fn fastmath(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(heavy_computation, m)?)?;
    Ok(())
}