-- module Day01 (solveDay01) where
module Day01 where

import           Data.Char       (isDigit)
import           Data.Complex
import           Data.Foldable   (foldl')
import           Data.List.Split (splitOn)
import           Data.Map.Strict (Map)
import qualified Data.Map.Strict as M

type Point   = Complex Double
type Instr   = String
type Command = (Instr, Point)

origin :: Point
origin = 0 :+ 0

commands :: [String] -> [Command]
commands = map parseCommand
  where
    parseCommand s = (dir, dist)
      where dir  = take 1 s
            dist = (read (takeWhile isDigit (drop 1 s)) :: Double) :+ 0

-- √-1
i :: Complex Double
i = 0 :+ 1

step :: (Point, Point) -> Command -> (Point, Point)
step (heading, point) ("R", dist) = (h', (h' * dist) + point)
  where h' = heading * conjugate i
step (heading, point) ("L", dist) = (h', (h' * dist) + point)
  where h' = heading * i
step _ _                          = error "Unrecognized command"

step' :: (Point, [Point]) -> Command -> (Point, [Point])
step' (heading, points) (cmd, dist)
  | cmd == "R" = let h' = heading * conjugate i
                 in (h', points ++ explodePoint (h' * dist))
  | cmd == "L" = let h' = heading * i
                 in (h', points ++ explodePoint (h' * dist))
  | otherwise  = error "Unrecognized command in `steps`"

processCommands' :: [Command] -> [Point]
processCommands' = snd . foldl' step' (north, [])
  where north = 0 :+ 1

processCommands :: [Command] -> Point
processCommands = snd . foldl' step (north, origin)
  where north = 0 :+ 1

calcAns :: Point -> Double
calcAns (x :+ y) = abs x + abs y

explodePoint :: Point -> [Point]
explodePoint (x :+ y)
  | x == 0  = replicate (abs . floor $ y) (0 :+ signum y)
  | y == 0  = replicate (abs . floor $ x) (signum x :+ 0)
  | otherwise = error "Invalid point provided to `explodePoint`"

walk :: [Point] -> Point
walk ps = go ps origin M.empty
  where
    go :: [Point] -> Point -> Map (Double, Double) Bool -> Point
    go []     _ _ = error "Did not encounter any places twice"
    go (s:ss) p m = case M.lookup (x, y) m of
                        Just _  -> p'
                        Nothing -> go ss p' m'
      where p'@(x :+ y) = p + s
            m'          = M.insert (x, y) True m

solveDay01 :: FilePath -> IO ()
solveDay01 pathToInput = do
  ls <- readFile pathToInput
  let cleanInput = splitOn ", " ls
  -- Part 1
  print . calcAns . processCommands . commands $ cleanInput
  -- Part 2
  print . calcAns . walk . processCommands' . commands $ cleanInput
