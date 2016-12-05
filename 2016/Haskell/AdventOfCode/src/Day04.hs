-- module Day04 (solveDay04) where
module Day04 where

import           Control.Monad   (mapM_)
import           Data.Char       (isDigit)
import           Data.Function   (on)
import           Data.List       (group, nub, sort, sortBy)
import           Data.List.Split (splitOn, wordsBy)

isSquareBracket :: Char -> Bool
isSquareBracket c = c == '[' || c == ']'

break' :: String -> (String, String)
break' s = (concat $ takeWhile (not . isDigit . head) ss, last ss)
  where ss = splitOn "-" s

breakDogtag :: String -> (Integer, String)
breakDogtag s = (read (head ss) :: Integer, last ss)
  where ss = wordsBy isSquareBracket s

mostFrequent :: String -> String
mostFrequent = concat . sortBy (compare `on` (negate . length)) . group . sort

processLine :: String -> (String, String, Integer)
processLine s = (givenName, checksum, value)
  where parts             = break' s
        (value, checksum) = breakDogtag . snd $ parts
        givenName         = take (length checksum) . nub . mostFrequent $ fst parts

solveDay04 :: FilePath -> IO ()
solveDay04 path = do
  putStrLn "Solution for day four: "
  ls <- readFile path
  let ls' = map processLine . lines $ ls
  -- mapM_ print ls'
  print $ foldr (\(s, s', v) x -> if s == s' then x + v else x) 0 ls'
  putStrLn ""
