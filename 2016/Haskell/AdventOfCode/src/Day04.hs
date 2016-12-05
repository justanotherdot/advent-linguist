-- module Day04 (solveDay04) where
module Day04 where

import           Control.Monad   (mapM_)
import           Data.Char       (chr, isDigit, ord)
import           Data.Function   (on)
import           Data.List       (group, nub, sort, sortBy)
import           Data.List.Split (splitOn, wordsBy)

isSquareBracket :: Char -> Bool
isSquareBracket c = c == '[' || c == ']'

break' :: String -> ([String], String)
break' s = (takeWhile (not . isDigit . head) ss, last ss)
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
        sorted            = nub . mostFrequent . concat . fst $ parts
        givenName         = take (length checksum) sorted

processLine' :: String -> (String, Integer)
processLine' s = (unwords . fst $ parts, value)
  where parts      = break' s
        (value, _) = breakDogtag . snd $ parts

decryptShiftRight :: Integer -> Char -> Char
decryptShiftRight _ ' ' = ' '
decryptShiftRight n c   = chr (k + ord 'a')
  where n' = fromIntegral n :: Int
        k  = mod (ord c - ord 'a' + n') (ord 'z' - ord 'a' + 1)

decryptName :: (String, Integer) -> (String, Integer)
decryptName (s, v) = (map (decryptShiftRight v) s, v)

solveDay04 :: FilePath -> IO ()
solveDay04 path = do
  putStrLn "Solution for day four: "
  ls <- readFile path
  let ls' = map processLine . lines $ ls
  print $ foldr (\(s, s', v) x -> if s == s' then x + v else x) 0 ls'
  let ls'' = map processLine' . lines $ ls
  let ss = map decryptName ls''
  mapM_ print $ filter (\x -> head (fst x) == 'n') ss
  putStrLn ""
