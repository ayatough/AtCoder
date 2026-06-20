def main(num_str):
    min_nonzero_digit = 10
    for d in num_str:
        if d != "0":
            min_nonzero_digit = min(min_nonzero_digit, int(d))
    num_str_excluded = list(num_str)
    num_str_excluded.remove(str(min_nonzero_digit))
    ans_str = [str(min_nonzero_digit)] + list(sorted(num_str_excluded))
    print("".join(ans_str))


if __name__ == '__main__':
    num_str = input().strip()
    main(num_str)
