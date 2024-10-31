#ifndef VEC2
#define VEC2

#include <cmath>
#include <iostream>

#include "constants.h"

class Vec2 {
private:
  float _x;
  float _y;

public:
  Vec2(float x, float y) : _x(x), _y(y) {}

  inline float x() const { return _x; }

  inline float y() const { return _y; }

  Vec2 &operator+=(Vec2 const &other) {
    this->_x += other.x();
    this->_y += other.y();
    return *this;
  }
};

bool operator==(Vec2 const &a, Vec2 const &b) {
  return abs(a.x() - b.x()) < EPSILON && abs(a.y() - b.y()) < EPSILON;
}

Vec2 operator-(Vec2 const &a, Vec2 const &b) {
  return Vec2(a.x() - b.x(), a.y() - b.y());
}

std::ostream &operator<<(std::ostream &os, Vec2 const &v) {
  return os << "Vec2: " << v.x() << ',' << v.y();
}

Vec2 rotate(Vec2 in, float rad) {
  float c = cos(rad);
  float s = sin(rad);
  return Vec2(in.x() * c - in.y() * s, in.x() * s + in.y() * c);
}

#endif  // VEC2