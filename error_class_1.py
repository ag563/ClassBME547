def calc_square_root(n):
    try:
        from calculator import sqrt
    except ModuleNotFoundError:
        print("The my_calculator module did not exist.")
        print("Use the builtin math module instead.")
        from math import sqrt
    except ImportError:
        print("The sqrt function did not exist.")
    except:
        print("Error")
        return
    answer = sqrt(n)
    return answer

def main():
    print(calc_square_root(-2))


if __name__ == "__main__":
    main()