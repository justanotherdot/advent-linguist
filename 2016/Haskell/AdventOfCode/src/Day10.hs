module Day10 where

import           Control.Concurrent
import           Data.Map           (Map)
-- import qualified Data.Map           as M

type BotChan = Chan Int
type BotDir  = Map Int BotChan
data OutputT = Bot Int | Bin Int deriving (Show, Eq)
type Id = Int

parseBotLine :: String -> (Id, OutputT, OutputT)
parseBotLine s = (bid, loType, hiType)
  where
    ws     = words s
    bid    = read (ws !! 1) :: Int
    loVal  = read (ws !! 6) :: Int
    hiVal  = read (ws !! 11) :: Int
    loType = case ws !! 5 of
              "bot"    -> Bot loVal
              "output" -> Bin loVal
              _        -> error $ "Parse error: couldn't parse '" ++ s ++ "'"
    hiType = case ws !! 10 of
              "bot"    -> Bot hiVal
              "output" -> Bin hiVal
              _        -> error $ "Parse error: couldn't parse '" ++ s ++ "'"

createBot :: BotChan -> String ->  IO (BotChan, Id, OutputT, OutputT)
createBot ch s = do
  let (bid, lo, hi) = parseBotLine s
  return (ch, bid, lo, hi)

respond :: BotChan -> OutputT -> OutputT -> IO ()
respond ch _lo _hi = do
  x <- readChan ch
  if x == 17 then print "hello" else print "nope"

solveDay10 :: FilePath -> IO ()
solveDay10 path = do
  s <- readFile path
  let ls = lines s
  putStrLn "Solution for day ten: "
  print ls
  putStrLn ""
