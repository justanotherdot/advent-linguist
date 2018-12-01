#[derive(Debug)]
enum OpTy {
    Add,
    Subtract,
    Unknown,
}

pub fn day_01_pt_01(input: &String) -> isize {
    input.lines().into_iter()
        .map(parse_lines)
        .inspect(|val| println!("{:?}", val))
        .fold(0, |acc, (op, num)| {
            match op {
                OpTy::Add =>
                    acc + num,
                OpTy::Subtract =>
                    acc - num,
                OpTy::Unknown =>
                    acc,
            }
        })
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
