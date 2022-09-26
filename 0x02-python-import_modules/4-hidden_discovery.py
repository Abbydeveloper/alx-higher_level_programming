#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":
    hidden_names = dir(hidden_4)
    for c in hidden_names:
        if c[:2] != "__":
            print(c)
