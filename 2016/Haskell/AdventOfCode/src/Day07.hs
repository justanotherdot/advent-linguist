module Day07 where

import           Data.List.Split (splitOneOf)
import           Text.Regex.PCRE

transformInput :: String -> [[(Integer, String)]]
transformInput = map (zip [(1 :: Integer)..] . splitOneOf "[]") . lines

outers :: [(Integer, String)] -> [String]
outers = map snd . filter (odd . fst)

inners :: [(Integer, String)] -> [String]
inners = map snd . filter (even . fst) . init

innersAndOuters :: [(Integer, String)] -> ([String], [String])
innersAndOuters vs = (inners vs, outers vs)

isABBA :: String -> Bool
isABBA s = (not . null $ textMatches) && any hasDistinct textMatches
  where
    matches :: AllTextMatches [] String
    matches       = s =~ "(.)(.)\\2\\1"
    textMatches   = getAllTextMatches matches
    hasDistinct x = head (take 2 x) /= last (take 2 x)

hasTLS :: ([String], [String]) -> Bool
hasTLS ios = not (any isABBA (fst ios)) && any isABBA (snd ios)

calcAns :: [Bool] -> Int
calcAns = length . filter (==True)

solveDay07 :: FilePath -> IO ()
solveDay07 path = do
  ls <- readFile path
  putStrLn "Solution for day seven: "
  print . calcAns . map (hasTLS . innersAndOuters) . transformInput $ ls
  putStrLn ""
