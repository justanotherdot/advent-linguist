extern crate regex;

use self::regex::Regex;
use std::error::Error;
use std::result;
use std::str::FromStr;

type Result<T> = result::Result<T, Box<Error>>;
type Bounds = ((isize, isize), (isize, isize));

#[derive(Debug)]
struct Coord {
    x: isize,
    y: isize,
}

pub fn day06(s: &str) {
    let coords: Vec<Coord> = s.lines().map(|c| c.parse::<Coord>().unwrap()).collect();
    let bounds = find_bounds(&coords);
    let finite_locs: Vec<&Coord> = coords.iter().filter(|c| c.within_bounds(bounds)).collect();

    println!("{}", coords[0].distance(&coords[1]));
    println!("{:?}", coords.len());
    println!("{:?}", finite_locs.len());

    // A bounding box of four elements.
    //   i.e. a plane has four corners on the cartesian plane.
    //   All 'finite_locs' will be within that plane.
    assert_eq!(finite_locs.len(), coords.len() - 4);
}

fn find_bounds(coords: &Vec<Coord>) -> ((isize, isize), (isize, isize)) {
    let min_max_tup = (std::isize::MAX, std::isize::MIN);
    coords.into_iter().fold(
        (min_max_tup, min_max_tup),
        |((min_x, max_x), (min_y, max_y)), coord| {
            (
                (isize::min(min_x, coord.x), isize::max(max_x, coord.x)),
                (isize::min(min_y, coord.y), isize::max(max_y, coord.y)),
            )
        },
    )
}

impl Coord {
    fn distance(&self, other: &Self) -> isize {
        (self.x - other.x).abs() + (self.y - other.y).abs()
    }

    fn within_bounds(&self, ((min_x, max_x), (min_y, max_y)): Bounds) -> bool {
        self.x > min_x && self.x < max_x && self.y > min_y && self.y < max_y
    }
}

impl FromStr for Coord {
    type Err = Box<Error>;

    // Could definitely be written sans unwraps
    fn from_str(s: &str) -> Result<Coord> {
        let re = Regex::new(r"(?P<x>\d+), (?P<y>\d+)")?;
        let caps = re.captures(s).unwrap();
        let x = caps["x"].parse().unwrap();
        let y = caps["y"].parse().unwrap();
        Ok(Coord { x, y })
    }
}
