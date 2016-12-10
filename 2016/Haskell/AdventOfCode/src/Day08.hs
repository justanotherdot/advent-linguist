module Day08 where

import           Data.List.Split (splitOn)
import           Data.Vector     (Vector)
-- import qualified Data.Vector as V

data Command = Rect Integer Integer
             | RotRow Integer Integer
             | RotCol Integer Integer
             deriving Show

type LCDScreen = Vector Bool

toRect :: String -> Command
toRect s = Rect (read $ head vals) (read $ last vals)
  where vals = splitOn "x" s

-- Ugly.
toRot :: [String] -> Command
toRot ss = case t of
            "row"    -> RotRow ix amt
            "column" -> RotCol ix amt
            _        -> error "Unrecognized command while parsing"
  where t   = head ss
        ix  = read . last . splitOn "=" . head . take 1 . drop 1 $ ss
        amt = read $ last ss

toCommand :: String -> Command
toCommand s = case head parts of
                "rect"   -> toRect (last parts)
                "rotate" -> toRot (tail parts)
                _        -> error "Unrecognized command while parsing"
  where parts = words s


parseInput :: String -> [Command]
parseInput s = map toCommand ls
  where ls = filter (not . null) . lines $ s

rectOn :: LCDScreen -> Integer -> Integer -> LCDScreen
rectOn _lcd _w _h = undefined

rotRow :: LCDScreen -> Integer -> Integer -> LCDScreen
rotRow _lcd _row _amt = undefined

rotCol :: LCDScreen -> Integer -> Integer -> LCDScreen
rotCol _lcd _col _amt = undefined

solveDay08 :: FilePath -> IO ()
solveDay08 path = do
  s <- readFile path
  putStrLn "Solution for day eight: "
  mapM_ print $ parseInput s
  putStrLn ""
