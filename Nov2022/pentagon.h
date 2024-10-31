#ifndef PENTAGON
#define PENTAGON

#include <assert.h>
#include <vector>

#include "vec2.h"

class Pentagon {
private:
  std::vector<Vec2> ps;
  float xMin, xMax, yMin, yMax;

public:
  Pentagon(Vec2 p, Vec2 v) {
    Vec2 start = p;
    for (int i = 0; i < 5; ++i) {
      ps.push_back(p);
      p += v;
      v = rotate(v, EXT_ANGLE);
    }
    assert(p == start);

    xMin = xMax = start.x();
    yMin = yMax = start.y();

    for (const auto &r : ps) {
      xMin = std::min(xMin, r.x());
      xMax = std::max(xMax, r.x());
      yMin = std::min(yMin, r.y());
      yMax = std::max(yMax, r.y());
    }
  }

  bool contains(Vec2 p) const {
    if (p.x() < xMin || p.x() > xMax || p.y() < yMin || p.y() > yMax) {
      return false;
    }

    int i, j, c = 0;
    for (i = 0, j = ps.size() - 1; i < ps.size(); j = i++) {
      if (((ps[i].y() > p.y()) != (ps[j].y() > p.y())) &&
          (p.x() <  (ps[j].x() - ps[i].x()) * (p.y() - ps[i].y()) /
                           (ps[j].y() - ps[i].y()) +
                       ps[i].x()))
        c = !c;
    }
    return c;
  }

  bool contains(const Pentagon &other) const {
    for (const auto &op : other.ps) {
        if (contains(op)) {
            return true;
        }
    }
    return false;
  }

  bool is_neighboor(const Pentagon &other) const {
    int same = 0;
    for (const auto &p1 : other.ps) {
        for (const auto &p2 : ps) {
            same += p1 == p2;
            if (same > 2) {
                return false;
            }
        }
    }
    return same == 2;
  }
};

#endif  // PENTAGON