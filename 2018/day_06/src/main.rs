mod soln;

use soln::day06;

fn main() {
    let input = include_str!("../input/puzzle.in");
    let (pt01, pt02) = day06(input.trim());
    println!("pt01: {}", pt01);
    println!("pt02: {}", pt02);
}
