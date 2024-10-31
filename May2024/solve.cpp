#include <fstream>
#include <functional>
#include <iostream>
#include <set>
#include <string>
#include <vector>

typedef long long ll;
typedef std::function<bool(ll)> Validator;

const ll N = 11;
const ll SHADED = -999;
const ll UNSET = -1;

ll boxes[N][N];
ll state[N][N];
// std::vector<int> row_order = {7, 8, 9, 10, 6, 5, 4, 3};
std::vector<int> row_order = {0, 1, 2, 3};
ll iteration = 0;
std::set<ll> success;

bool is_palindrome(ll x) {
  std::vector<ll> d;
  while (x > 0) {
    d.push_back(x % 10);
    x /= 10;
  }
  ll l = 0, h = d.size() - 1;
  while (l < h) {
    if (d[l] != d[h]) {
      return false;
    }
    l++, h--;
  }
  return true;
}

std::vector<ll> prime_factors(ll x) {
  std::vector<ll> pf;
  for (ll i = 2; i <= x; ++i)
    while (x % i == 0) {
      pf.push_back(i);
      x /= i;
    }
  return pf;
}

bool is_prime(ll x) {
  if (x < 2) {
    return false;
  }
  for (ll i = 2; i * i <= x; ++i) {
    if (x % i == 0) {
      return false;
    }
  }
  return true;
}

Validator validators[N] = {
    // square
    [](ll x) {
      ll a = 1;
      while (a * a < x) {
        a++;
      }
      return a * a == x;
    },
    // 1 more than a palindrome
    [](ll x) { return is_palindrome(x - 1); },
    // prime raised to a prime power
    [](ll x) {
      auto pf = prime_factors(x);
      if (!is_prime(pf[0])) {
        return false;
      }
      for (auto p : pf) {
        if (p != pf[0]) {
          return false;
        }
      }
      return is_prime(pf.size());
    },
    // sum of digits is 7
    [](ll x) {
      ll d = 0;
      while (x > 0) {
        d += x % 10;
        x /= 10;
      }
      return d == 7;
    },
    // fibonacci
    [](ll x) {
      ll a = 1, b = 1;
      while (b < x) {
        b = a + b;
        a = b - a;
      }
      return x == b;
    },
    // square
    [](ll x) {
      ll a = 1;
      while (a * a < x) {
        a++;
      }
      return a * a == x;
    },
    // multiple of 37
    [](ll x) { return x % 37 == 0; },
    // palindrome multiple of 23
    [](ll x) { return is_palindrome(x) && (x % 23 == 0); },
    // product of digits end in 1
    [](ll x) {
      ll p = 1;
      while (x > 0) {
        p *= x % 10;
        x /= 10;
      }
      return p % 10 == 1;
    },
    // mulitple of 88
    [](ll x) { return x % 88 == 0; },
    // 1 less than a palindrome
    [](ll x) { return is_palindrome(x + 1); },
};

void init() {
  std::ifstream input("puzzle.grid", std::ifstream::in);
  for (ll i = 0; i < N; ++i) {
    std::string s;
    std::getline(input, s);
    for (ll j = 0; j < N; ++j) {
      boxes[i][j] = s[j] - '0';
    }
  }

  for (ll i = 0; i < N; ++i) {
    for (ll j = 0; j < N; ++j) {
      state[i][j] = -1;
    }
  }
}

void print() {
  for (ll i = 0; i < N; ++i) {
    for (ll j = 0; j < N; ++j) {
      if (state[i][j] == SHADED) {
        std::cout << "#";
      } else if (state[i][j] == UNSET) {
        std::cout << "?";
      } else {
        std::cout << state[i][j];
      }
    }
    std::cout << std::endl;
  }
  std::cout << std::endl;
}

bool inline is_shaded(ll i, ll j) {
  return 0 <= i && i < N && 0 <= j && j < N && state[i][j] == SHADED;
}

bool has_common(std::set<ll> &a, std::set<ll> &b) {
  for (ll x : a) {
    if (b.find(x) != b.end()) {
      return true;
    }
  }
  return false;
}

void add_number_constralls(ll i, ll j, ll di, ll dj, std::set<ll> &must_be,
                           std::set<ll> &must_not_be) {
  ll ni = i + di;
  ll nj = j + dj;
  if (!(0 <= ni && ni < N && 0 <= nj && nj < N)) {
    return;
  }

  if (state[ni][nj] < 0) {
    return;
  }

  if (boxes[ni][nj] != boxes[i][j]) {
    must_not_be.insert(state[ni][nj]);
  }

  if (boxes[ni][nj] == boxes[i][j]) {
    must_be.insert(state[ni][nj]);
  }
}

bool is_digit(ll x) { return 0 <= x && x <= 9; }

bool is_valid_number(ll i, ll j) {
  if (j < 0) {
    return true;
  }

  ll n = 0;
  ll digit = 1;
  while (j >= 0 && is_digit(state[i][j])) {
    n += state[i][j] * digit;
    digit *= 10;
    j -= 1;
  }

  if (n < 10) {
    return false;
  }

  return validators[i](n);
}

void search(ll ri, ll j) {
  if (ri >= row_order.size()) {
    std::cout << "success" << std::endl;
    print();
    return;
  }
  ll i = row_order[ri];

  //

  ///
  //   if (iteration++ % 100 == 0) {
  //     print();
  //   }
  ///

  std::set<ll> possible;
  if (!is_shaded(i - 1, j) && !is_shaded(i + 1, j) && !is_shaded(i, j - 1) &&
      !is_shaded(i, j + 1) && is_valid_number(i, j - 1)) {
    possible.insert(SHADED);
  }

  std::set<ll> must_be, must_not_be;
  add_number_constralls(i, j, -1, 0, must_be, must_not_be);
  add_number_constralls(i, j, 1, 0, must_be, must_not_be);
  add_number_constralls(i, j, 0, -1, must_be, must_not_be);
  add_number_constralls(i, j, 0, 1, must_be, must_not_be);
  if (has_common(must_be, must_not_be)) {
    return;
  }

  if (must_be.size() > 1) {
    return;
  }

  if (must_be.size() == 1) {
    possible.insert(*must_be.begin());
  } else {
    for (ll x = 0; x <= 9; ++x) {
      possible.insert(x);
    }
  }

  for (ll not_be : must_not_be) {
    possible.erase(not_be);
  }
  if (j == 0 || state[i][j - 1] == SHADED) {
    possible.erase(0);
  }

  ll ni = ri, nj = j + 1;
  if (nj >= N) {
    ni += 1;
    nj = 0;
  }

  for (ll p : possible) {
    state[i][j] = p;
    if (j == N - 1 && 0 <= p && p <= 9 && !is_valid_number(i, j)) {
      continue;
    }
    if (ni != ri) {
      success.insert(i);
    }
    search(ni, nj);
  }

  state[i][j] = UNSET;
}

int main() {
  init();
  search(0, 0);

  for (int s : success) {
    std::cout << s << ' ';
  }
}
