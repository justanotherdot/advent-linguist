use std::collections::BTreeMap;

pub fn day02_pt01(raw_input: &String) -> i64 {
    let mut twos_count = 0;
    let mut threes_count = 0;
    for line in raw_input.lines() {
        let char_freqs = frequency(line);
        if has_exact_count(2, &char_freqs) {
            twos_count += 1;
        }
        if has_exact_count(3, &char_freqs) {
            threes_count += 1;
        }
    }
    twos_count * threes_count
}

pub fn day02_pt02(raw_input: &String) -> String {
    let s = String::new();
    for id1 in raw_input.lines() {
        for id2 in raw_input.lines() {
            if id1 == id2 {
                continue;
            }

            let count = id1.chars().zip(id2.chars())
                .filter(|(c1, c2)| c1 != c2)
                .count();

            if count == 1 {
                // exit early since we don't need to process anything else.
                return id1.chars().zip(id2.chars())
                    .filter(|(c1, c2)| c1 == c2)
                    .map(|(c, _)| c)
                    .collect();
            }
        }
    }
    s
}

pub fn frequency(s: &str) -> BTreeMap<char, i64> {
    let mut char_counts : BTreeMap<char, i64> = BTreeMap::new();
    for ref c in s.chars() {
        let v = char_counts.entry(*c).or_insert(0);
        *v += 1;
    }
    char_counts
}

pub fn has_exact_count(n: i64, freq: &BTreeMap<char, i64>) -> bool {
    freq.into_iter().filter(|(_c, count)| **count == n).count() > 0
}

#[cfg(test)]
mod test {
    use super::{
        frequency,
        has_exact_count,
    };

    #[test]
    fn frequency_works() {
        assert_eq!(frequency("bandana"),
                   vec![
                    ('d', 1),
                    ('a', 3),
                    ('b', 1),
                    ('n', 2),
                   ].into_iter().collect());
    }

    #[test]
    fn str_has_exactly_works_01() {
        assert_eq!(has_exact_count(2, &frequency("hello")), true);
    }

    #[test]
    fn str_has_exactly_works_02() {
        assert_eq!(has_exact_count(3, &frequency("abbba")), true);
    }

    #[test]
    fn str_has_exactly_works_03() {
        assert_eq!(has_exact_count(3, &frequency("a")), false);
    }

    #[test]
    fn str_has_exactly_works_04() {
        assert_eq!(has_exact_count(3, &frequency("")), false);
    }

    #[test]
    fn str_has_exactly_works_05() {
        assert_eq!(has_exact_count(3, &frequency("helllooo")), true);
    }
}
