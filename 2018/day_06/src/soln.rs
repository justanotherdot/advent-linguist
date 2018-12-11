extern crate regex;

use self::regex::Regex;
use std::collections::HashMap;
use std::error::Error;
use std::result;
use std::str::FromStr;

type Result<T> = result::Result<T, Box<Error>>;
type Bounds = ((isize, isize), (isize, isize));

#[derive(Debug, PartialEq)]
struct Coord {
    x: isize,
    y: isize,
}

#[derive(Debug, PartialEq)]
enum Closest {
    Tie,
    Landmark(usize),
}

pub fn day06(s: &str) -> usize {
    let coords: Vec<Coord> = s.lines().map(|c| c.parse::<Coord>().unwrap()).collect();
    let bounds = find_bounds(&coords);
    let landmarks: Vec<(usize, &Coord)> = coords
        .iter()
        .enumerate()
        .filter(|(_, c)| c.within_bounds(bounds))
        .collect();

    // A bounding box of four elements.
    //   i.e. a plane has four corners on the cartesian plane.
    //   All 'landmarks' will be within that plane.
    assert_eq!(landmarks.len(), coords.len() - 4);

    let mut markers: Vec<(Coord, Closest)> = vec![];
    for y in (bounds.1).0 + 1..(bounds.1).1 {
        for x in (bounds.0).0 + 1..(bounds.0).1 {
            let coord = Coord { x, y };
            let closest = coord.closest(&landmarks);
            if let Closest::Landmark(_) = closest {
                markers.push((coord, closest));
            }
        }
    }

    let mut freqs: HashMap<usize, usize> = HashMap::new();
    for (_, closest) in markers {
        if let Closest::Landmark(loc) = closest {
            *freqs.entry(loc).or_default() += 1;
        }
    }

    *freqs.values().max().unwrap()
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

    fn closest(&self, landmarks: &Vec<(usize, &Coord)>) -> Closest {
        let (closest, _) = landmarks.iter().fold(
            (Closest::Tie, std::isize::MAX),
            |(closest_id, closest_distance), (id, loc)| {
                let new_distance = self.distance(loc);
                if new_distance < closest_distance {
                    (Closest::Landmark(*id), new_distance)
                } else if new_distance == closest_distance {
                    (Closest::Tie, closest_distance)
                } else {
                    (closest_id, closest_distance)
                }
            },
        );
        closest
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

#[cfg(test)]
mod test {
    use super::*;

    #[test]
    fn a_landmark_is_always_closest_to_itself() {
        assert_eq!(
            Coord { x: 0, y: 0 }.closest(&vec![
                (1, &Coord { x: 12, y: 3 }),
                (0, &Coord { x: 0, y: 0 }),
                (2, &Coord { x: 1, y: 0 }),
            ]),
            Closest::Landmark(0),
        );
    }

    #[test]
    fn a_landmark_is_a_tie_if_equidistant_between_landmarks() {
        assert_eq!(
            Coord { x: 0, y: 0 }.closest(&vec![
                (0, &Coord { x: 2, y: 2 }),
                (1, &Coord { x: 2, y: 2 }),
            ]),
            Closest::Tie,
        );
    }
}
