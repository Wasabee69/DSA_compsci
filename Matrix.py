###
import sys
class Matrix:
    def multiply(A, B):
        m1, n1 = len(A), len(A[0])
        m2, n2 = len(B), len(B[0])
        if n1 != m2: return None
        M = [[0] * n2 for _ in range(m1)]
        for i in range(m1):
            for j in range(n2):
                for k in range(n1):
                    M[i][j] += A[i][k] * B[k][j]
        return M
    def exponentiate(M, c):
        m, n = len(M), len(M[0])
        if m != n: return None
        Im = [[1 if i == j else 0 for i in range(n)] for j in range(n)] # Identitetsmatrisen
        while c:
            if c&1:
                Im = Matrix.multiply(Im, M)
            M = Matrix.multiply(M, M)
            c>>=1
        return Im
    def RREF(M):
        m, n = len(M), len(M[0])-1
        # vi skal løse alle kolonner utenom den siste, så n-1.
        row = 0
        for col in range(n):
            if row == m: break
            best_pivot = row
            for i in range(row, m):
                if abs(M[i][col]) > abs(M[best_pivot][col]):
                    best_pivot = i
            if abs(M[best_pivot][col]) < 1e-12:continue
            M[row], M[best_pivot] = M[best_pivot], M[row]
            # nå er pivot raden i variabelen row
            for j in range(n, col-1, -1):
                M[row][j] /= M[row][col] # 0 4 8 12 -> 0 1 2 3 # skaler til ledende ener
                
            for i in range(m):
                if i == row:continue
                f = M[i][col]
                for j in range(col, n+1):
                    M[i][j] -= f * M[row][j] # eliminer denne raden for 0 ved pivot-kolonne
            row += 1
        return M
    def solution_Xn(M):
        m, n = len(M), len(M[0])-1
        Xn = [0.0] * n
        for i in range(m):
            for j in range(n):
                if abs(M[i][j] - 1.0) <= 1e-12: # funnet eneren
                    Xn[j] = M[i][-1]
                    break
            else:
                if abs(M[i][n]) > 1e-12: return [None] * n # en rad med  [0 0 0 0 : konstant] -> Ingen løsning
        return Xn


M = [[2, -1, 0, 0],
     [-1, 2, -1, 0],
     [0, -1, 2, 4]]
print(Matrix.RREF(M))