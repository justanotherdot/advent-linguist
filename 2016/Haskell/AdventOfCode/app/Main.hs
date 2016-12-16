module Main where

import           Day01 (solveDay01)
import           Day02 (solveDay02)
import           Day03 (solveDay03)
import           Day04 (solveDay04)
-- import           Day05 (solveDay05)
import           Day06 (solveDay06)
import           Day07 (solveDay07)
import           Day08 (solveDay08)
import           Day09 (solveDay09)
-- import           Day10 (solveDay10)

solveDay05Dummy :: IO ()
solveDay05Dummy = do
  putStrLn "Solution for day five: "
  putStrLn "f97c354d"
  putStrLn "863dde27"
  putStrLn ""

solveDay10Dummy :: IO ()
solveDay10Dummy = do
  putStrLn "Solutio nfor day ten: "
  putStrLn "Bot 86 compared 17 and 61"
  putStrLn "67*11*31 = 22847"
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
  solveDay07 "./input/day07.in"
  solveDay08 "./input/day08.in"
  solveDay09 "./input/day09.in"
  -- solveDay10 "./input/day10.in"
  solveDay10Dummy
