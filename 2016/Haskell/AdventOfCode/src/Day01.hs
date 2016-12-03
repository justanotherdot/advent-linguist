-- module Day01 (solveDay01) where
module Day01 where

import           Data.Complex
import           Data.Foldable     (foldl')
import qualified Data.HashMap.Lazy as HM

type Point = Complex Double

origin :: Point
origin = 0 :+ 0

north :: Point
north = 0 :+ 1

cleanInput :: String -> String
cleanInput "" = ""
cleanInput s  = take 2 s

type Command = (String, Double)

parseInput :: String -> Command
parseInput s = (dir, dist)
  where dir  = take 1 s
        dist = read (take 1 $ drop 1 s) :: Double

processCommand :: Command -> (Point, Point) -> Either String (Point, Point)
processCommand ("R", dist) (dir, p) = Right (dir', p')
  where i'    = 0 :+ (-1)
        dist' = dist :+ 0
        dir'  = dir * i'
        p'    = (dir' * dist') + p
processCommand ("L", dist) (dir, p) = Right (dir', p')
  where i     = 0 :+ 1
        dist' = dist :+ 0
        dir'  = dir * i
        p'    = (dir' * dist') + p
processCommand _ _ = Left "Unrecognized command in input"

processAllCommands :: [Command] -> Point
processAllCommands = snd . foldl' go (north, origin)
  where go t c = case processCommand c t of
                  Right x' -> x'
                  Left  s  -> error s

solveDay01 :: FilePath -> IO ()
solveDay01 pathToInput = do
  ls <- readFile pathToInput
  let cs = map (parseInput . cleanInput) $ words ls
  let dest = processAllCommands cs
  print $ abs (realPart dest) + abs (imagPart dest)
