pub fn day05_pt01(input: &String) -> String {

    let r = react_fold(input);

    format!("{}", r.len())
}

fn react_fold(input: &String) -> String {
    // The idea behind how this works is:
    //   1. Add stuff to your new empty string bit by bit
    //   2. if adding that new stuff doesn't make sense, don't include it
    //      (and in fact prune it from the string you've been adding to)
    let s = input.trim().chars()
        .fold("".to_string(), |acc, x| {
            if acc.len() > 0 {
                let dupe = acc.clone();
                let (y, ys) = dupe.split_at(1);
                let p = y.to_ascii_lowercase();
                let q = x.to_string().to_ascii_lowercase();
                if p == q && x.to_string() != y {
                    format!("{}", ys)
                } else {
                    format!("{}{}", x, acc)
                }
            } else {
                format!("{}{}", x, acc)
            }
        });
    // there is no foldr in rust, so we reverse the string
    s.chars().rev().collect::<String>()
}

//fn react_stack(input: &String) -> String {
    // Stack/Vector style.
    //let mut v = Vec::new();
    //for c1 in input.trim().chars() {
        //match v.last() {
            //None =>
                //v.push(c1),
            //Some(&c2) => {
                //let p = c1.to_lowercase().to_string();
                //let q = c2.to_lowercase().to_string();
                //if p == q && c1 != c2 {
                    //v.pop();
                //} else {
                    //v.push(c1);
                //}
            //}
        //}
    //}
//}

pub fn day05_pt02(input: &String) -> usize {
    "abcdefghijklmnopqrstuvwxyz".chars()
        .fold(std::usize::MAX, |min, c1| {
            let reduced_input: String =
                input.chars().into_iter()
                .filter(|c2| !(c2.to_lowercase().to_string() == c1.to_string()))
                .collect();
            let s = react_fold(&reduced_input);
            usize::min(min, s.len())
        })
}
