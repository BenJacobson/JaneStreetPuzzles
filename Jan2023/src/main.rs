use rand::Rng;
use std::cmp::max;
use std::collections::HashSet;

type State = (i32, i32, i32, i32);

trait Sum {
    fn sum(&self) -> i32;
}

impl Sum for State {
    fn sum(&self) -> i32 {
        self.0 + self.1 + self.2 + self.3
    }
}

trait Mult {
    fn mult(&self, m: i32) -> Self;
}

impl Mult for State {
    fn mult(&self, m: i32) -> Self {
        (self.0 * m, self.1 * m, self.2 * m, self.3 * m)
    }
}

trait Highest {
    fn highest(&self) -> i32;
}

impl Highest for State {
    fn highest(&self) -> i32 {
        max(max(self.0, self.1), max(self.2, self.3))
    }
}

trait Limit {
    fn is_in_limit(&self, limit: i32) -> bool;
}

impl Limit for State {
    fn is_in_limit(&self, limit: i32) -> bool {
        self.0 <= limit && self.1 <= limit && self.2 <= limit && self.3 <= limit
    }
}

trait Rot {
    fn rot(&self, i: i32) -> Self;
}

impl Rot for State {
    fn rot(&self, i: i32) -> Self {
        let mut a = vec![self.0, self.1, self.2, self.3];
        a.rotate_left((i as usize) % 4);
        (a[0], a[1], a[2], a[3])
    }
}

trait Add {
    fn add(&self, a: i32) -> Self;
}

impl Add for State {
    fn add(&self, a: i32) -> Self {
        let mut s = self.clone();
        s.0 += a;
        s.1 += a;
        s.2 += a;
        s.3 += a;

        s
    }
}

trait Pos {
    fn is_pos(&self) -> bool;
}

impl Pos for State {
    fn is_pos(&self) -> bool {
        self.0 >= 0 && self.1 >= 0 && self.2 >= 0 && self.3 >= 0
    }
}

fn fgcd(first: i32, second: &i32) -> i32 {
    let mut max = first;
    let mut min = *second;
    if min > max {
        let val = max;
        max = min;
        min = val;
    }

    if min == 0 || max == 0 {
        return match max {
            0 => 1,
            _ => max,
        };
    }

    loop {
        let res = max % min;
        if res == 0 {
            return min;
        }

        max = min;
        min = res;
    }
}

fn gcd_reduce(mut s: State) -> State {
    let gcd = vec![s.0, s.1, s.2, s.3].iter().fold(s.3, fgcd);
    s.0 /= gcd;
    s.1 /= gcd;
    s.2 /= gcd;
    s.3 /= gcd;

    s
}

fn shift_reduce(mut s: State) -> State {
    let m = *vec![s.0, s.1, s.2, s.3].iter().min().unwrap();
    s.0 -= m;
    s.1 -= m;
    s.2 -= m;
    s.3 -= m;

    s
}

fn rotate_reduce(s: State) -> State {
    let a = vec![
        (s.0, s.1, s.2, s.3),
        (s.1, s.2, s.3, s.0),
        (s.2, s.3, s.0, s.1),
        (s.3, s.0, s.1, s.2),
    ];
    *a.iter().min().unwrap()
}

fn make_canonical(mut s: State) -> State {
    loop {
        let before = s;
        s = gcd_reduce(s);
        s = shift_reduce(s);
        if before == s {
            break;
        }
    }
    rotate_reduce(s)
}

fn print_state(s: &State, i: i32) {
    println!(
        "{: <30} {: <10} {:?}",
        format!("{:?}", s),
        i,
        make_canonical(*s)
    );
}

fn print_state_factorization(s: State) {
    // println!(
    //     "{:?}, {:?}, {:?}, {:?}",
    //     prime_factorization(s.0),
    //     prime_factorization(s.1),
    //     prime_factorization(s.2),
    //     prime_factorization(s.3)
    // );
}

fn reduce(mut s: State, debug: bool) -> i32 {
    let mut i = 1;
    while s != (0, 0, 0, 0) {
        s = make_canonical(s);
        if debug {
            print_state(&s, i);
            print_state_factorization(s);
        }
        let a = (s.0 - s.1).abs();
        let b = (s.1 - s.2).abs();
        let c = (s.2 - s.3).abs();
        let d = (s.3 - s.0).abs();
        s = (a, b, c, d);

        i += 1;
    }
    if debug {
        print_state(&s, i);
    }

    i
}

fn random_state(primes: &Vec<i32>) -> State {
    let mut rng = rand::thread_rng();
    (
        primes[rng.gen_range(0..primes.len())],
        primes[rng.gen_range(0..primes.len())],
        primes[rng.gen_range(0..primes.len())],
        primes[rng.gen_range(0..primes.len())],
    )
}

fn prime_factorization(mut n: i32) -> Vec<i32> {
    let mut ans = Vec::new();
    let mut i = 2;
    while i * i <= n {
        while n % i == 0 {
            ans.push(i);
            n /= i;
        }
        i += 1;
    }

    if n > 1 {
        ans.push(n);
    }

    ans
}

fn brute_force(limit: i32) {
    let mut iterations: Vec<HashSet<State>> = Vec::new();
    let mut steps = 0;
    for a in 0..=limit {
        for b in 0..=limit {
            for c in 0..=limit {
                for d in 0..=limit {
                    steps += 1;
                    let mut state = (a, b, c, d);
                    state = make_canonical(state);
                    let iters = reduce(state, false) as usize;
                    while iterations.len() < iters+1 {
                        iterations.push(HashSet::new());
                    }
                    iterations[iters].insert(state);
                }
            }
        }
    }

    println!("steps: {}", steps);
    for (i, h) in iterations.iter().enumerate() {
        println!("iteration: {}, options: {}, min: {:?}", i, h.len(), h.iter().min_by_key(|s| (s.sum(), *s)));

    }
}

fn main() {
    // let high = 10001; // 10_000_001;
    // let mut sieve: Vec<bool> = vec![true; high];
    // let mut primes: Vec<i32> = Vec::new();
    // for i in 2..sieve.len() {
    //     if !sieve[i] {
    //         continue;
    //     }
    //     primes.push(i as i32);
    //     for j in ((2 * i)..sieve.len()).step_by(i) {
    //         sieve[j] = false;
    //     }
    // }
    // println!("{}", primes.len());

    // for _ in 0..1000 {
    //     let state = random_state(&primes);
    //     let expect = reduce(state);
    //     for _ in 0..1000 {
    //         let mut rng = rand::thread_rng();
    //         let add = rng.gen_range(0..1_000_000);
    //         let result = reduce(gcd_reduce(shift_reduce(gcd_reduce((
    //             state.0 + add,
    //             state.1 + add,
    //             state.2 + add,
    //             state.3 + add,
    //         )))));
    //         if result != expect {
    //             println!("Failed at state: {:?}, add: {}", state, add);
    //         }
    //     }
    // }

    // let mut best = 0;
    // for i in 0..primes.len() {
    //     for j in (i+1)..primes.len() {
    //         for k in (j+1)..primes.len() {
    //             let iters = reduce((0, primes[i], primes[j], primes[k]));
    //             best = max(best, iters);

    //             if iters == 22 {
    //                 println!("{:?}", (0, primes[i], primes[j], primes[k]));
    //             }
    //         }
    //     }
    // }

    // println!("{}", best);

    let limit = 50;

    brute_force(limit);

    let mut steps = 0;
    let start: State = (1, 1, 1, 1);
    let mut current = HashSet::new();
    current.insert(start);
    let mut iterations = 2;
    loop {
        println!("iteration: {}, options: {}, min: {:?}, min: {:?}", iterations, current.len(), current.iter().min(), current.iter().min_by_key(|s| (s.sum(), *s)));
        // println!("{:?}", current);
        let mut next = HashSet::new();
        for c in current.iter() {
            let ex = *c;
            let mult = limit / ex.highest();
            for m in 1..=mult {
                let ex = ex.mult(m);
                let highest = limit - ex.highest();
                for base in 0..=highest {
                    let ex = ex.add(base);
                    for rot in 0..4 {
                        let ex = ex.rot(rot);
                        for i in 0..4 {
                            let mut new = (0, 0, 0, 0);
                            new.0 = 0;
                            new.1 = ex.0;
                            new.2 = if i & 1 > 0 {
                                new.1 + ex.1
                            } else {
                                new.1 - ex.1
                            };
                            new.3 = if i & 2 > 0 {
                                new.2 + ex.2
                            } else {
                                new.2 - ex.2
                            };

                            // println!("Try {:?} -> {:?}", ex, new);

                            steps += 1;
                            if new.is_pos()
                                && new.is_in_limit(limit)
                                && (new.3 - new.0).abs() == ex.3
                                && reduce(new, false) == iterations + 1
                            {
                                // println!("yes {:?}", make_canonical(new));
                                next.insert(make_canonical(new));
                            } else {
                                // println!("no {:?}", make_canonical(new));
                            }
                        }
                    }
                }
            }
        }

        current = next;
        iterations += 1;

        if current.is_empty() {
            break;
        }
    }
    println!("steps: {}", steps);

    // println!("{:?}", make_canonical((4547, 2472, 1344, 8363)));
    // reduce((0, 4547, 7019, 8363), true);
    // println!("{}", reduce((0, 6, 1, 5), false));
}

/*
I can shift or gcd a state without changing the iterations to 0.
*/

/*
(0, 4547, 7019, 8363)
yields 22
*/
