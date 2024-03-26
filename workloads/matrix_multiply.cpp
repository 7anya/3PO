// write a program to multiply two matrices
// The program should take the dimensions of the matrices as input
// ramly generate the matrices with random values
// multiply the matrices and print the result
// The program should be able to handle matrices of any size

#include <iostream>
#include <vector>
#include <random>
#include <ctime>

using namespace std;

int main() {
    int m, n, p, q;
    cout << "Enter the dimensions of the first matrix: ";
    cin >> m >> n;
    cout << "Enter the dimensions of the second matrix: ";
    cin >> p >> q;

    if (n != p) {
        cout << "The matrices cannot be multiplied\n";
        return 1;
    }

    vector<vector<int>> A(m, vector<int>(n));
    vector<vector<int>> B(p, vector<int>(q));
    vector<vector<int>> C(m, vector<int>(q));

    srand(time(0));
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            A[i][j] = rand() % 10;
        }
    }

    for (int i = 0; i < p; i++) {
        for (int j = 0; j < q; j++) {
            B[i][j] = rand() % 10;
        }
    }

    for (int i = 0; i < m; i++) {
        for (int j = 0; j < q; j++) {
            C[i][j] = 0;
            for (int k = 0; k < n; k++) {
                C[i][j] += A[i][k] * B[k][j];
            }
        }
    }

    cout << "Matrix A:\n";
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            cout << A[i][j] << " ";
        }
        cout << endl;
    }

    cout << "Matrix B:\n";
    for (int i = 0; i < p; i++) {
        for (int j = 0; j < q; j++) {
            cout << B[i][j] << " ";
        }
        cout << endl;
    }

    cout << "Matrix C:\n";
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < q; j++) {
            cout << C[i][j] << " ";
        }
        cout << endl;
    }

    return 0;
}