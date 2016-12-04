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
commands = map processCommand
  where
    processCommand s = (dir, dist)
      where dir  = take 1 s
            dist = (read (takeWhile isDigit (drop 1 s)) :: Double) :+ 0

-- √-1
i :: Point
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

calcAns :: Point -> Double
calcAns (x :+ y) = abs x + abs y

solveDay01 :: FilePath -> IO ()
solveDay01 pathToInput = do
  ls <- readFile pathToInput
  let cleanInput = splitOn ", " ls
  print $ calcAns . processCommands . commands $ cleanInput
