mod internal;
use std::io::prelude::*;
use std::fs::File;
use std::env::{args};

fn main() -> std::io::Result<()> {
    let filename_pt01 : String = args().skip(1).take(1).collect();
    let ref pt_01_input_buffer = input_buffer(filename_pt01)?;

    println!("{:?}", internal::day02_pt01(pt_01_input_buffer));
    println!("{}", internal::day02_pt02(pt_01_input_buffer));

    Ok(())
}

fn input_buffer(filename: String) -> std::io::Result<String> {
    let mut f = File::open(filename)?;
    let mut input_buf = String::new();
    f.read_to_string(&mut input_buf)?;

    Ok(input_buf)
}
