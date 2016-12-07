module Main where

import           Day01 (solveDay01)
import           Day02 (solveDay02)
import           Day03 (solveDay03)
import           Day04 (solveDay04)
-- import           Day05 (solveDay05)
import           Day06 (solveDay06)

solveDay05Dummy :: IO ()
solveDay05Dummy = do
  putStrLn "Solution for day five: "
  putStrLn "f97c354d"
  putStrLn "863dde27"
  putStrLn ""

main :: IO ()
main = do
  solveDay01 "./input/day01.in"
  solveDay02 "./input/day02.in"
  solveDay03 "./input/day03.in"
  solveDay04 "./input/day04.in"
  -- solveDay05
  solveDay05Dummy
  solveDay06 "./input/day06.in"
