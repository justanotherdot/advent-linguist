module Day08 where

import           Data.Vector (Vector)
-- import qualified Data.Vector as V

data Command = Rect Integer Integer
             | RotRow Integer Integer
             | RotCol Integer Integer
             deriving Show

type LCDScreen = Vector Bool

parseInput :: String -> [Command]
parseInput _s = undefined

rectOn :: LCDScreen -> Integer -> Integer -> LCDScreen
rectOn _lcd _w _h = undefined

rotRow :: LCDScreen -> Integer -> Integer -> LCDScreen
rotRow _lcd _row _amt = undefined

rotCol :: LCDScreen -> Integer -> Integer -> LCDScreen
rotCol _lcd _col _amt = undefined

solveDay08 :: FilePath -> IO ()
solveDay08 path = do
  ls <- readFile path
  putStrLn "Solution for day eight: "
  print ls
  putStrLn ""
