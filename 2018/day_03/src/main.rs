mod internal;
use std::io::prelude::*;
use std::fs::File;
use std::env::{args};

fn main() -> std::io::Result<()> {
    let filename_pt01 : String = args().skip(1).take(1).collect();
    let pt_01_input_buffer = input_buffer(filename_pt01)?;

    let (a, b) = internal::day03(pt_01_input_buffer);
    println!("day03, pt01 answer: {:?}", a);
    println!("day03, pt02 answer: {:?}", b);

    Ok(())
}

fn input_buffer(filename: String) -> std::io::Result<String> {
    let mut f = File::open(filename)?;
    let mut input_buf = String::new();
    f.read_to_string(&mut input_buf)?;

    Ok(input_buf)
}
