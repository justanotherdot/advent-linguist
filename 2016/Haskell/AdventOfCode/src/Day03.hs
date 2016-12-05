module Day03 where

import           Data.List (sort)

processInput :: String -> [[Integer]]
processInput = map (map (read :: String -> Integer) . words) . lines

processInput' :: String -> [[Integer]]
processInput' s = condenseList $ map (map (read :: String -> Integer) . threeTupleToList) zs
  where ls = words s
        zs = zip3 ls (drop 3 ls) (drop 6 ls)

threeTupleToList :: (a, a, a) -> [a]
threeTupleToList (x, y, z) = [x, y, z]

isTriangle :: [Integer] -> Bool
isTriangle xs = 2 * last xs' < sum xs'
  where xs' = sort xs

condenseList :: [[Integer]] -> [[Integer]]
condenseList [] = []
condenseList ls = take 3 ls ++ condenseList (drop 9 ls)

solveDay03 :: FilePath -> IO ()
solveDay03 path = do
  putStrLn "Solution for day three: "
  ls <- readFile path
  let ls' = processInput ls
  print . length . filter isTriangle $ ls'
  let ls'' = processInput' ls
  print . length . filter isTriangle $ ls''
  putStrLn ""
