-- {-# LANGUAGE OverloadedStrings #-}

module Day05 where

import           Crypto.Hash
-- import           Data.ByteString.Builder
import           Data.ByteString.Char8 (pack)
-- import           Data.ByteString.Char8   (all, pack, singleton)
-- import           Data.ByteString.Lazy    (ByteString, head, length, print,
--                                           splitAt, toStrict)
import           Data.Monoid
-- import           Prelude               hiding (all, head, length, print, splitAt)
-- import           Text.Show.ByteString  (show)

doorID :: String
doorID = "reyedfim"

md5 :: String -> Digest MD5
md5 = hash . pack

crackPassword :: String -> Integer -> String
crackPassword s n
  | length s == 8 = s
  | otherwise     = if all (=='0') left
                      then crackPassword (s <> [head right]) (n+1)
                      else crackPassword s (n+1)
    where
      digest = show . md5 $ doorID <> show n
      (left, right) = splitAt 5 digest


solveDay05 :: IO ()
solveDay05 = do
  putStrLn "Solution for day five: "
  print $ crackPassword "" 0
  putStrLn ""
