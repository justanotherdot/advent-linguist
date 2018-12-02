use std::collections::{BTreeSet};

#[derive(Debug)]
enum OpTy {
    Add,
    Subtract,
    Unknown,
}

pub fn day_01_pt_01(input: &String) -> isize {
    input.lines().into_iter()
        .map(parse_lines)
        .fold(0, |acc, (op, num)| run_op(op, acc, num))
}

pub fn day_01_pt_02(input: &String) -> (isize, bool) {
    let mut seen_set = BTreeSet::new();
    let mut acc = 0;

    // could probably just use a scan here.
    for (op, num) in input.lines().into_iter().cycle().map(parse_lines) {
        let rv = match op {
            OpTy::Add => {
                acc += num;
                acc
            },
            OpTy::Subtract => {
                acc -= num;
                acc
            }
            OpTy::Unknown =>
                acc
        };

        match seen_set.insert(rv) {
            false => {
                return (rv, true);
            },
            true => ()
        }
    }
    (0, false)
}

fn run_op(op: OpTy, lhs: isize, rhs: isize) -> isize {
    match op {
        OpTy::Add =>
            lhs + rhs,
        OpTy::Subtract =>
            lhs - rhs,
        OpTy::Unknown =>
            lhs,
    }
}

fn parse_lines(line: &str) -> (OpTy, isize) {
    let op = parse_op(line.chars().take(1).collect::<String>());
    let num = line.chars().skip(1).collect::<String>()
        .parse()
        .unwrap_or(0);
    (op, num)
}

fn parse_op(op_str: String) -> OpTy {
    match op_str.as_ref() {
        "+" =>
            OpTy::Add,
        "-" =>
            OpTy::Subtract,
        _ =>
            OpTy::Unknown
    }
}
