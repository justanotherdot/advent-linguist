mod internal;
use std::io::prelude::*;
use std::fs::File;
use std::env::{args};

// Create a multidimensional vector to supposer x,y styled indexing
// at each coordinate x,y for the range of given coordinates
//   i.e. x+i+o for i=0..l where l is the given length and o is the offset from the left edge of
//   the grid. similarly for y but with offset from the top edge and width
// we can do grid[x][y] there lives a hash where we will insert the id of this pattern
// i.e. grid[x][y].insert(id) =

fn main() {
    let filename_pt01 : String = args().skip(1).take(1).collect();
    let pt_01_input_buffer = input_buffer(filename_pt01)?;

    for line in pt_01_input_buffer.lines() {
        internal::parse_line(line);
    }

    println!("Hello, world!");
}

fn input_buffer(filename: String) -> std::io::Result<String> {
    let mut f = File::open(filename)?;
    let mut input_buf = String::new();
    f.read_to_string(&mut input_buf)?;

    Ok(input_buf)
}
