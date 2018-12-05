use std::collections::{HashMap, HashSet};

#[derive(Debug)]
pub struct Claim {
    id:   usize,
    w:    usize,
    h:    usize,
    top:  usize,
    left: usize,
}

type Grid = HashMap<(usize, usize), HashSet<usize>>;

pub fn day03(raw_input: String) -> (usize, usize) {
    let mut grid: Grid = HashMap::new();

    let mut claims = vec![];
    for line in raw_input.lines() {
        //println!("{}", line);
        match parse_line(line) {
            Ok(claim) => {
                //println!("  {:?}", claim);
                mark_claim_on_grid(&mut grid, &claim);
                claims.push(claim);
            },
            Err(err) =>
                println!("{}", err)
        }
    }
    let a = grid.iter().filter(|(_k, v)| v.len() > 1).count();
    let b = claims.iter()
        .filter_map(|c| find_uncontested_claim(&mut grid, c))
        .next().unwrap().id;
    (a, b)
}

fn mark_claim_on_grid(grid: &mut Grid, claim: &Claim) {
    let row_beg = claim.top;
    let row_end = claim.top+claim.h;
    let col_beg = claim.left;
    let col_end = claim.left+claim.w;
    for i in row_beg..row_end {
        for j in col_beg..col_end {
            grid.entry((i, j)).or_default().insert(claim.id);
        }
    }
}

fn find_uncontested_claim<'a>(grid: &mut Grid, claim: &'a Claim) -> Option<&'a Claim> {
    let row_beg = claim.top;
    let row_end = claim.top+claim.h;
    let col_beg = claim.left;
    let col_end = claim.left+claim.w;
    let mut is_uncontested = true;
    for i in row_beg..row_end {
        for j in col_beg..col_end {
            match grid.get(&(i, j)) {
                Some(claims) => {
                    if claims.len() > 1 {
                        is_uncontested = false;
                    }
                },
                None => {
                    panic!("provided `grid' is incomplete");
                },
            }
        }
    }

    if is_uncontested {
        Some(claim)
    } else {
        None
    }
}

pub fn parse_line(s : &str) -> Result<Claim, Box<std::error::Error>>  {
    let nums =
        s.split(|c:char| !c.is_digit(10))
            .filter(|x| x.len() > 0)
            .map(|s| s.parse::<usize>().unwrap())
            .collect::<Vec<_>>();

    let id   = nums[0];
    let left = nums[1];
    let top  = nums[2];
    let w    = nums[3];
    let h    = nums[4];

    Ok(Claim { id, w, h, top, left })
}
