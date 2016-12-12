{-# LANGUAGE OverloadedStrings #-}

module Day09 where

import           Data.Text      (Text)
import qualified Data.Text      as T
import qualified Data.Text.IO   as TIO
import           Data.Text.Read (decimal)
import           Prelude        hiding (toInteger)

data Mode = PartOne | PartTwo

parseMarker :: Text -> (Integer, Integer)
parseMarker m = (toInteger x, toInteger y)
  where
    [x, y] = T.splitOn "x" m
    toInteger s =
      case decimal s of
        Right v -> fst v
        Left  _ -> error "Invalid conversion while processing nonterminal"

evalExprs :: Mode -> Text -> Integer
evalExprs mode es
  | T.null es = 0
  | currElem == '(' =
      let
        (marker, es') = T.breakOn ")" (T.tail es)
        (qty, reps)   = parseMarker marker
        qty'          = fromIntegral qty :: Int
        chunk         = T.take qty' $ T.tail es'
        rst           = T.drop (qty'+1) es'
        len           = fromIntegral (T.length chunk) :: Integer
      in case mode of
          PartOne -> reps * len + evalExprs mode (T.drop (qty'+1) es')
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
