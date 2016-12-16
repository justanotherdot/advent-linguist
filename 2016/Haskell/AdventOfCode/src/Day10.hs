module Day10 where

import           Control.Concurrent
import           Control.Concurrent.Async
import           Control.Monad
import           Data.Map                 (Map)
import qualified Data.Map                 as M

type Bot     = (BotChan, Id, OutputT, OutputT, [Int])
type BotChan = Chan Int
type BotDir  = Map Int Bot
data OutputT = Bot Int | Bin Int deriving (Show, Eq)
type Id      = Int

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

createBot :: String ->  IO (Id, Bot)
createBot s = do
  ch <- newChan
  let (bid, lo, hi) = parseBotLine s
  return (bid, (ch, bid, lo, hi, []))

spawnBot :: BotDir -> Bot -> IO (Async ())
spawnBot dir bot = async (respond dir bot)

sendTo :: BotDir -> Int -> OutputT -> IO ()
sendTo dir val (Bot bid) =
  case M.lookup bid dir of
    Just (ch, _, _, _, _) -> writeChan ch val
    Nothing            -> error $ "Cannot find bot with that ID: " ++ show bid
sendTo _ val (Bin bid) =
  putStrLn $ show val ++ " sent to bin " ++ show bid

respond :: BotDir -> Bot -> IO ()
respond dir (ch, bid, lo, hi, vs) = do
  x <- readChan ch
  let vs' = x:vs
  let loVal = minimum vs'
  let hiVal = maximum vs'
  when (loVal == 17 && hiVal == 61)
    (putStrLn $ "Bot " ++ show bid ++ " comparing 17 and 61")
  when (length vs' >= 2)
    (sendTo dir loVal lo >> sendTo dir hiVal hi)
  respond dir (ch, bid, lo, hi, vs')

parseValueLine :: String -> (Int, OutputT)
parseValueLine s = (read (ws !! 1), out)
  where ws  = words s
        out = case ws !! 4 of
                "bot"    -> Bot (read (ws !! 5))
                "output" -> Bin (read (ws !! 5))
                _        -> error $ "Parse error: couldn't parse " ++ show s

solveDay10 :: FilePath -> IO ()
solveDay10 path = do
  s <- readFile path
  let ls = lines s
  bs <- M.fromList <$> traverse createBot (filter ((=='b') . head) ls)
  as <- traverse (spawnBot bs) bs
  let vs = map parseValueLine (filter ((=='v') . head) ls)
  putStrLn "Solution for day ten: "
  void $! traverse (uncurry $ sendTo bs) vs
  mapM_ wait as
