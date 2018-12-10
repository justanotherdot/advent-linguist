mod soln;

use soln::{
    day06
};

fn main() {
    let input = include_str!("../input/puzzle.in");
    day06(input.trim());
}
