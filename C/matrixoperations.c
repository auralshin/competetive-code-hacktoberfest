#include <stdio.h>
#include <conio.h>
#include <math.h>

#define MAX 3

void matrix ( int [3][3] ) ;
void create ( int [3][3] ) ;
void display ( int [3][3] ) ;
void matmul ( int [3][3], int [3][3], int [3][3] ) ;
void transpose ( int [3][3], int [3][3] ) ;
int determinant ( int [3][3] ) ;
int isortho ( int [3][3] ) ;

void main( )
{
    int mat [3][3], d ;

    clrscr( ) ;

    printf ( "\nEnter elements for array: \n\n" ) ;
    create ( mat ) ;

    printf ( "\nThe Matrix: \n" ) ;
    display ( mat ) ;

    d = determinant ( mat ) ;
    printf ( "\nThe determinant for given matrix: %d.\n", d ) ;

    if ( d == 0 )
        printf ( "\nMatrix is singular.\n" ) ;
    else
        printf ( "\nMatrix  is not singular.\n" ) ;

    d = isortho ( mat ) ;

    if ( d != 0 )
        printf ( "\nMatrix is orthogonal.\n" ) ;
    else
        printf ( "\nMatrix is not orthogonal.\n" ) ;

    getch( ) ;
}

/* initializes the matrix mat with 0 */
void matrix ( int mat[3][3] )
{
    int i, j ;
    for ( i = 0 ; i < MAX ; i++ )
    {
        for ( j = 0 ; j < MAX ; j++ )
            mat[i][j] = 0 ;
    }
}

/* creates matrix mat */
void create ( int mat[3][3] )
{
    int n, i, j ;
    for ( i = 0 ; i < MAX ; i++ )
    {
        for ( j = 0 ; j < MAX ; j++ )
        {
            printf ( "Enter the element: " ) ;
            scanf ( "%d", &n ) ;
            mat[i][j] = n ;
        }
    }
}

/* displays the contents of matrix */
void display ( int mat[3][3] )
{
    int i, j ;
    for ( i = 0 ; i < MAX ; i++ )
    {
        for ( j = 0 ; j < MAX ; j++ )
            printf ( "%d\t", mat[i][j] ) ;
        printf ( "\n" ) ;
    }
}

/* multiplies two matrices */
void matmul ( int mat1[3][3], int mat2[3][3], int mat3[3][3] )
{
    int i, j, k ;
    for ( k = 0 ; k < MAX ; k++ )
    {
        for ( i = 0 ; i < MAX ; i++ )
        {
            mat3[k][i] = 0 ;
            for ( j = 0 ; j < MAX ; j++ )
                mat3[k][i] += mat1[k][j] * mat2[j][i] ;
        }
    }
}

/* obtains transpose of matrix m1 */
void transpose ( int mat[3][3], int m[3][3] )
{
    int i, j ;
    for ( i = 0 ; i < MAX ; i++ )
    {
        for ( j = 0 ; j < MAX ; j++ )
             m[i][j] = mat[j][i] ;
    }
}

/* finds the determinant value for given matrix */
int determinant( int mat[3][3] )
{
    int sum, i, j, k, p ;
    sum = 0 ; j = 1 ; k = MAX - 1 ;

    for ( i = 0 ; i < MAX ; i++ )
    {
        p = pow ( -1, i ) ;

        if ( i == MAX - 1 )
            k = 1 ;
        sum = sum + ( mat[0][i] * ( mat[1][j] * mat[2][k] - mat[2][j] * mat[1][k] ) ) * p ;
        j = 0 ;
    }

    return sum ;
}

/* checks if given matrix is an orthogonal matrix */
int isortho ( int mat[3][3] )
{
    /* transpose the matrix */
int m1[3][3], m2[3][3], i ;
    transpose ( mat, m1 ) ;

    /* multiply the matrix with its transpose */

    matmul ( mat, m1, m2 ) ;

    /* check for the identity matrix */
for ( i = 0  ; i < MAX ; i++ )
    {
        if ( m2[i][i] == 1 )
            continue ;
        elsebreak ;
    }
    if ( i == MAX )
        return 1 ;
    elsereturn 0 ;
}
