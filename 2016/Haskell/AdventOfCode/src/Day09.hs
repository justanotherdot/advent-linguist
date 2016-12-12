{-# LANGUAGE OverloadedStrings #-}

module Day09 where

import           Data.Text      (Text)
import qualified Data.Text      as T
import qualified Data.Text.IO   as TIO
import           Data.Text.Read (decimal)
import           Prelude        hiding (toInteger)

data Mode = PartOne | PartTwo

parseMarker :: Text -> (Int, Int)
parseMarker m = (toInt x, toInt y)
  where
    [x, y] = T.splitOn "x" m
    toInt s =
      case decimal s of
        Right v -> fst v
        Left  _ -> error "Invalid conversion while processing nonterminal"

evalExprs :: Mode -> Text -> Int
evalExprs mode es
  | T.null es = 0
  | currElem == '(' =
      let
        (marker, es') = T.breakOn ")" (T.tail es)
        (qty, reps)   = parseMarker marker
        chunk         = T.take qty $ T.tail es'
        rst           = T.drop (qty+1) es'
      in case mode of
          PartOne -> reps * T.length chunk + evalExprs mode rst
          PartTwo -> reps * evalExprs mode chunk + evalExprs mode rst
  | otherwise = 1 + evalExprs mode (T.tail es)
  where currElem = T.head es

solveDay09 :: FilePath -> IO ()
solveDay09 path = do
  s <- TIO.readFile path
  putStrLn "Solution for day nine: "
  print . evalExprs PartOne $ T.strip s
  print . evalExprs PartTwo $ T.strip s
  putStrLn ""
