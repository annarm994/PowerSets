# Power Set Generator

This application takes a set as input from the user and generates the power set of the given set.

## How to Run

1. Clone the repository:
    ```bash
    git clone <repository_url>
    ```
2. Navigate to the project directory:
    ```bash
    cd power-set-generator
    ```
3. Run the application:
    ```bash
    python power_set_generator.py
    ```

## Test Cases

- Normal Cases:
  1. Input: `1 2 3` -> Output: `(), (1,), (2,), (3,), (1, 2), (1, 3), (2, 3), (1, 2, 3)`
  2. Input: `a b c` -> Output: `(), (a,), (b,), (c,), (a, b), (a, c), (b, c), (a, b, c)`
  3. Input: `x y` -> Output: `(), (x,), (y,), (x, y)`
- Edge Cases:
  1. Input: `1` -> Output: `(), (1,)`
  2. Input: ` ` -> Output: `()`
  3. Input: `1 1` -> Output: `(), (1,), (1,)`

