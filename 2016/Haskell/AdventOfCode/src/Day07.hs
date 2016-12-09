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

isABA :: String -> Bool
isABA [x, y, z] = x == z && x /= y
isABA _         = False

allABAs :: String -> [String]
allABAs = filter isABA . chunksOf' 3
  where
    chunksOf' n xs
      | length xs < 3 = []
      | otherwise      = take n xs : chunksOf' n (drop 1 xs)

fromABAtoBAB :: String -> String
fromABAtoBAB s = [b, a, b]
  where a = head s
        b = s !! 1

containsBAB :: String -> String -> Bool
containsBAB babPat s = s =~ babPat

hasSSL :: ([String], [String]) -> Bool
hasSSL ios = (not . null) abas && or babs
  where abas = let os = snd ios
               in concatMap allABAs os
        babs = let is = fst ios
               in concatMap (\x -> map (containsBAB (fromABAtoBAB x)) is) abas

hasTLS :: ([String], [String]) -> Bool
hasTLS ios = not (any isABBA (fst ios)) && any isABBA (snd ios)

calcAns :: [Bool] -> Int
calcAns = length . filter (==True)

solveDay07 :: FilePath -> IO ()
solveDay07 path = do
  ls <- readFile path
  putStrLn "Solution for day seven: "
  print . calcAns . map (hasTLS . innersAndOuters) . transformInput $ ls
  print . calcAns . map (hasSSL . innersAndOuters) . transformInput $ ls
  putStrLn ""
