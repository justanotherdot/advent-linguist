module Day06 where

import           Data.Function (on)
import           Data.List     (group, maximumBy, minimumBy, sort, transpose)

transformInput :: String -> [String]
transformInput = transpose . lines

mostFrequentChar :: String -> Char
mostFrequentChar s = head s'
  where s' = maximumBy (compare `on` length) . group . sort $ s

leastFrequentChar :: String -> Char
leastFrequentChar s = head s'
  where s' = minimumBy (compare `on` length) . group . sort $ s

solveDay06 :: FilePath -> IO ()
solveDay06 path = do
  ls <- readFile path
  putStrLn "Solution for day six: "
  print . map mostFrequentChar . transformInput $ ls
  print . map leastFrequentChar . transformInput $ ls
  putStrLn ""
