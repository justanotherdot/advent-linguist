module Main where

import           Day01 (solveDay01)
import           Day02 (solveDay02)
import           Day03 (solveDay03)

main :: IO ()
main = do
  solveDay01 "./input/day01.in"
  solveDay02 "./input/day02.in"
  solveDay03 "./input/day03.in"
