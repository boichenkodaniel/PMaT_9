use pyo3::prelude::*;

#[pyfunction]
fn resize_logic(data: Vec<u8>, width: usize, height: usize, new_width: usize, new_height: usize) -> PyResult<Vec<u8>> {
    let mut resized = Vec::with_capacity(new_width * new_height * 4);
    
    let x_ratio = width as f32 / new_width as f32;
    let y_ratio = height as f32 / new_height as f32;

    for y in 0..new_height {
        for x in 0..new_width {
            let px = (x as f32 * x_ratio) as usize;
            let py = (y as f32 * y_ratio) as usize;
            
            let index = (py * width + px) * 4;
            
            if index + 3 < data.len() {
                resized.extend_from_slice(&data[index..index + 4]);
            }
        }
    }

    Ok(resized)
}

#[pymodule]
fn resize_image(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(resize_logic, m)?)?;
    Ok(())
}