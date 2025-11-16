#!/usr/bin/env python3
"""
Practical 10
Coding and decoding messages using nonsingular matrices.
Simple scheme:
- Map A-Z and space to numbers 0-26.
- Group message into blocks of size n (n = matrix size).
- Encode: cipher = M * block (mod some base) OR numeric real transform.
For simplicity, we use integer arithmetic mod 29 (prime-ish) so inverse exists if det != 0 mod 29.
"""
import sys
import numpy as np

ALPH = {c:i for i,c in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ ")}
INV_ALPH = {i:c for c,i in ALPH.items()}
MOD = 29

def text_to_blocks(text, n):
    text = text.upper()
    nums = [ALPH.get(c, 26) for c in text]  # unknowns -> space
    # pad with spaces (value 26)
    while len(nums) % n != 0:
        nums.append(26)
    blocks = [nums[i:i+n] for i in range(0,len(nums),n)]
    return np.array(blocks).T  # shape n x k

def blocks_to_text(blocks):
    out = []
    for col in blocks.T:
        for v in col:
            v = int(round(v)) % MOD
            out.append(INV_ALPH.get(v if v in INV_ALPH else 26))
    return "".join(out).strip()

def read_matrix_and_message():
    print("Enter square encoding matrix entries row-wise (space-separated). Blank -> default 2x2:")
    rows=[]
    while True:
        l=sys.stdin.readline().strip()
        if l=="":
            break
        rows.append([int(x) for x in l.split()])
    if not rows:
        M = np.array([[3,3],[2,5]], dtype=int)
    else:
        M = np.array(rows,dtype=int)
    if M.shape[0] != M.shape[1]:
        raise SystemExit("Matrix must be square.")
    print("Enter message to encode:")
    msg = sys.stdin.readline().strip()
    if msg=="":
        msg="Linear Algebra is fun"
    return M % MOD, msg

def mod_inv_matrix(M, mod):
    from sympy import Matrix
    return np.array(Matrix(M).inv_mod(mod), dtype=int)

def main():
    M, msg = read_matrix_and_message()
    n = M.shape[0]
    print("Using modulus", MOD)
    # check invertibility mod MOD
    try:
        Minv = mod_inv_matrix(M, MOD)
    except Exception as e:
        print("Matrix not invertible modulo", MOD, "error:", e)
        return
    blocks = text_to_blocks(msg, n)
    cipher = (M.dot(blocks)) % MOD
    print("\nCipher blocks (numbers):\n", cipher)
    decoded_blocks = (Minv.dot(cipher)) % MOD
    decoded = blocks_to_text(decoded_blocks)
    print("\nDecoded message:\n", decoded)

if __name__ == "__main__":
    main()
