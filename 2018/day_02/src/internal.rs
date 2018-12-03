use std::collections::HashMap;

pub fn day01_pt01(raw_input: String) -> usize {
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
    // (twos_count, threes_count)
    twos_count * threes_count
}

pub fn frequency(s: &str) -> HashMap<char, usize> {
    let mut char_counts : HashMap<char, usize> = HashMap::new();
    for ref c in s.chars() {
        let v = char_counts.entry(*c).or_insert(0);
        *v += 1;
    }
    char_counts
}

pub fn has_exact_count(n: usize, freq: &HashMap<char, usize>) -> bool {
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
