mod internal;
use internal::day_01_pt_01;
use std::io::prelude::*;
use std::fs::File;
use std::env::{args};

fn main() -> std::io::Result<()> {
    let input_file : String = args().skip(1).take(1).collect();
    let mut f = File::open(input_file)?;
    let mut pt_01_input_buffer = String::new();
    f.read_to_string(&mut pt_01_input_buffer)?;

    println!("answer (pt. 01): {}", day_01_pt_01(&pt_01_input_buffer));

    Ok(())
}
