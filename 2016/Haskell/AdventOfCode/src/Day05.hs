{-# LANGUAGE CPP               #-}
{-# LANGUAGE OverloadedStrings #-}

module Day05 where

#define PAR 0

#if PAR
import           Control.Monad.Par
#endif

import           Crypto.Hash
import           Data.ByteString.Lazy.Char8 (pack)
import           Data.Monoid

doorID :: String
doorID = "reyedfim"

md5 :: String -> Digest MD5
md5 = hashlazy . pack

crackPassword :: String -> Integer -> String
crackPassword s n
  | length s == 8 = s
  | otherwise     = if all (=='0') left
                      then crackPassword (s <> take 1 right) (n+1)
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
  print . crackPassword "" $ 0
#else
  print $ runPar $ parMapReduceRangeThresh 897995
                    (InclusiveRange 1 7183956)
                    (\x -> return $ crackPassword' (fromIntegral x :: Integer))
                    (\x y -> return (x <> y)) ""
#endif
  putStrLn ""
