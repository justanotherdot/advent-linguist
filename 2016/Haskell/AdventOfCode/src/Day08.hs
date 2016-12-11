module Day08 where

import           Control.Monad.Trans.State
import           Data.List.Split           (chunksOf, splitOn)
import           Data.Vector               (Vector, (!), (++))
import qualified Data.Vector               as V
import           Prelude                   hiding ((++))

data Command = Rect Integer Integer
             | RotRow Integer Integer
             | RotCol Integer Integer
             deriving Show

type LCDScreen = Vector Bool

toRect :: String -> Command
toRect s = Rect (read $ head vals) (read $ last vals)
  where vals = splitOn "x" s

-- Ugly.
toRot :: [String] -> Command
toRot ss = case t of
            "row"    -> RotRow ix amt
            "column" -> RotCol ix amt
            _        -> error "Unrecognized command while parsing"
  where t   = head ss
        ix  = read . last . splitOn "=" . head . take 1 . drop 1 $ ss
        amt = read $ last ss

toCommand :: String -> Command
toCommand s = case head parts of
                "rect"   -> toRect (last parts)
                "rotate" -> toRot (tail parts)
                _        -> error "Unrecognized command while parsing"
  where parts = words s

pprintLCD :: LCDScreen -> IO ()
pprintLCD lcd = mapM_ printIt chopped
  where chopped = chunksOf 50 (V.toList lcd)
        printIt s = do
          mapM_ (\x -> if x then putStr "#" else putStr ".") s
          putStrLn ""

parseInput :: String -> [Command]
parseInput s = map toCommand ls
  where ls = filter (not . null) . lines $ s

rectOn :: Integer -> Integer -> State LCDScreen ()
rectOn width height = do
    lcd <- get
    let lcd' = V.update lcd . V.fromList $ rectIxs width height
    put lcd'
  where
    rectIxs :: Integer -> Integer -> [(Int, Bool)]
    rectIxs w h
      | w*h > 300  || w == 0 || h == 0 || w > 50 || h > 6 = []
      | otherwise  = concatMap makeRow cols
      where
        cols = [0, 50 .. (h' * 50 -1)]
        [w', h'] = map (\x -> fromIntegral x :: Int) [w, h]
        makeRow offset = zip [(offset :: Int) .. (w'+offset-1)] (repeat True)

rotateRight :: Int -> Int -> Vector a -> Vector a
rotateRight amount upperBound vec = prefix ++ suffix
  where prefix = V.take amount $ V.drop (upperBound - amount) vec
        suffix = V.take (upperBound - amount) vec

rotRow :: Integer -> Integer -> State LCDScreen ()
rotRow rowNo qty = modify (\lcd -> V.update lcd $ rotRowIxs lcd rowNo qty)
  where
    rotRowIxs :: LCDScreen -> Integer -> Integer -> Vector (Int, Bool)
    rotRowIxs vec row amt
        | row >= 6 || row < 0 = V.empty
        | otherwise = V.zip ixs vec'
      where
        row'   = fromIntegral row :: Int
        amt'   = fromIntegral (amt `mod` 50) :: Int
        ixs    = V.enumFromTo (row'*50) (row'*50+50-1)
        rowVec = V.take 50 $ V.drop (row' * 50) vec
        vec'   = rotateRight amt' 50 rowVec

rotCol :: Integer -> Integer -> State LCDScreen ()
rotCol colNo qty = modify (\lcd -> V.update lcd $ rotColIxs lcd colNo qty)
  where
    rotColIxs :: LCDScreen -> Integer -> Integer -> Vector (Int, Bool)
    rotColIxs vec col amt
        | col >= 50 || col < 0 = V.empty
        | otherwise = V.zip ixs vec'
      where
        col'   = fromIntegral col :: Int
        amt'   = fromIntegral (amt `mod` 6) :: Int
        ixs    = V.enumFromStepN col' 50 6
        colVec = V.map (vec !) ixs
        vec'   = rotateRight amt' 6 colVec

processCommand :: Command -> State LCDScreen ()
processCommand (Rect x y)     = rectOn x y
processCommand (RotRow i amt) = rotRow i amt
processCommand (RotCol j amt) = rotCol j amt

solveDay08 :: FilePath -> IO ()
solveDay08 path = do
  s <- readFile path
  putStrLn "Solution for day eight: "
  let emptyLCD  = V.replicate (5*60) False
  let filledLCD = execState (mapM_ processCommand $ parseInput s) emptyLCD
  print . length . V.filter (==True) $ filledLCD
  pprintLCD filledLCD
  putStrLn ""
