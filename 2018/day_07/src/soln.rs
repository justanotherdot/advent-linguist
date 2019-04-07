extern crate regex;

use self::regex::Regex;
//use std::collections::HashMap;
use std::error::Error;
use std::result;
use std::str::FromStr;

type Result<T> = result::Result<T, Box<Error>>;

#[derive(Debug)]
struct Edge {
    a: String,
    b: String,
}

pub fn day07(s: &str) {
    for l in s.lines() {
        let e = l.parse::<Edge>();
        println!("{:?}", e);
    }
}

impl FromStr for Edge {
    type Err = Box<Error>;

    // Could definitely be written sans unwraps
    fn from_str(s: &str) -> Result<Edge> {
        let re = Regex::new(r"Step (?P<a>[A-Z])[a-z ]+(?P<b>[A-Z])")?;
        let caps = re.captures(s).unwrap();
        let a = caps["a"].parse().unwrap();
        let b = caps["b"].parse().unwrap();
        Ok(Edge { a, b })
    }
}

#[cfg(test)]
mod test {
    use super::*;

    #[test]
    fn two_equals_two() {
        assert_eq!(2, 2);
    }
}
