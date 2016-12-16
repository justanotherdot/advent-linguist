module Day10 where

import           Control.Concurrent
import           Control.Monad
import           Data.Map           (Map)
import qualified Data.Map           as M

type BotChan = Chan Int
type BotDir  = Map Int (BotChan, Id, OutputT, OutputT)
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

createBot :: String ->  IO (Id, (BotChan, Id, OutputT, OutputT))
createBot s = do
  ch <- newChan
  let (bid, lo, hi) = parseBotLine s
  return (bid, (ch, bid, lo, hi))

spawnBot :: BotDir -> (BotChan, Id, OutputT, OutputT) -> IO ()
spawnBot dir (ch, _bid, lo, hi) = void $! forkIO (respond dir ch lo hi)

sendTo :: BotDir -> Int -> OutputT -> IO ()
sendTo dir val (Bot bid) =
  case M.lookup bid dir of
    Just (ch, _, _, _) -> writeChan ch val
    Nothing            -> error $ "Cannot find bot with that ID: " ++ show bid
sendTo _ _ _ = undefined

respond :: BotDir -> BotChan -> OutputT -> OutputT -> IO ()
respond dir ch lo hi = do
  x <- readChan ch
  if x == 17 then print "hello" else print "nope"
  respond dir ch lo hi

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
  void $! traverse (spawnBot bs) bs
  let vs = map parseValueLine (filter ((=='v') . head) ls)
  putStrLn "Solution for day ten: "
  mapM_ (uncurry $ sendTo bs) vs
  putStrLn ""
