module Day10 where

solveDay10 :: FilePath -> IO ()
solveDay10 path = do
  s <- readFile path
  putStrLn "Solution for day ten: "
  print s
  putStrLn ""
