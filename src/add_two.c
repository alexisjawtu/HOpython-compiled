/* file: add_two.c */
#include <stdlib.h>
#include "add_two.h"

float add_float(float a, float b) {
  return a + b;
}

int add_int(int a, int b) {
  return a + b;
}

int add_float_ref(float *a, float *b, float *c) {
  *c = *a + *b;
  return 0;
}

int add_int_ref(int *a, int *b, int *c) {
  *c = *a + *b;
  return 0;
}
