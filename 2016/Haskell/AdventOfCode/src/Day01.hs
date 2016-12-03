-- module Day01 (solveDay01) where
module Day01 where

import           Control.Monad   (mapM_)
import           Data.Complex
import           Data.Foldable   (foldl')
import           Data.List.Split (splitOn)
import           Text.Printf

origin :: Complex Double
origin = 0 :+ 0

north :: Complex Double
north = 0 :+ 1

commands :: [String] -> [(String, Complex Double)]
commands = map processCommand
  where
    processCommand s = (dir, dist)
      where dir  = take 1 s
            dist = (read (take 1 (drop 1 s)) :: Double) :+ 0

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

processCommands :: [(String, Complex Double)] ->
                   [(Complex Double, Complex Double)]
processCommands = scanl step (north, origin)

calcAns :: Complex Double -> Double
calcAns (x :+ y) = abs x + abs y

pprint :: (Complex Double, Complex Double) -> IO ()
pprint (a0 :+ b0, a1 :+ b1) = printf "Heading: %4f + %4fi, Position: %4f + %4fi\n" a0 b0 a1 b1

solveDay01 :: FilePath -> IO ()
solveDay01 pathToInput = do
  ls <- readFile pathToInput
  let cleanInput = splitOn ", " ls
  mapM_ pprint $ processCommands . commands $ cleanInput
