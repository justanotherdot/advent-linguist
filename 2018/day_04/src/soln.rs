extern crate regex;

use self::regex::Regex;

pub fn day_04(s: String) {
    let mut v = vec![];
    for line in s.lines() {
        v.push(parse_line(line));
    }
    v.sort();
    println!("{:?}", v);
}

fn parse_line(s: &str) -> String {
    let re = Regex::new(
        r"\[(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2}) (?P<hour>\d{2}):(?P<minute>\d{2})\]"
    ).unwrap();
    let caps = re.captures(s).unwrap();
    //println!("{:?}", caps);
    let iso8601 = format!(
        "{}-{:02}-{:02}T{:02}:{:02}:00Z",
        &caps["year"],
        &caps["month"],
        &caps["day"],
        &caps["hour"],
        &caps["minute"],
    );
    //println!("{}", iso8601);
    iso8601
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
