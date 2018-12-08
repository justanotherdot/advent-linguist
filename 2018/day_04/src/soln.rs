extern crate regex;
extern crate chrono;

use self::regex::Regex;
use self::chrono::prelude::*;
use std::collections::{HashMap};

#[derive(Debug)]
enum Action {
    Awake,
    Asleep,
    GuardOnDuty(isize),
}

#[derive(Debug)]
struct LogEntry {
    timestamp: String,
    action: Action,
}

pub fn day_04(s: String) {
    let mut v = vec![];
    for line in s.lines() {
        let log_entry = parse_line(line);
        v.push(log_entry);
    }
    v.sort_by_key(|x| x.timestamp.to_owned());

    let mut all_minutes: HashMap<(isize, u32), u32> = HashMap::new();

    let mut x = v.into_iter().fold(
        (-1, HashMap::new(), "".to_owned()),
        |mut acc: (isize, HashMap<isize, Vec<u32>>, String), log_entry: LogEntry| {
            //println!("{:?}", log_entry);
            match log_entry.action {
                Action::GuardOnDuty(id) => {
                    (id, acc.1, acc.2)
                },
                Action::Asleep => {
                    let id = acc.0;
                    let start_time = log_entry.timestamp;
                    (id, acc.1, start_time)
                },
                Action::Awake => {
                    // Get the intervals where someone has fallen asleep and is now awake
                    if acc.2 != "" {
                        let id = acc.0;
                        let start_time = acc.2.parse::<DateTime<Utc>>().unwrap();
                        let end_time = log_entry.timestamp.parse::<DateTime<Utc>>().unwrap();
                        for m in start_time.minute()..end_time.minute() {
                            acc.1.entry(id).or_default().push(m);
                            *all_minutes.entry((id, m)).or_insert(0) += 1;
                        }
                        return (acc.0, acc.1, "".to_owned());
                    }
                    acc
                },
            }
        }).1;

    let pair = x.iter_mut().max_by_key(|(_, v)| v.len()).unwrap();
    let id   = pair.0;
    let mins = pair.1;
    let most_mins = mins.iter()
        .fold(HashMap::new(),
              |mut acc: HashMap<u32, u32>, x| {
                  *acc.entry(*x).or_default() += 1; acc
              })
        .into_iter()
        .max_by(|(_, v1), (_, v2)| v1.cmp(v2)).unwrap().0 as isize;
    println!("pt01: {}", id * most_mins);

    println!("{:#?}", all_minutes);
    let rv = all_minutes.into_iter()
        .max_by(|(_, v1), (_, v2)| v1.cmp(&v2)).unwrap();
    println!("{:?}", rv);
    println!("pt02: {}", (rv.0).1 *  (rv.0).0 as u32);
    //println!("{:#?}", x);
}

fn parse_line(s: &str) -> LogEntry {
    let re = Regex::new(
        r"\[(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2}) (?P<hour>\d{2}):(?P<minute>\d{2})\] (?P<extra>.+)"
    ).unwrap();
    let caps = re.captures(s).unwrap();
    let timestamp = format!(
        "{}-{:02}-{:02}T{:02}:{:02}:00Z",
        &caps["year"],
        &caps["month"],
        &caps["day"],
        &caps["hour"],
        &caps["minute"],
    );

    let action = match &caps["extra"] {
        "wakes up" =>
            Action::Awake,
        "falls asleep" =>
            Action::Asleep,
        e => {
            let re = Regex::new(r"(?P<guardno>\d+)").unwrap();
            let matches = re.captures(e).unwrap();
            Action::GuardOnDuty(matches["guardno"].parse::<isize>().unwrap())
        },

    };

    LogEntry { timestamp, action }
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
