extern crate regex;

use self::regex::Regex;

pub fn day_04(s: String) {
    for line in s.lines() {
        parse_line(line);
    }
}

fn parse_line(s: &str) {
    let re = Regex::new(
        r"\[(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2}) (?P<hour>\d{2}):(?P<minute>\d{2})\]"
    ).unwrap();
    let caps = re.captures(s).unwrap();
    println!("{:?}", caps);
}

#[cfg(test)]
mod test {
    use super::{
    };

    #[test]
    fn frequency_works() {
        assert_eq!(1, 1);
    }

}
