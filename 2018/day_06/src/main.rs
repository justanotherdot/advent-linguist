mod soln;

use soln::day06;

fn main() {
    let input = include_str!("../input/puzzle.in");
    println!("pt01: {}", day06(input.trim()));
}
