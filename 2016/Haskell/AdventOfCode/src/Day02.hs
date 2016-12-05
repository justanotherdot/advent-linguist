module Day02 (solveDay02) where

import           Data.Foldable   (foldl')
import           Data.Map.Strict (Map)
import qualified Data.Map.Strict as M

type KeypadPos = Char
type Command   = Char

transitions :: Map (KeypadPos, Command) KeypadPos
transitions = M.fromList [(('1', 'R'), '2'), (('1', 'D'), '4')
                         ,(('2', 'L'), '1'), (('2', 'R'), '3'), (('2', 'D'), '5')
                         ,(('3', 'L'), '2'), (('3', 'D'), '6')
                         ,(('4', 'U'), '1'), (('4', 'R'), '5'), (('4', 'D'), '7')
                         ,(('5', 'U'), '2'), (('5', 'R'), '6'), (('5', 'D'), '8'), (('5', 'L'), '4')
                         ,(('6', 'U'), '3'), (('6', 'L'), '5'), (('6', 'D'), '9')
                         ,(('7', 'U'), '4'), (('7', 'R'), '8')
                         ,(('8', 'L'), '7'), (('8', 'U'), '5'), (('8', 'R'), '9')
                         ,(('9', 'L'), '8'), (('9', 'U'), '6')]

transitions' :: Map (KeypadPos, Command) KeypadPos
transitions' = M.fromList [(('1', 'D'), '3')
                         ,(('9', 'L'), '8')
                         ,(('D', 'U'), 'B')
                         ,(('5', 'R'), '6')
                         ,(('2', 'R'), '3'), (('2', 'D'), '6')
                         ,(('4', 'L'), '3'), (('4', 'D'), '8')
                         ,(('C', 'U'), '8'), (('C', 'L'), 'B')
                         ,(('A', 'U'), '6'), (('A', 'R'), 'B')
                         ,(('6', 'U'), '2'), (('6', 'R'), '7'), (('6', 'D'), 'A'), (('6', 'L'), '5')
                         ,(('3', 'U'), '1'), (('3', 'R'), '4'), (('3', 'D'), '7'), (('3', 'L'), '2')
                         ,(('8', 'U'), '4'), (('8', 'R'), '9'), (('8', 'D'), 'C'), (('8', 'L'), '7')
                         ,(('B', 'U'), '7'), (('B', 'R'), 'C'), (('B', 'D'), 'D'), (('B', 'L'), 'A')
                         ,(('7', 'U'), '3'), (('7', 'R'), '8'), (('7', 'D'), 'B'), (('7', 'L'), '6')]

transition :: Map (KeypadPos, Command) KeypadPos -> KeypadPos -> Command -> KeypadPos
transition m pos cmd = M.findWithDefault pos (pos, cmd) m

processLine :: Map (KeypadPos, Command) KeypadPos -> KeypadPos -> [Command] -> KeypadPos
processLine m = foldl' (transition m)

processLines :: Map (KeypadPos, Command) KeypadPos -> KeypadPos -> [[Command]] -> String
processLines m start = snd . foldl' go (start, "")
  where go (pos, str) line = let pos' = processLine m pos line
                             in (pos', str ++ [pos'])

solveDay02 :: FilePath -> IO ()
solveDay02 path = do
  putStrLn "Solution for day two: "
  ls <- readFile path
  putStrLn "Part 1: "
  putStrLn . processLines transitions '5' . lines $ ls
  putStrLn "Part 2: "
  putStrLn . processLines transitions' '5' . lines $ ls
  putStrLn ""
