import Control.Monad
import Data.List

--prints a specific solution
printBoard b = do
    mapM_ (putStrLn) [[ if e == True then 'Q' else 'X' | e <- r] | r <- b]
    putStrLn ""

--creates permutations of all rows of size sz with 1 queen
permuteRows sz = [(replicate (num - 1) False) ++ (True:(replicate (sz - num) False)) | num <- [1..sz]]

--creates permutations of all configurations of n-queens
permuteBoards sz = sequence (replicate sz (permuteRows sz))

--make sure queens are not within a straight shot to one another i.e. can't attack
checkDiagonal b = checkRow (allDiagonals b)
checkRow b = not (any (\row -> length (filter (==True) row) > 1) b)
checkCol b = checkRow (map reverse (transpose b))

--checks for solution i.e. the queens can't attack one another
solutionCheck b = (checkRow b) && (checkCol b) && (checkDiagonal b)

--get the diagonals that exist in the board
allDiagonals b = (diagonals b) ++ (diagonals (map reverse (transpose b)))

diagonals :: [[a]] -> [[a]]
diagonals [] = []
diagonals ([]:cell) = cell
diagonals cell = zipWith (++) (map ((:[]) . head) cell ++ repeat []) ([]:(diagonals (map tail cell)))

--prompts for board size, then attempts to find a solution
nQueens = do
    putStrLn "Board Size:"
    n <- readLn :: IO Int
    let sol = (filter (solutionCheck) (permuteBoards n))
    mapM_ (printBoard) sol
    unless ((length sol) > 0) (putStrLn "No solutions.")
    let num = (length (filter (solutionCheck) (permuteBoards n)))
    putStrLn ("# of solutions: " ++ show num)
    -- print 

--only outputs quantity of board configurations which are valid
nQueensNumSoln = do
    putStrLn "Board Size:"
    n <- readLn :: IO Int
    let num = (length (filter (solutionCheck) (permuteBoards n)))
    putStrLn ("# of solutions: " ++ show num)

--run both functions
main = do
    putStrLn "Testing nQueens..." 
    nQueens