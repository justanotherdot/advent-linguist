-- module Day01 (solveDay01) where
module Day01 where

import           Data.Char       (isDigit)
import           Data.Complex
import           Data.Foldable   (foldl')
import           Data.List.Split (splitOn)
import           Data.Map.Strict (Map)
import qualified Data.Map.Strict as M

origin :: Complex Double
origin = 0 :+ 0

north :: Complex Double
north = 0 :+ 1

commands :: [String] -> [(String, Complex Double)]
commands = map processCommand
  where
    processCommand s = (dir, dist)
      where dir  = take 1 s
            dist = (read (takeWhile isDigit (drop 1 s)) :: Double) :+ 0

-- √-1
i :: Complex Double
i = 0 :+ 1

step :: (Complex Double, Complex Double) ->
        (String, Complex Double)         ->
        (Complex Double, Complex Double)
step (heading, point) ("R", dist) = (h', (h' * dist) + point)
  where h' = heading * conjugate i
step (heading, point) ("L", dist) = (h', (h' * dist) + point)
  where h' = heading * i
step _ _                          = error "Unrecognized command"

processCommands :: [(String, Complex Double)] -> Complex Double
processCommands = snd . foldl' step (north, origin)

-- Setup for part2 solution.
processCommands' :: [(String, Complex Double)] -> [(Complex Double, Complex Double)]
processCommands' = scanl step (north, origin)

calcAns :: Complex Double -> Double
calcAns (x :+ y) = abs x + abs y

sndPart :: [Complex Double]
        -> Map (Double, Double) Bool
        -> Complex Double
sndPart []     _ = error "Never revisted any location"
sndPart (p@(p1 :+ p2):ps) m = case M.lookup (p1, p2) m of
                    Just _  -> p
                    Nothing -> sndPart ps $ M.insert (p1, p2) True m 

solveDay01 :: FilePath -> IO ()
solveDay01 pathToInput = do
  ls <- readFile pathToInput
  let cleanInput = splitOn ", " ls
  print $ calcAns . processCommands . commands $ cleanInput
  let points = map snd .processCommands' . commands $ cleanInput
  print $ calcAns $ sndPart points M.empty
