{-# LANGUAGE CPP               #-}
{-# LANGUAGE OverloadedStrings #-}

module Day05 where

#define PAR 1

#if PAR
import           Control.Monad.Par
#endif

import           Crypto.Hash
import           Data.ByteString.Char8 (pack)
import           Data.Monoid

doorID :: String
doorID = "reyedfim"

md5 :: String -> Digest MD5
md5 = hash . pack

crackPassword :: String -> Integer -> String
crackPassword s n
  | n > (10^(7 :: Integer)) = s
  -- | length s == 8 = s
  | otherwise     = if all (=='0') left
                      then crackPassword (s <> [head right]) (n+1)
                      else crackPassword s (n+1)
    where
      digest = show . md5 $ doorID <> show n
      (left, right) = splitAt 5 digest

crackPassword' :: Integer -> String
crackPassword' n = if all (=='0') left then take 1 right else ""
    where
      digest = show . md5 $ doorID <> show n
      (left, right) = splitAt 5 digest

solveDay05 :: IO ()
solveDay05 = do
  putStrLn "Solution for day five: "
#if PAR == 0
  print . reverse . crackPassword [] $ 0
#else
  print $ runPar $ parMapReduceRangeThresh 100 (InclusiveRange 1 (10^(7 :: Integer))) (\x -> return $ crackPassword' (fromIntegral x :: Integer)) (\x y -> return (x ++ y)) []
#endif
  putStrLn ""
