module Day03 where

import           Data.List (sort)

processInput :: String -> [[Integer]]
processInput = map (map (read :: String -> Integer) . words) . lines

isTriangle :: [Integer] -> Bool
isTriangle xs = (> last xs') . sum . take 2 $ xs'
  where xs' = sort xs

solveDay03 :: FilePath -> IO ()
solveDay03 path = do
  putStrLn "Solution for day three: "
  ls <- readFile path
  let ls' = processInput ls
  print . length . filter isTriangle $ ls'
  putStrLn ""
