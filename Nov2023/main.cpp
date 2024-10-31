#include <functional>
#include <iostream>
#include <set>
#include <utility>
#include <vector>

const int N = 8;
const int BOARD[N][N] = {
    {0, 2, 4, 3, 5, 6, 2, 4},      {1, 2, 0, 1, 2, 5, 7, 6},
    {0, 3, 1, 4, 2, 7, 10, 7},     {2, 6, 4, 2, 5, 9, 8, 11},
    {4, 10, 7, 9, 6, 8, 7, 9},     {4, 7, 5, 8, 8, 6, 13, 10},
    {7, 9, 11, 9, 10, 12, 14, 12}, {9, 8, 10, 12, 11, 8, 10, 17},
};

const int MOVES[][3] = {
    {0, 1, 2}, {1, 0, 2}, {0, 2, 1}, {1, 2, 0}, {2, 0, 1}, {2, 1, 0},
};

typedef std::function<void()> UndoFunction;

struct PathEntry {
  int i;
  int j;
  int wait;
};

class Seen {
public:
  void set(int i, int j) { bits |= 1 << (i * 8 + j); }

  void unset(int i, int j) { bits &= ~(1 << (i * 8 + j)); }

  bool is_set(int i, int j) { return (bits & (1 << (i * 8 + j))) > 0; }

private:
  long long int bits = 0;
};

class Board {
public:
  Board() {
    i = 0;
    j = 0;
    total_time = 0;
    memcpy(board, BOARD, sizeof BOARD);
    memset(count, 0, sizeof count);
    count[0][0]++;
    path.push_back({0, 0, 0});
  }

  int get_i() { return i; }

  int get_j() { return j; }

  std::vector<std::pair<int, int>> getJumps() {
    std::vector<std::pair<int, int>> jumps = {};

    for (const auto &move : MOVES) {
      if (!inBounds(i + move[0], j + move[1]))
        continue;

      if (count[i + move[0]][j + move[1]] >= 3)
        continue;

      if (abs(board[i][j] - board[i + move[0]][j + move[1]]) == move[2]) {
        jumps.push_back({i + move[0], j + move[1]});
      }
    }

    return jumps;
  }

  std::set<int> getWaits() {
    int cout_same_alt;
    for (int ii = 0; ii < N; ++ii) {
      for (int jj = 0; jj < N; ++jj) {
        if (board[ii][jj] == board[i][j]) {
          cout_same_alt++;
        }
      }
    }

    std::set<int> waits = {};

    for (const auto &move : MOVES) {
      if (!inBounds(i + move[0], j + move[1]))
        continue;

      int diff1 = board[i][j] - board[i + move[0]][j + move[1]] - move[2];
      if (diff1 > 0)
        waits.insert(diff1);

      int diff2 = board[i][j] - board[i + move[0]][j + move[1]] + move[2];
      if (diff2 > 0)
        waits.insert(diff2);
    }

    return waits;
  }

  UndoFunction jump(std::pair<int, int> ij) {
    int old_i = i;
    int old_j = j;
    int new_i = ij.first;
    int new_j = ij.second;

    i = new_i;
    j = new_j;
    count[new_i][new_j]++;
    path.push_back({new_i, new_j, 0});

    return [this, old_i, old_j, new_i, new_j]() {
      count[new_i][new_j]--;
      i = old_i;
      j = old_j;
      path.pop_back();
    };
  }

  UndoFunction wait(int w) {
    int op_i = N - 1 - i;
    int op_j = N - 1 - j;

    std::cout << "wait " << w << std::endl;

    std::vector<std::pair<int, int>> same_alt;
    for (int ii = 0; ii < N; ++ii) {
      for (int jj = 0; jj < N; ++jj) {
        if (board[ii][jj] == board[i][j]) {
          board[ii][jj] -= w;
          same_alt.push_back({ii, jj});
        }
      }
    }

    board[op_i][op_j] += w;
    total_time += w * same_alt.size();
    path.back().wait = w * same_alt.size();

    return [this, same_alt, op_i, op_j, w]() {
      for (const auto &p : same_alt) {
        board[p.first][p.second] += w;
      }
      board[op_i][op_j] -= w;
      total_time -= w * same_alt.size();
      path.back().wait = 0;
    };
  }

  bool isDone() { return i == N - 1 && j == N - 1; }

  void printPath() {
    for (const auto &p : path) {
      int n = 1 + p.i;
      char a = 'a' + p.j;
      std::cout << "(" << p.wait << ", " << a << n << "), ";
    }
    std::cout << std::endl;
  }

private:
  int i;
  int j;
  std::vector<PathEntry> path;
  int board[N][N];
  int count[N][N];
  int total_time;

  bool inBounds(int ii, int jj) {
    return ii >= 0 && jj >= 0 && ii < N && jj < N;
  }
};

void search(Board &board, Seen &seen) {
  if (board.isDone()) {
    board.printPath();
    return;
  } else {
    board.printPath();
  }

  for (auto &jump : board.getJumps()) {
    if (seen.is_set(jump.first, jump.second))
      continue;

    seen.set(jump.first, jump.second);
    auto undo = board.jump(jump);
    search(board, seen);
    seen.unset(jump.first, jump.second);
    undo();
  }

  Seen new_seen;
  new_seen.set(board.get_i(), board.get_j());
  for (auto &wait : board.getWaits()) {
    auto undo = board.wait(wait);
    search(board, new_seen);
    undo();
  }
}

int main() {
  std::cout << "begin search" << std::endl;

  Board board;
  Seen seen;
  seen.set(board.get_i(), board.get_j());

  search(board, seen);

  std::cout << "completed search" << std::endl;
}
