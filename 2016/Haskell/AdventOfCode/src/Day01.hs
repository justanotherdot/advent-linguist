-- module Day01 (solveDay01) where
module Day01 where

import           Data.Char       (isDigit)
import           Data.Complex
import           Data.Foldable   (foldl')
import           Data.List.Split (splitOn)
import           Data.Map.Strict (Map, union)
import qualified Data.Map.Strict as M

type Point   = Complex Double
type Instr   = String
type Command = (Instr, Point)

origin :: Point
origin = 0 :+ 0

commands :: [String] -> [Command]
commands = map processCommand
  where
    processCommand s = (dir, dist)
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

processCommands :: [Command] -> Point
processCommands = snd . foldl' step (north, origin)
  where north = 0 :+ 1

processCommands' :: [Command] -> [Point]
processCommands' = map snd. scanl step (north, origin)
  where north = 0 :+ 1

calcAns :: Point -> Double
calcAns (x :+ y) = abs x + abs y

deltas :: [Command] -> [Point]
deltas = drop 1 . scanl1 (flip (-)) . processCommands'

explodePoint :: Point -> [Point]
explodePoint p
  | realPart p == 0.0  = replicate (abs . floor . imagPart $ p) (0 :+ signum (imagPart p))
  | imagPart p == 0.0  = replicate (abs . floor . realPart $ p) (signum (realPart p) :+ 0)
  | otherwise = error "Invalid tuple provided to `explodePoint`"

walk :: [Point] -> Point -> Map (Double, Double) Bool -> Point
walk []     _ _ = error "Did not encounter any places twice"
walk (s:ss) p m = case M.lookup (x, y) m of
                    Just _  -> p'
                    Nothing -> walk ss p' m'
  where p'@(x :+ y) = p + s
        m'          = M.insert (x, y) True m

solveDay01 :: FilePath -> IO ()
solveDay01 pathToInput = do
  ls <- readFile pathToInput
  let cleanInput = splitOn ", " ls
  print . calcAns . processCommands . commands $ cleanInput
  let steps'  = concatMap explodePoint . deltas . commands $ cleanInput
  print $ calcAns $ walk steps' origin M.empty
