mod soln;

use std::io::prelude::*;
use std::fs::File;
use std::env::{args};
use soln::{
    day05
};

fn main() -> std::io::Result<()> {
    let filename : String = args().skip(1).take(1).collect();
    let input_buffer = input_buffer(filename)?;

    day05(input_buffer);

    Ok(())
}

fn input_buffer(filename: String) -> std::io::Result<String> {
    let mut f = File::open(filename)?;
    let mut input_buf = String::new();
    f.read_to_string(&mut input_buf)?;

    Ok(input_buf)
}
