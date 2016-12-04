module Day02 where

import           Data.Foldable   (foldl')
import           Data.Map.Strict (Map)
import qualified Data.Map.Strict as M

type KeypadPos = Integer
type Command   = Char

transitions :: Map (KeypadPos, Command) KeypadPos
transitions = M.fromList [((1, 'R'), 2), ((1, 'D'), 4)
                         ,((2, 'L'), 1), ((2, 'R'), 3), ((2, 'D'), 5)
                         ,((3, 'L'), 2), ((3, 'D'), 6)
                         ,((4, 'U'), 1), ((4, 'R'), 5), ((4, 'D'), 7)
                         ,((5, 'U'), 2), ((5, 'R'), 6), ((5, 'D'), 8), ((5, 'L'), 4)
                         ,((6, 'U'), 3), ((6, 'L'), 5), ((6, 'D'), 9)
                         ,((7, 'U'), 4), ((7, 'R'), 8)
                         ,((8, 'L'), 7), ((8, 'U'), 5), ((8, 'R'), 9)
                         ,((9, 'L'), 8), ((9, 'U'), 6)]

transition :: KeypadPos -> Command -> KeypadPos
transition pos cmd = M.findWithDefault pos (pos, cmd) transitions

processLine :: KeypadPos -> [Command] -> KeypadPos
processLine = foldl' transition

processLines :: [[Command]] -> String
processLines = snd . foldl' go (5, "")
  where go (pos, str) line = let pos' = processLine pos line
                             in (pos', str ++ show pos')

solveDay02 :: FilePath -> IO ()
solveDay02 path = do
  putStrLn "Solution for day two: "
  ls <- readFile path
  putStrLn . processLines . lines $ ls
  putStrLn ""
