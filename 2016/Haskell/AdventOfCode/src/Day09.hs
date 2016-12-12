{-# LANGUAGE OverloadedStrings #-}

module Day09 where

import           Data.Text      (Text)
import qualified Data.Text      as T
import qualified Data.Text.IO   as TIO
import           Data.Text.Read (decimal)
import           Prelude        hiding (toInteger)

parseMarker :: Text -> (Integer, Integer)
parseMarker m = (toInteger x, toInteger y)
  where
    [x, y] = T.splitOn "x" m
    toInteger s =
      case decimal s of
        Right v -> fst v
        Left  _ -> error "Invalid conversion while processing nonterminal"

evalExprs :: Bool -> Text -> Integer
evalExprs pt2 es
  | T.null es = 0
  | currElem == '(' =
      let
        (marker, es') = T.breakOn ")" (T.tail es)
        (qty, reps)   = parseMarker marker
        qty'          = fromIntegral qty :: Int
        rst           = T.take qty' $ T.tail es'
        len           = fromIntegral (T.length rst) :: Integer
      in if pt2
        then reps * evalExprs pt2 rst + evalExprs pt2 (T.drop (qty'+1) es')
        else reps * len + evalExprs pt2 (T.drop (qty'+1) es')
  | otherwise = 1 + evalExprs pt2 (T.tail es)
  where currElem = T.head es

solveDay09 :: FilePath -> IO ()
solveDay09 path = do
  s <- TIO.readFile path
  putStrLn "Solution for day nine: "
  print . evalExprs False $ T.strip s
  print . evalExprs True $ T.strip s
  putStrLn ""
